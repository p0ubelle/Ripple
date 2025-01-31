import customtkinter as ctk

class Ribble(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Ribble")
        self.resizable(False, False)

        # Initial Theme State (Light Mode)
        self.current_theme = "light"
        ctk.set_appearance_mode("light")  # Default theme

        # Colors for themes
        self.light_bg = "#FFFFFF"
        self.dark_bg = "#181818"
        self.light_btn = "#E0E0E0"
        self.dark_btn = "#303030"

        # Set Initial Background Color
        self.configure(fg_color=self.light_bg)

        # Theme Toggle Button
        self.theme_button = ctk.CTkButton(self, text="Switch Theme", command=self.toggle_theme)
        self.theme_button.pack(pady=20)

    def toggle_theme(self):
        """Smoothly transition between themes without restarting the window"""
        if self.current_theme == "light":
            start_color, end_color = self.light_bg, self.dark_bg
            start_btn, end_btn = self.light_btn, self.dark_btn
            new_theme = "dark"
        else:
            start_color, end_color = self.dark_bg, self.light_bg
            start_btn, end_btn = self.dark_btn, self.light_btn
            new_theme = "light"

        self.fade_background(start_color, end_color, start_btn, end_btn, steps=30, delay=20)
        self.current_theme = new_theme

    def fade_background(self, start, end, start_btn, end_btn, steps=30, delay=20):
        """Smoothly fades background and button color without causing window reset"""
        start_rgb = self.hex_to_rgb(start)
        end_rgb = self.hex_to_rgb(end)
        start_btn_rgb = self.hex_to_rgb(start_btn)
        end_btn_rgb = self.hex_to_rgb(end_btn)

        step_rgb = [(e - s) / steps for s, e in zip(start_rgb, end_rgb)]
        step_btn_rgb = [(e - s) / steps for s, e in zip(start_btn_rgb, end_btn_rgb)]

        def update_color(step=0):
            if step <= steps:
                new_rgb = [int(start_rgb[i] + step_rgb[i] * step) for i in range(3)]
                new_btn_rgb = [int(start_btn_rgb[i] + step_btn_rgb[i] * step) for i in range(3)]
                new_hex = self.rgb_to_hex(new_rgb)
                new_btn_hex = self.rgb_to_hex(new_btn_rgb)

                # Apply background color change without window reset
                self.configure(fg_color=(new_hex, new_hex))  # Background change
                # Apply button color change
                self.theme_button.configure(fg_color=(new_btn_hex, new_btn_hex))

                # Schedule next update
                self.after(delay, update_color, step + 1)
            else:
                # Set the final theme mode after animation completes
                ctk.set_appearance_mode(self.current_theme)

        update_color()  # Start animation

    def hex_to_rgb(self, hex_color):
        """Convert hex to RGB tuple"""
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_color):
        """Convert RGB tuple to hex"""
        return f"#{''.join(f'{c:02x}' for c in rgb_color)}"

if __name__ == "__main__":
    app = Ribble()
    app.mainloop()
