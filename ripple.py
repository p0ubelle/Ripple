import customtkinter
from cb import set_clipboard

customtkinter.set_default_color_theme("themes\\lavender.json")


class Ribble(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Ribble")
        self.resizable(False, False)


        self.clipboard_btn = customtkinter.CTkButton(self, text="test", fg_color="red", command=self.extract_accounts)
        self.clipboard_btn.pack()


        self.account_frame = customtkinter.CTkScrollableFrame(self, width=650)
        self.account_frame.pack()
        self.account_frame.columnconfigure(1, weight=1)

        self.usernames = customtkinter.CTkLabel(self.account_frame, text="test", font=("Arial", 20))
        self.usernames.grid(row=0, column=0)

        self.passwords = customtkinter.CTkLabel(self.account_frame, text="test", font=("Arial", 20))
        self.passwords.grid(row=0, column=1)



    def extract_accounts(self):
        print("extracting accounts...")
        with open("accounts.txt", "r", encoding="utf-8") as file:
            row=0
            for line in file:
                    if ":" in line:
                        account, password = line.strip().split(":")

                        user_label = customtkinter.CTkLabel(self.account_frame, text=account, font=("Arial", 16))
                        user_label.grid(row=row, column=0, padx=5, pady=2)

                        pass_label = customtkinter.CTkLabel(self.account_frame, text=password, font=("Arial", 16))
                        pass_label.grid(row=row, column=1, padx=5, pady=2)


                        row += 1





# process = subprocess.Popen(
#     ["./cpp_backend"],  # Use "./cpp_backend.exe" on Windows
#     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
# )
# process.stdout.readline()



if __name__ == "__main__":
    app = Ribble()
    app.mainloop()
