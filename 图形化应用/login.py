import tkinter as tk
import tkinter.messagebox
from main import MainPage
class LoginPage:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry('300x180')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.root.title('登录')
        tk.Label(self.page).grid(row=0, column=0)
        tk.Label(self.page, text='账号').grid(row=1, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.W, pady=10)
        tk.Label(self.page, text='密码').grid(row=2, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=1, stick=tk.W, pady=10)

        tk.Button(self.page, text='登录', command=self.login_check).grid(row=3, column=0, stick=tk.W, pady=10)
        tk.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=tk.E, pady=10)

    def login_check(self):
        name = self.username.get()
        pwd = self.password.get()

        if name == 'admin' and pwd == 'admin':
            tkinter.messagebox.showinfo(title='恭喜你！', message='登录成功')
            self.page.destroy()
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title='错误！', message='用户名或密码错误')





if __name__ == '__main__':

    root = tk.Tk()
    LoginPage(root)
    root.mainloop()
