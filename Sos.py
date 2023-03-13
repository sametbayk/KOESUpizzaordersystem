# Sos parent class

class Sos():

    def __init__(self,name, cost):
        self.name = name
        
        self.cost = cost

    def get_cost(self):
        return self.cost
    
    def get_name(self):
        return self.name

    def get_info(self):
        return f"\n{self.cost}"    

# Sos child class

class Sossuz(Sos):
    def __init__(self):
        self.name = "Sossuz"
        self.cost = 0.00

class Zeytin(Sos):
    def __init__(self):
        self.name = "Zeytin"
        self.cost = 6.00
        

class Mantar(Sos):
    def __init__(self):
        self.name = "Mantar"
        self.cost = 6.00
        

class Peynir(Sos):
    def __init__(self):
        self.name = "Peynir"
        self.cost = 8.00
        

class Et(Sos):
    def __init__(self):
        self.name = "Et"
        self.cost = 10.00
        

class Soğan(Sos):
    def __init__(self):
        self.name = "Soğan"
        self.cost = 7.00
        

class Misir(Sos):
    def __init__(self):
        self.name = "Misir"
        self.cost = 6.50
        

    