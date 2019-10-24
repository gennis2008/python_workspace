#!_*_coding:uft-8_*_
#__author__:"gavin li"

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.age = addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print("为学员%s 办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass
class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        ('''
        ----info of student:%s -----
        name:%s
        age:%s
        sex:%s
        salary:%s
        course:%s
        ''' % (self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course [%s]" % (self.name,self.course))
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
        -----info of Student:%s -----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        ''' % (self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print("%s has paid tution for $%s" % (self.name,amount))

school = School("坏小孩%s","沙河")
t1 = Teacher("oldboy",56,"MF",200000,"Linux")
t2 = Teacher("gavin",22,"Male",3000,"go")
s1  = Student("aa",18,"M",2000,"pythondevs")
s2  = Student("bb",20,"M",2000,"devs")

t1.tell()
s1.tell()
school.hires(t1)
school.enroll(s1)
print(school.students)
print(school.staffs)
