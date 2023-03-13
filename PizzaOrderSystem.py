from Pizza import *
from Sos import *
import datetime
import csv
import time



class PizzaOrderSystem():

    # Pizza nesnesi oluşunca otomatik olarak oluşan nesneler.

    def __init__(self):
        print("KOESU Pizzaya hoşgeldiniz.\n")
        print("Menümüz..\n")
        self.doc = open("Menu.txt","r",encoding='utf-8').readlines()
        self.total_cost = 0
        self.sepet = {}
        self.fis_kayit = {}
        self.fis_kayit_pizza = []
        self.fis_kayit_sos = []


        
    def taban_menü(self):
        for i in range(5):
            print(self.doc[i])

    def sos_menü(self):         
        for i in range(5,len(self.doc)):
            print(self.doc[i])

    def cost_change(self, x,y):
        self.total_cost += (x+y)

    def get_total_cost(self):
        return f"{self.total_cost} TL"    
        
    
    def sipariş_kayit(self):

        # Müşteriden bilgiler alınır ve dict olarak kaydedilir.

        print("Ödeme ekranına yönlendiriliyorsunuz...")
        time.sleep(1)
        self.fis_kayit["Isim"] = input("\nİsim: ")
        self.fis_kayit["Soyisim"] = input("Soyisim: ")
        self.fis_kayit["Telefon"] = input("Telefon: ")
        self.fis_kayit["Tc NO"] = input("TC No: ")
        self.fis_kayit["KartBilgi"] = input("Kart Numaranız: ")
        self.fis_kayit["KartSifre"] = input("Şifreniz: ")
        self.fis_kayit["Fiyat"] = self.get_total_cost()
        self.tarih()
        self.fis_kayit["Tabanlar"] = self.fis_kayit_pizza
        self.fis_kayit["Soslar"] = self.fis_kayit_sos
        print("Afiyet olsun :)")

    def tarih(self):
        # Tarihin otomatik olarak kayıt edildiği yer.

        self.fis_kayit["Tarih"] = datetime.datetime.ctime(datetime.datetime.now())

    def fis_ver(self):

        # Sipariş tamamlandıktan sonra gösterilen fiş kısmı.
        print()
        print("Fişiniz hazırlanıyor...")
        time.sleep(1)
        print("İsim = ", self.fis_kayit["Isim"])
        print("Soyisim = ", self.fis_kayit["Soyisim"])
        print("Fiyat = ", self.fis_kayit["Fiyat"])
        print("Tarih = ", self.fis_kayit["Tarih"])

    def sepete_ekle(self, p):

        if(p.get_name() in self.sepet.keys()):
            self.sepet[p.get_name()] += 1
        else:
            self.sepet[p.get_name()] =  1   

    def alinan_göster(self):
        # En son sipariş edilenlerin gösterildiği yer.

        print("Alınanlar: ")
        for a,b in self.sepet.items():
            print(a,b, "adet")  
                  

    def add_csv(self):

        # Müşteri verileri ve sipariş edilen pizza tabanı ve sosunun kayıt altına alındığı yer.
        with open("orders.csv", mode="a", newline="") as dosya: 
            writer = csv.writer(dosya, delimiter=';')
            writer.writerow([self.fis_kayit["Isim"], self.fis_kayit["Soyisim"], 
                             self.fis_kayit["Telefon"],self.fis_kayit["Tc NO"],
                             self.fis_kayit["KartBilgi"], self.fis_kayit["KartSifre"], 
                             self.fis_kayit["Tarih"], self.fis_kayit["Fiyat"],
                             self.fis_kayit["Tabanlar"], self.fis_kayit["Soslar"]])
                    

    def siparis_pizza(self):

        # Pizza tabani seçim yeri
        self.taban_menü()
        pizza_tabani =  input("Pizza tabanı  seçiniz: ")

        if(pizza_tabani == "1"):
            pizza = Klasik()

        elif(pizza_tabani == "2"):
            pizza = Margarita()

        elif(pizza_tabani == "3"):
            pizza = TürkPizza()

        elif(pizza_tabani == "4"):
            pizza = SadePizza()

        else:
            print("Öyle bir pizza yok!!!")

        self.sepete_ekle(pizza)
        self.fis_kayit_pizza.append(pizza.get_name())
            

        return pizza    

    def siparis_sos(self):

        # Pizza sosu seçim yeri
        
        self.sos_menü()
        pizza_sosu = input("Pizza sosu seçiniz: ")

        if(pizza_sosu == "11"):
            sos = Zeytin()

        elif(pizza_sosu == "10"):
            sos = Sossuz()    

        elif(pizza_sosu == "12"):
            sos = Mantar()

        elif(pizza_sosu == "13"):
            sos = Peynir()

        elif(pizza_sosu == "14"):
            sos = Et()

        elif(pizza_sosu == "15"):
            sos = Soğan()

        elif(pizza_sosu == "16"):
            sos = Misir()

        else:
            print("Öyle bir pizza yok!!!")

        self.sepete_ekle(sos)
        self.fis_kayit_sos.append(sos.get_name())
    
           
        return sos

         


