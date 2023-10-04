class Purchaseable:
    def purchase(self, quantity, price_per_unit):
        total_cost = quantity * price_per_unit
        return total_cost
class Spendable:
    def cts(self, purchase):
        total_spent = sum(purchase)
        return total_spent
class Discountable:
    def apply_discount(self, price, dpe):
        dpr = price * (1 - dpe / 100)
        return dpr
class Remain_stock:
    def RS(self, amount, purchase_amount):
        remain = amount - purchase_amount
        return remain
class Book(Purchaseable, Spendable, Discountable, Remain_stock):
    def __init__(self, isbn, title, author, price, stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        
    def display_info(self):
        return f"Title:{self.title}, Author:{self.author}, Price:${self.price}"

while True:
    ti = input("Please enter the ISBN:")
    tt = input("Please enter the title:")
    ta = input("Please enter the author:")
    tp = float(input("Please enter the price:"))
    ts = int(input("Please enter the stock:"))
    b1 = Book(ti, tt, ta, tp, ts)
    purchase_quantity = int(input("Please enter the bought amount:"))
    unit_price = b1.price
    total_cost = b1.purchase(purchase_quantity, unit_price)
    purchases = [total_cost]
    total_spent = b1.cts(purchases)
    remain = b1.RS(b1.stock, purchase_quantity)
    dpe = int(input("Please enter the discount:"))
    dpr = b1.apply_discount(b1.price, dpe)
    print("Purchase successfully\ninfo:")
    print(b1.display_info())
    print(f"\nPurchase {purchase_quantity} copies of book 1 for ${total_cost}.")
    print(f"Total spent: ${total_spent}")
    print(f"\nDiscounted price of Book 1 after {dpe}% discount: ${dpr}")
    print(f"\nRemain stock:{remain}")