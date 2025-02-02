import customtkinter
from customtkinter import filedialog
from src.riot import launch_riot_client
from src.cb import set_clipboard
from src.importacc import extract_accounts

customtkinter.set_default_color_theme("themes\\coffee.json")


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

        self.showpass_btn = customtkinter.CTkSwitch(self.option_frame, text="Show Passwords", variable=True)



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


    def show_passwords(self):
        print("showing passwords...")
        self.passwords.configure(text="passwords")
        self.showpass_btn.configure(text="Hide Passwords", command=self.hide_passwords)



# process = subprocess.Popen(
#     ["./cpp_backend"],  # Use "./cpp_backend.exe" on Windows
#     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
# )
# process.stdout.readline()



if __name__ == "__main__":
    app = Ribble()
    app.mainloop()
