class RestaurantTable:
    menus = {
        'apple':2000,
        'fanta':1000,
        'mango':2500
    }

    def __init__(self):
        self.total = 0
        self.orders =[]

    def addOrder(self,order):
        self.orders.append(order)
        self.total += self.menus[order]

    def printBill(self):
        print("****RECEIPT****")
        for order in self.orders:
            print('f{order}:{self.menus[order]}')
            print("****thankyou***")

def menu():
    print("wlecome")
    print("below id thw neni")
    print('apple'+ str(2000))
    print('fanta'+ str(1000))
    print('mango'+str(2500))

    table = RestaurantTable()
    while True:
        order =input("order: ")
        table.addOrder(order)

        another=input("yes/no:")

        if another == 'yes':
            continue
        if another =='no':
            table.printBill()
            break
menu()



