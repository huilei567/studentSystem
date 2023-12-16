import tkinter as tk
from login import LoginPage

def run_app():
    root = tk.Tk()
    LoginPage(root)
    root.mainloop()



if __name__ == '__main__':
    run_app()
