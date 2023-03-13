# Pizza parent class

class Pizza():

    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name

    def get_info(self):
        return f"{self.description} \n{self.cost}"    

# Pizza child class
    
class Klasik(Pizza):
    def __init__(self):
        self.name = "Klasik"
        self.cost = 129.90
        self.description = "İçindekiler: Domates, Mozarella, Sucuk, Siyah zeytin"
              
class Margarita(Pizza):
    def __init__(self):
        self.name = "Margarita"
        self.cost = 119.00
        self.description = "İçindekiler: Domates, Mozarella, Fesleğen, Zeytinyağı"

class TürkPizza(Pizza):
    def __init__(self):
        self.name = "TürkPizza"
        self.cost = 149.00
        self.description = "İçindekiler: Pastırma, Sucuk, Biber, Mantar"

class SadePizza(Pizza):
    def __init__(self):
        self.name = "SadePizza"
        self.cost = 119.00
        self.description = "İçindekiler: Kaşar peynir, Kekik, Domates sosu"

 


