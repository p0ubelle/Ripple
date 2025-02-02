from tkinter import messagebox
import customtkinter

def extract_accounts(self, file="accounts.txt"):
        try:
            print("extracting accounts...")
            self.refresh_btn.configure(text="Refresh")
            with open(file, "r", encoding="utf-8") as file:
                row=0
                for line in file:
                        if ":" in line:
                            username, acc_name, password = line.strip().split(":")
                            password = password[:3] + "*" * 4

                            user_label = customtkinter.CTkButton(self.account_frame, text=username, font=("Arial", 16), fg_color="transparent", border_width=0, hover_color="#313160")
                            user_label.grid(row=row, column=0, padx=5, pady=2)

                            acc_label = customtkinter.CTkButton(self.account_frame, text=acc_name, font=("Arial", 16), fg_color="transparent", border_width=0, hover_color="#313160")
                            acc_label.grid(row=row, column=1, padx=5, pady=2)

                            pass_label = customtkinter.CTkLabel(self.account_frame, text=password, font=("Arial", 16))
                            pass_label.grid(row=row, column=2, padx=5, pady=2)

                            row += 1

        except FileNotFoundError:
            print("file not found")
            messagebox.showerror("Error", "File not found, use import file button")

        except Exception as e:
            print("error", e)
            messagebox.showerror("Error", str(e) + "\n\nCorrect format-> username:account_name:password")
