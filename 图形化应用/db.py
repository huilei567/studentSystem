import json
import os

file = 'students.json'
if not os.path.exists(file):
    open(file, 'w')




class StudentsDB:
    def __init__(self):
        self.students = []
        self.load_students_data()


    def insert(self, students):
        self.students.append(students)
    def all(self):
        return self.students

    def delete_by_name(self, name):
        for student in self.students:
            if name==student["name"]:
                self.students.remove(student)
                return True, f'{name}删除成功'
        return False, f"{name}不存在"



    def search_by_name(self, name):
        for student in self.students:
            if name == student["name"]:
                return True, student
        return False, f"{name}不存在"
    def updata(self, stu):
        name = stu['name']
        for student in self.students:
            if name == student["name"]:
                student.update(stu)
                return True, f'{name} 用户数据修改成功'
        return False, f"{name}不存在"


    def save_data(self):
        with open('students.json', mode='w', encoding='utf-8') as f:
            text = json.dumps(self.students, indent=4, ensure_ascii=False)
            f.write(text)


    def load_students_data(self):
        with open('students.json', mode='r', encoding='utf-8') as f:
            data = f.read()
        if data:
            self.students = json.loads(data)

db = StudentsDB()






















