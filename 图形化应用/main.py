import tkinter as tk
from view import InputFrame, QueryFrame, DeleteFrame, ChangeFrame, AboutFrame

# 主界面
class MainPage:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry('600x400')

        menuber = tk.Menu(self.root)
        self.input_page = InputFrame(self.root)
        self.query_page = QueryFrame(self.root)
        self.delete_page = DeleteFrame(self.root)
        self.change_page = ChangeFrame(self.root)
        self.about_page = AboutFrame(self.root)

        self.root.title('学生信息管理系统 (V2.72)')

        menuber.add_command(label='录入', command=self.show_input)
        menuber.add_command(label='查询', command=self.show_all)
        menuber.add_command(label='删除', command=self.show_delete)
        menuber.add_command(label='修改', command=self.show_change)
        menuber.add_command(label='关于', command=self.show_about)
        self.root.config(menu=menuber)
    def show_input(self):
        self.delete_page.pack_forget()
        self.query_page.pack_forget()
        self.change_page.pack_forget()
        self.about_page.pack_forget()
        self.input_page.pack()

    def show_all(self):
        self.input_page.pack_forget()
        self.delete_page.pack_forget()
        self.change_page.pack_forget()
        self.about_page.pack_forget()
        self.query_page.pack()

    def show_delete(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.change_page.pack_forget()
        self.about_page.pack_forget()
        self.delete_page.pack()

    def show_change(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.about_page.pack_forget()
        self.change_page.pack()

    def show_about(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.change_page.pack_forget()
        self.about_page.pack()

if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()






