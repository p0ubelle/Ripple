
import requests
import os
import pathlib
import customtkinter
from packaging import version as vs


INSTALLED_VERSION = "v0.0.2-alpha"  # Release


def create_frame(tag_name, body, published_date, size, download_url, install_update):
    update_top_lvl = customtkinter.CTk()
    update_top_lvl.geometry("400x300")

    update_top_lvl.columnconfigure(0, weight=1)
    update_top_lvl.rowconfigure(1, weight=1)
    update_top_lvl.rowconfigure(2, weight=1)

    header = customtkinter.CTkLabel(update_top_lvl, text=f"Ripple {tag_name}", font=("Segoe UI Emoji", 16, "bold"))
    header.grid(row=0, column=0)

    body_scrollable_frame = customtkinter.CTkScrollableFrame(update_top_lvl)
    body_scrollable_frame.grid(row=1, column=0, sticky="NSEW", padx=10)

    body_frame = customtkinter.CTkLabel(body_scrollable_frame, text=body, font=("Segoe UI Emoji", 14, "bold"), justify="left", anchor="w")
    body_frame.grid(row=1, column=0)

    footer_frame = customtkinter.CTkFrame(update_top_lvl, height=70)
    footer_frame.grid(row=2, column=0, sticky="NSEW", pady=5, padx=10)
    footer_frame.columnconfigure(0, weight=1)


    file_size = round(float(size)/1024/1024, 1)
    footer_info = customtkinter.CTkLabel(footer_frame, text=f" date: {published_date}  | size: {file_size}Mo", font=("Segoe UI Emoji", 16, "bold"))
    footer_info.grid(row=1, column=0)
    footer_button = customtkinter.CTkButton(footer_frame, width=45)

    if install_update:
        footer_button.configure(command=lambda: install_update(tag_name), text="Install")
    else:
        footer_button.configure(command=lambda: update_top_lvl.destroy(), text="OK")

    footer_button.grid(row=1, column=1)

    update_top_lvl.mainloop()


def check_update():
    if os.name == "nt":
        ripple_folder = os.path.join(os.getenv("APPDATA"), "Ripple")
        os.makedirs(ripple_folder, exist_ok=True)
        pin_file_path = os.path.join(ripple_folder, "version.txt")
        exe_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "Ripple.exe")

    def get_latest_release():
        url = 'https://api.github.com/repos/p0ubelle/Ripple/releases/latest'
        response = requests.get(url)
        data = response.json()

        if "tag_name" in data and "body" in data and "published_at" in data:
            if "assets" in data and len(data["assets"]) > 0:
                return data["tag_name"], data["body"], data["published_at"], data["assets"][0]["size"], data["assets"][0]["browser_download_url"]
        return None

    def install_update(new_version):
        url = f'https://github.com/p0ubelle/Ripple/releases/download/{new_version}/Ripple.exe'
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            print(f"Downloading {new_version}...")

            with open(exe_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            print("Update downloaded successfully!")
            with open(pin_file_path, "w") as f:
                f.write(new_version)

            return True
        else:
            print("Failed to download update.")
            return False


    if not os.path.exists(pin_file_path):
        with open(pin_file_path, "w") as f:
            f.write(INSTALLED_VERSION)
        version = INSTALLED_VERSION
    else:
        with open(pin_file_path, "r") as f:
            version = f.read().strip()

    program_version = vs.parse(INSTALLED_VERSION)
    already_installed_version = vs.parse(version)
    if program_version > already_installed_version:
        version = INSTALLED_VERSION
        with open(pin_file_path, "w") as f:
            f.write(version)


    latest_release = get_latest_release()

    if latest_release:
        if latest_release[0] != version:
            create_frame(*latest_release, install_update)
        else:
            print("You are up to date!")
            create_frame(*latest_release, install_update=None)

    else:
        print("Failed to fetch the latest release.")
