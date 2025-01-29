import customtkinter
import subprocess
import sys

class Ribble(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        self.geometry("700x400")
        self.title("Ribble")
        self.resizable(False, False)


        self.quit = customtkinter.CTkButton(self, text="test", fg_color="red", command=self.quit)
        self.quit.pack()


# process = subprocess.Popen(
#     ["./cpp_backend"],  # Use "./cpp_backend.exe" on Windows
#     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
# )
# process.stdout.readline()



if __name__ == "__main__":
    app = Ribble()
    app.mainloop()
