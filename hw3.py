book = [
    {"name":"book1","price":200},
    {"name":"book2","price":100},
    {"name":"book3","price":150},
    {"name":"book4","price":250},
    ]
order = [
    {"name":"book1","quantity":1},
    {"name":"book3","quantity":2}
    ]
total_amount = 0
for i in order:
    for ii in book:
        if i['name'] == ii['name']:
            total_amount += ii['price']*i['quantity']
if total_amount >= 500:
    total_amount *= 0.9
    print("Congrats, you received a 10% discount.")
print(f"Your order cost {total_amount}.")