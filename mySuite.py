import tkinter
import tkinter.messagebox
import customtkinter as ctk

#Setting appearance mode and default colour for window
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Myfinance(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.geometry("1200x1000")
        self.title("TestWindow")

class MySuite(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("My Suite")
        self.geometry("650x450")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.button1 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button1.grid(row=0, column=0, pady=10, padx=10, sticky="nesw")

        self.button2 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button2.grid(row=0, column=1, pady=10, padx=10, sticky="nesw")

        self.button3 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button3.grid(row=0, column=2, pady=10, padx=10, sticky="nesw")

        self.button4 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button4.grid(row=1, column=0, pady=10, padx=10, sticky="nesw")

        self.button5 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button5.grid(row=1, column=1, pady=10, padx=10, sticky="nesw")

        self.button6 = ctk.CTkButton(master=self, text="Login", command=self.open_topLevel)
        self.button6.grid(row=1, column=2, pady=10, padx=10, sticky="nesw")
        
        self.toplevel_window = None
        
    def login(self):
        print("hmm")
        
    def open_topLevel(self):
        print()
        if self.toplevel_window is None or not self.teplevel_window.winfo_exists():
           self.toplevel_window = Myfinance(self) 
        else:
            self.toplevel_window.focus()

if __name__ == "__main__":
    app = MySuite()
    app.mainloop()
    
    
    
# root = ctk.CTk()
# frame = ctk.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill="both", expand=True, sticky="nesw")
# label = ctk.CTkLabel(master=frame, text="Login sys")
# label.pack(pady=12, padx=10)
# entry1 = ctk.CTkEntry(master=frame, placeholder_text="User")
# entry1.pack(pady=12,padx=10)
# entry2 = ctk.CTkEntry(master=frame, placeholder_text="User", show="*")
# entry2.pack(pady=12,padx=10)
# checkbox = ctk.CTkCheckBox(master=frame, text="Remember me")
# checkbox.pack(pady=12, padx=10)