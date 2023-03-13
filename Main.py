from Pizza import *
from Sos import *
from PizzaOrderSystem import *
import time

order = PizzaOrderSystem()

# Pizza tabanı ve sos nesneleri oluşturuldu.
# Gerekli olan tüm metotlar, fonksiyonlar çağırıldı.
# !!! Kodun çalıştırıldığı main dosyası burası !!!

while (True):
       
    pizza = order.siparis_pizza()
    print("******************************")
    sos = order.siparis_sos()
    print("******************************")
    order.cost_change(pizza.get_cost(), sos.get_cost())       
    print("Tutar: ", order.get_total_cost())
    order.alinan_göster()
    ans = input("Başka bir pizza siparişi vermek ister misiniz?(e/h): ")
    print("******************************")

    if (ans.lower() == "e"):
        continue

    elif (ans.lower() == "h"):
        siparis_onay = input("Siparişinizi onaylıyor musunuz?(e/h): ")
        if (siparis_onay.lower() == "e"):
            order.sipariş_kayit()
            order.add_csv()
            order.fis_ver()
            break
        elif(siparis_onay.lower() == "h"):
            print("Siparişiniz iptal edilmiştir sepetiniz sıfırlanıştır!!!")
            break
        else:
            print("Hatalı seçim!!!")
 
    else:
        print("Hatalı şeçim!!!")
        break
                


