import csv
import datetime


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost
    
class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__("Klasik Pizza", 20)
    
    
class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 25)
    
    
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk Pizza", 30)
    
    
class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 15)
        
class PizzaDecorator(Pizza):
    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost
        
    def get_description(self):
        return self.component.get_description() + ' ' + self.description
    
    def get_cost(self):
        return self.component.get_cost() + self.cost

class Zeytin(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "Zeytin ile", 2)
        

class Mantar(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "Mantar ile", 3)
        

class KeciPeyniri(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "Keci Peyniri ile", 4)
        

class Et(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "Et ile", 5)
        

class Sogan(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "Sogan ile", 1)
        

class MISIR(PizzaDecorator):
    def __init__(self, component):
        super().__init__(component, "MISIR ile", 2)
        
def display_menu():
    with open("Menu.txt", "r") as file:
        print(file.read())
        
def get_pizza():
    while True:
        choice = input("Lütfen Sipariş Vermek İstediğiniz Pizzayı Seçiniz (1-4): ")
        if choice == "1":
            return KlasikPizza()
        elif choice == "2":
            return MargheritaPizza()
        elif choice == "3":
            return TurkPizza()
        elif choice == "4":
            return SadePizza()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
            
def get_sauce(pizza):
    while True:
        choice = input("Eklemek İstediğiniz Sosu Seçiniz (11-16): ")
        if choice == "":
            print("Sos seçmediniz.")
            return pizza
        elif choice == "11":
            return Zeytin(pizza)
        elif choice == "12":
            return Mantar(pizza)
        elif choice == "13":
            return KeciPeyniri(pizza)
        elif choice == "14":
            return Et(pizza)
        elif choice == "15":
            return Sogan(pizza)
        elif choice == "16":
            return MISIR(pizza)
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyiniz.")
            
def get_customer_info():
    name = input("Adınızı Giriniz: ")
    
    while True:
        user_id = input("Kullanıcı Adınızı Giriniz: ")
        if user_id == "admin":
            print("Sisteme Kayıtlı Adresiniz Bulunmuştur.")
            break
        else:
            print("Geçersiz Kullanıcı adı. Tekarar Deneyiniz.")

    card_number = input("Lütfen Ödeme Yapmak İstediğiniz Banka veya Kredi Kartı numaranızı Giriniz: ")

    while True:
        card_pin = input("Lütfen Kart Şifrenizi Giriniz: ")
        if len(card_pin) == 4 and card_pin.isdigit():
           break
        print("Geçersiz şifre. Lütfen 4 haneli şifrenizi giriniz.")

    return name, user_id, card_number, card_pin

def add_order_to_database(pizza, name, user_id, card_number, card_pin):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("Orders_Database.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Saat:" + timestamp, " İsim:" + name, " Id:" + user_id, " Kart No:" + card_number, " Kart Şifre:" + card_pin, " Pizza:" + pizza.get_description(), " Ücret:" + str(pizza.get_cost()) + "₺"])

def main():
    display_menu()
    print("Merhaba Pizzacı'ya Hoşgeldiniz! Sağlıklı Günler Dileriz.\n")
    pizza = get_pizza()
    pizza = get_sauce(pizza)
    users_order = pizza.get_description()
    total_cost = pizza.get_cost()
    print("Siparişiniz: " + users_order)
    print("Toplam Tutar: " + str(total_cost) + "₺\n")
    
    name, user_id, card_number, card_pin = get_customer_info()
    add_order_to_database(pizza, name, user_id, card_number, card_pin)
    print("Siparişiniz Onaylanmıştır. Tahmini teslimat süresi FOREVER\n\nBizi Tercih Ettiğiniz İçin Teşekkürler...\n")
    

if __name__ == '__main__':
    main()