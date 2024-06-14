class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    def get_balance(self):
        total_balance = sum(item["amount"] for item in self.ledger)
        return total_balance
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = f"{item['description'][:23]:23}"
            amount = f"{item['amount']:>7.2f}"
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    total_spent = 0
    spent_per_category = []
    
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_per_category.append(spent)
        total_spent += spent
    
    percentages = [int((spent / total_spent) * 100) for spent in spent_per_category]
    
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    
    chart += "    -" + "---" * len(categories) + "\n"
    
    max_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_length) for category in categories]
    
    for x in range(max_length):
        chart += "     "
        for name in names:
            chart += f"{name[x]}  "
        chart += "\n"
    
    chart = chart.rstrip("\n")
    
    return title + chart

# Example usage
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
clothing.deposit(500, "deposit")
clothing.withdraw(32.45, "shirt")
auto.deposit(1000, "deposit")
auto.withdraw(150, "tires")

food.transfer(20, clothing)

print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))