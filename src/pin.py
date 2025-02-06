import customtkinter
import os
import bcrypt
from CTkMessagebox import CTkMessagebox

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
                        pin_top_lvl.result = True
                        pin_top_lvl.quit()
                        pin_top_lvl.destroy()
                    else:
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
        def verify_pin():
            with open(pin_file_path, "r") as f:
                stored_hash = f.read().strip()
            if bcrypt.checkpw(pin_entry.get().encode(), stored_hash.encode()):
                pin_top_lvl.result = True  # Set result before closing
                pin_top_lvl.quit()
                pin_top_lvl.destroy()
            else:
                pin_entry.delete(0, "end")
                CTkMessagebox(title="Error", message="Wrong PIN", icon="cancel", option_1="Retry")
                bottom_label.configure(text="Wrong PIN", text_color="red")

        submit_button = customtkinter.CTkButton(pin_top_lvl, text="Login", command=verify_pin)  # Fix here
        submit_button.place(relx=0.5, rely=0.8, anchor="center")

        pin_entry.bind("<Return>", lambda event: verify_pin())

    pin_top_lvl.result = False
    on_submit()
    pin_top_lvl.mainloop()

    return pin_top_lvl.result  # Return the result after window closes
