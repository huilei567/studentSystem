import tkinter as tk
from tkinter import ttk

from db import db



illustrate ='说明：此为开发版不代表最终版本，仅供参考学习'
# 增
class InputFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        self.name = tk.StringVar()
        self._java = tk.StringVar()
        self._python = tk.StringVar()
        self._mysql = tk.StringVar()

        self.status = tk.StringVar()
        self.create_page()
    def create_page(self):
        tk.Label(self).grid(row=0, column=0)
        tk.Label(self, text='姓名').grid(row=1, column=0, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self.name).grid(row=1, column=1, stick=tk.E, pady=10)
        tk.Label(self, text='java').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self._java).grid(row=2, column=1, stick=tk.E)
        tk.Label(self, text='python').grid(row=3, column=0, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self._python).grid(row=3, column=1, stick=tk.E, pady=10)
        tk.Label(self, text='MySQL').grid(row=4, column=0, stick=tk.W, pady=10)
        tk.Entry(self, textvariable=self._mysql).grid(row=4, column=1, stick=tk.E, pady=10)
        tk.Button(self, text='录入', command=self.recode_student).grid(row=5, column=1, stick=tk.E, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, stick=tk.E, pady=10)

    def recode_student(self):
        stu = {'name':self.name.get(), 'java':self._java.get(),
                'python':self._python.get(), 'MySQL':self._mysql.get()
        }
        self.name.set('')
        self._java.set('')
        self._python.set('')
        self._mysql.set('')
        db.insert(stu)
        self.status.set('提交数据成功')
        db.save_data()
        print(stu)


#  查
class QueryFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        columns = ('name', '_java', '_python', '_MySQL')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('name', width=80, anchor='center')
        self.tree_view.column('_java', width=80, anchor='center')
        self.tree_view.column('_python', width=80, anchor='center')
        self.tree_view.column('_MySQL', width=80, anchor='center')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('_java', text='java')
        self.tree_view.heading('_python', text='python')
        self.tree_view.heading('_MySQL', text='MySQL')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)
        self.show_data_frame()

    def show_data_frame(self):
        for _ in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        students = db.all()
        index = 0
        for stu in students:
            self.tree_view.insert('', index+1, values=(
                stu['name'], stu['java'], stu['python'], stu['MySQL'],
            ))

#  删
class DeleteFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root = master
        tk.Label(self, text='删除数据').pack()
        self.delete_frame = tk.Frame(self)
        self.delete_frame.pack()
        self.status = tk.StringVar()
        self.username = tk.StringVar()
        tk.Label(self.delete_frame, text='请输入要删除学生的姓名').pack(anchor=tk.W, padx=20)
        tk.Entry(self.delete_frame, textvariable=self.username).pack(side=tk.LEFT, padx=20, pady=5)

        tk.Button(self.delete_frame, text='删除', command=self._delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def _delete(self):
        username = self.username.get()
        flag, message = db.delete_by_name(username)
        self.status.set(message)
        db.save_data()


#  改
class ChangeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root =master
        tk.Label(self, text='修改界面').pack()
        self.change_frame = tk.Frame(self)
        self.change_frame.pack()
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self._java = tk.StringVar()
        self._python = tk.StringVar()
        self._MySQL = tk.StringVar()

        tk.Label(self.change_frame).grid(row=0, column=0)
        tk.Label(self.change_frame, text='姓名').grid(row=1, column=0, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self.name).grid(row=1, column=1, stick=tk.E, pady=10)
        tk.Label(self.change_frame, text='java').grid(row=2, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self._java).grid(row=2, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='python').grid(row=3, column=0, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self._python).grid(row=3, column=1, stick=tk.E, pady=10)
        tk.Label(self.change_frame, text='MySQL').grid(row=4, column=0, stick=tk.W, pady=10)
        tk.Entry(self.change_frame, textvariable=self._MySQL).grid(row=4, column=1, stick=tk.E, pady=10)
        tk.Button(self.change_frame, text='查询', command=self._search).grid(row=6, column=0, stick=tk.E, pady=10)
        tk.Button(self.change_frame, text='修改', command=self._change).grid(row=6, column=1, stick=tk.E, pady=10)
        tk.Label(self.change_frame, textvariable=self.status).grid(row=7, column=1, stick=tk.E, pady=10)

    def _search(self):
        flag, info = db.search_by_name(self.name.get())
        if flag:
            self.name.set(info['name'])
            self._java.set(info['java'])
            self._python.set(info['python'])
            self._MySQL.set(info['MySQL'])
        else:
            self.status.set(info)

    def _change(self):
        stu = {'name': self.name.get(), 'java': self._java.get(),
               'python': self._python.get(), 'MySQL': self._MySQL.get()
               }
        self.name.set('')
        self._java.set('')
        self._python.set('')
        self._MySQL.set('')
        db.updata(stu)
        self.status.set('修改数据成功')
        db.save_data()


# 说明
class AboutFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.root =master
        tk.Label(self, text='关于作品：本作品由tkinyer制作').pack(anchor=tk.W)
        tk.Label(self, text='关于作者：海经贸大二huilei推出').pack(anchor=tk.W)
        tk.Label(self, text='版权所有：海经贸大二huilei').pack(anchor=tk.W)
        tk.Label(self, text=illustrate).pack(anchor=tk.W)


















