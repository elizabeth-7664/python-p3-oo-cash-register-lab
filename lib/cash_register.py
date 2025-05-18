class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
        self.transactions = []  # Store all transactions for removing items

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        self.transactions.append((title, price, quantity))
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_title, last_price, last_quantity = self.transactions.pop()
            self.total -= last_price * last_quantity
            for _ in range(last_quantity):
                if last_title in self.items:
                    self.items.remove(last_title)
        if not self.transactions:
            self.total = 0.0
