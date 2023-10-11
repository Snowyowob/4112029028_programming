Lesson_list = []

                
            

while True:
    selection = 0
    TSI = int(input("Please enter your ID:"))
    if TSI < 1000000000 or TSI > 9999999999:
        print("Error")
    else:
        TSN = input("Please enter your name:")
        T_user = {"SID":TSI, "Sname":TSN}
        while selection != "5":
            selection = input(f"Welcome student {TSN}, which service do you want:\n1.Add class\n2.Choose class\n3.Delete class\n4.Logout\n")        
            if selection == "1":
                TCI = int(input("Please enter the class ID:"))
                if TCI < 1000 or TCI > 9999:
                    print("Error")
                else:
                    TCN = input("Please enter the class name:")
                    TCP = input("Please enter the Professor:")
                    TCT = input("Please enter the class time:")
                    TC = {"CID":TCI, "Cname":TCN, "Professor":TCP, "Ctime":TCT}
                    Lesson_list.append(TC)
                    for i in Lesson_list:
                        print(f"ID:{i['CID']}\nName:{i['Cname']}\nProfessor:{i['Professor']}\nTime:{i['Ctime']}")
            elif selection == "2":
                TID = input("Please enter class ID:")
                for lessons in Lesson_list:
                    if TID == lessons['CID']:
                        T_user["Chosen_Class"] = lessons['Cname']
            elif selection == "3":
                TID = input("Please enter class ID:")
                for lessons in Lesson_list:
                    if TID == lessons['CID']:
                        if T_user["Chosen_Class"] == lessons['Cname']:
                            T_user.remove(lessons['Cname'])
            