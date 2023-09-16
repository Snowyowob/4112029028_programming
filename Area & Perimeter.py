while True:
    shape = 0
    shape = input("Please choose your shape\n1.Circle\n2.Rectangle\n3.Triangle\n4.Exit\n")
    shape = int(shape)
    if shape == 1:
        Radius = input("Please insert Radius:")
        Radius = float(Radius)
        area = float(3.14*Radius**2)
        perimeter = float(6.28*Radius)
        print(f"\nYour area is:{area}")
        print(f"Your perimeter is:{perimeter}\n")
    elif shape == 2: 
        side1 = input("Please insert first side:")
        side1 = float(side1) 
        side2 = input("Please insert second side:")
        side2 = float(side2)
        area = float(side1*side2)
        perimeter = float(2*(side1+side2))
        print(f"\nYour area is:{area}")
        print(f"Your perimeter is:{perimeter}\n")
    elif shape == 3:       
        side1 = input("Please insert first side:")
        side1 = float(side1) 
        side2 = input("Please insert second side:")
        side2 = float(side2)
        side3 = input("Please insert third side:")
        side3 = float(side3)
        perimeter = float(side1+side2+side3)
        temp = float(perimeter/2)
        area = float((temp*(temp-side1)*(temp-side2)*(temp-side3))**0.5)
        if area <= 0:
            print("Incorrect input")
        else:
            print(f"\nYour area is:{area}")
            print(f"Your perimeter is:{perimeter}\n") 
    elif shape == 4:
        print("Exit Successfully")
        break