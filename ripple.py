import customtkinter
import bcrypt
import os
import sys
from CTkMessagebox import CTkMessagebox
from customtkinter import filedialog
from src.riot import launch_riot_client
from src.cb import set_clipboard
from src.importacc import extract_accounts
from src.pin import check_first_time
from src.update import check_update

# Set the default color theme
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



class Ribble(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Ribble")
        self.resizable(False, False)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        # _________ OPTIONS BUTTONS
        self.option_frame = customtkinter.CTkFrame(self, bg_color="transparent")
        self.option_frame.grid(column=1, row=0, sticky="nsew", padx=(0,10), pady=20)

        self.refresh_btn = customtkinter.CTkButton(self.option_frame, text="Initialise", command=self.import_file)
        self.refresh_btn.grid(row=0, pady=5)

        self.launchriot_btn = customtkinter.CTkButton(self.option_frame, text="Open Riot", command=launch_riot_client)
        self.launchriot_btn.grid(row=1, pady=5)

        self.import_btn = customtkinter.CTkButton(self.option_frame, text="Import File", command=self.import_file)
        self.import_btn.grid(row=2, pady=5)

        self.update_btn = customtkinter.CTkButton(self.option_frame, text="Check Update", command=check_update)
        self.update_btn.grid(row=3, pady=5, sticky="s")

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
    if check_first_time() == True:
        os.system("cls")
        ripple()
    else:
        print(check_first_time())
