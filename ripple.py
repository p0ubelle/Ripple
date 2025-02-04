import customtkinter
import bcrypt
import os
import sys
from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog
from src.riot import launch_riot_client
from src.cb import set_clipboard
from src.importacc import extract_accounts



if getattr(sys, 'frozen', False):
    # If the app is frozen (compiled into .exe), use the path inside the temporary folder
    theme_path = os.path.join(sys._MEIPASS, "themes", "coffee.json")
else:
    # If running from source, use the relative path
    theme_path = "themes\\coffee.json"

customtkinter.set_default_color_theme(theme_path)
def ripple():
    app = Ribble()
    app.mainloop()





if os.name == "nt":
    ripple_folder = os.path.join(os.getenv("APPDATA"), "Ripple")
    os.makedirs(ripple_folder, exist_ok=True)
    pin_file_path = os.path.join(ripple_folder, "pin.txt")


def check_first_time():
    pin_top_lvl = customtkinter.CTk()

    a = pin_top_lvl.winfo_screenwidth() // 2
    b = pin_top_lvl.winfo_screenheight() // 2
    pin_top_lvl.geometry(f"{200}x{150}+{a}+{b}")
    pin_top_lvl.title("PIN")

    pin_entry = customtkinter.CTkEntry(pin_top_lvl, show="*", placeholder_text="Enter PIN")
    pin_entry.place(relx=0.5, rely=0.5, anchor="center")
    bottom_label = customtkinter.CTkLabel(pin_top_lvl, text="Enter your PIN", font=("Arial", 10))
    bottom_label.place(relx=0.5, rely=0.3, anchor="center")

    def on_submit():
        if not os.path.exists(pin_file_path) or os.path.getsize(pin_file_path) == 0:
            set_pin()
        else:
            check_pin()

    def set_pin():
        def on_submit():
            pin = pin_entry.get()
            if pin:
                pin_entry.delete(0, "end")
                bottom_label.configure(text="Re-enter your PIN")

                def confirm_pin():
                    if pin_entry.get() == pin:
                        hashed_pin = bcrypt.hashpw(pin.encode(), bcrypt.gensalt()).decode()
                        with open(pin_file_path, "w") as f:
                            f.write(hashed_pin)
                        pin_top_lvl.destroy()
                    else:
                        print("PINs do not match")
                        CTkMessagebox(title="Error", message="Does not match", icon="cancel")

                submit_button.configure(command=confirm_pin, text="Confirm")
                pin_entry.unbind("<Return>")
                pin_entry.bind("<Return>", lambda event: confirm_pin())
            else:
                pin_entry.configure(placeholder_text="PIN cannot be empty")

        submit_button = customtkinter.CTkButton(pin_top_lvl, text="Register", command=on_submit)
        submit_button.place(relx=0.5, rely=0.8, anchor="center")

        pin_entry.bind("<Return>", lambda event: on_submit())


    def check_pin():
        def on_submit():
            with open(pin_file_path, "r") as f:
                stored_hash = f.read().strip()
            if bcrypt.checkpw(pin_entry.get().encode(), stored_hash.encode()):
                pin_top_lvl.destroy()
                ripple()
            else:
                pin_entry.delete(0, "end")
                close = CTkMessagebox(title="Error", message="Wrong PIN", icon="cancel", option_1="Retry")
                bottom_label.configure(text="Wrong PIN")

        submit_button = customtkinter.CTkButton(pin_top_lvl, text="Login", command=on_submit)
        submit_button.place(relx=0.5, rely=0.8, anchor="center")

        pin_entry.bind("<Return>", lambda event: on_submit())
    on_submit()
    pin_top_lvl.mainloop()


class Ribble(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Ribble")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # _________ OPTIONS RIGHT BUTTONS
        self.option_frame = customtkinter.CTkFrame(self, bg_color="transparent")
        self.option_frame.grid(column=1, row=0, sticky="nsew", padx=(0,10), pady=20)

        self.refresh_btn = customtkinter.CTkButton(self.option_frame, text="Initialise", command=self.import_file)
        self.refresh_btn.grid(row=0, pady=5)

        self.launchriot_btn = customtkinter.CTkButton(self.option_frame, text="Open Riot", command=launch_riot_client)
        self.launchriot_btn.grid(row=1, pady=5)

        self.import_btn = customtkinter.CTkButton(self.option_frame, text="Import File", command=self.import_file)
        self.import_btn.grid(row=2, pady=5)

        # self.showpass_btn = customtkinter.CTkSwitch(self.option_frame, text="Show Passwords", variable=True)



        self.account_frame = customtkinter.CTkScrollableFrame(self)
        self.account_frame.grid(column=0, row=0, padx=(10), pady=20, sticky="nsew")
        self.account_frame.columnconfigure(1, weight=1)

        self.usernames = customtkinter.CTkLabel(self.account_frame, text="waiting...", font=("Arial", 20))
        self.usernames.grid(row=0, column=0)

        self.passwords = customtkinter.CTkLabel(self.account_frame, text="waiting...", font=("Arial", 20))
        self.passwords.grid(row=0, column=1)


    def import_file(self):
        print("importing file...")
        path = filedialog.askopenfilename()
        extract_accounts(self=self, file=path)


if __name__ == "__main__":
    check_first_time()
