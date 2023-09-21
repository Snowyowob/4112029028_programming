book = [
    {"name":"book1","quantity":10,"price":120},
    {"name":"book2","quantity":15,"price":240},
    {"name":"book3","quantity":8,"price":200},
    {"name":"book4","quantity":16,"price":160}
    ]

while True:
    service = int(input("How can I help you?\n1.Add books\n2.Remove books\n3.Update books\n4.Display book list\n5.Book ordering\n6.End program\n"))
    if service == 1:
        tn = str(input("Book name:"))
        tq = int(input("Book number:"))
        tp = int(input("Book price:"))
        td = {"name":tn,"quantity":tq,"price":tp}
        book.append(td)
        print(f"\n{tn} added successfully\n")
    else:
        if service == 2:
            removing = str(input("Book name:"))
            for removal in book:
                if removing == removal['name']:
                    book.remove(removal)
                    print(f"\n{removing} removed successfully\n")
        else:
            if service == 3:
                updating = str(input("Book name:"))
                for update in book:
                    if updating == update['name']:
                        nq = int(input("Number of the book:"))
                        update['quantity'] = nq
                        print(f"\nThe number of {updating} has been changed to {nq}\n")
            else:
                if service == 4:
                    print("\nThe books here are:\n")
                    for temp in book:
                        print(f"Name:{temp['name']},  Price:{temp['price']}, Quantity:{temp['quantity']}")
                    print("\n")
                else:
                    if service == 5:
                        total_amount = 0
                        while True:
                            order_name = str(input("Book name:"))
                            if order_name == "stop":
                                break
                            for item in book:
                                if order_name == item['name']:
                                    oq = int(input("Book number:"))
                                    if oq <= item['quantity']:
                                        total_amount += item['price']*oq
                                        item['quantity'] -= oq
                                    else:
                                        print("\nNot enough book\n")
                        if total_amount >= 500:
                            if total_amount >= 1000:
                                total_amount *= 0.8
                                print("\nCongrats, you received a 20% discount.")
                            else:
                                total_amount *= 0.9
                                print("\nCongrats, you received a 10% discount.")
                        print(f"Your order cost {total_amount}\n")
                    else:
                        if service == 6:
                            print("\nThanks for using, please come again.")
                            break
                        else:
                            print("\nInvalid service, please try again\n")