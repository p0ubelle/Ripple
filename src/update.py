
import requests
import os 
import pathlib


INSTALLED_VERSION = "v0.0.1-alpha"  # Change this in each release



if os.name == "nt":
    ripple_folder = os.path.join(os.getenv("APPDATA"), "Ripple")
    os.makedirs(ripple_folder, exist_ok=True)
    pin_file_path = os.path.join(ripple_folder, "version.txt")
    exe_path = os.path.join(pathlib.Path(__file__).parent.resolve(), "Ripple.exe")




def get_latest_release(update_message = "There is a new version available! Please update to the latest version."):
    url = 'https://api.github.com/repos/p0ubelle/Ripple/tags'
    response = requests.get(url)
    data = response.json()
    if isinstance(data, list) and data:
        return data[0]["name"]
    return None  


def install_update(new_version):
    url = f'https://github.com/p0ubelle/Ripple/releases/download/{new_version}/Ripple.exe'
    print(url)
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        print(f"Downloading {new_version}...")

        with open(exe_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print("Update downloaded successfully!")
        with open(pin_file_path, "w") as f:
            f.write(get_latest_release())
            
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



if get_latest_release() != version:
    install_update(get_latest_release())
else:
    print("You are up to date!")
