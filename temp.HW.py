class student:
    def __init__(self, SID, Sname, Chosen_class):
        self.SID = SID
        self.Sname = Sname
        self.Chosen_class = Chosen_class
    def class_choosing(self, TID):
        for lessons in Lesson_list:
            if TID == lessons['CID']:
                    student['Chosen_class'] = lessons['Cname']
            else:
                print("Error")
    def class_deleting(self, TID):
        for lessons in Lesson_list:
            if TID == lessons['CID']:
                if student['Chosen_class'] == lessons['Cname']:
                    student.remove(lessons['Cname'])
                else:
                    print("Error")
Lesson_list = []
class Lesson:
    def __init__(self, CID, Cname, Professor, Ctime):
        self.CID = CID
        self.Cname = Cname
        self.Professor = Professor
        self.Ctime = Ctime
    def class_adding(self, TCI, TCN, TCP, TCT, TC):
            TCI = float(input("Please enter the class ID:"))
            if TCI < 1000 or TCI > 9999:
                print("Error")
            else:
                TCN = input("Please enter the class name:")
                TCP = input("Please enter the Professor:")
                TCT = input("Please enter the class time:")
                TC = Lesson(TCI, TCN, TCP, TCT)
                Lesson_list.append(TC)
                
            

while True:
    selection = 0
    TSI = float(input("Please enter your ID:"))
    if TSI < 100000000 or TSI > 999999999:
        print("Error")
    else:
        TSN = input("Please enter your name:")
        T_user = student(TSI, TSN, 0)
        while selection != 4:
            selection = input("Welcome student {TSN}, which service do you want:\n1.Add class\n2.Choose class\n3.Delete class\n4.Logout\n")        
            if selection == 1:
                TC = []
                TC.class_adding
                for i in Lesson_list:
                    print(f"ID:{Lesson.CID}\nName:[Lesson.Cname]\nProfessor:{Lesson:Professor}\nTime:{Lesson:Ctime}")
            elif selection == 2:
                TID = input("Please enter class ID:")
                TID.class_choosing
            elif selection == 3:
                TID = input("Please enter class ID:")
                TID.class_deleting