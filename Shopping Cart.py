class Product:
    def __init__(self, name, price,amount):
        self.name=name
        self.price=price
        self.amount=amount
    def get_price(self,items):
        if(99>items>10):
            x=0.9*items*self.price
        elif(items>99):
            x=0.8*items*self.price
        elif(items<10):
            x=items*self.price
        return x
    def make_purchase(self,items):
        self.amount=self.amount-items
n=int(input("Enter number of products: "))
print()
x=[]
bill=0.0
for i in range(n):
    x.append(Product(input("Enter product name: "),float(input("Enter price: ")),int(input("Enter stock amount: "))))
    print()
print("List of items:")
for i in range(y):
    print(i+1,".",x[i].name)
print()
a=1
while(a!=0):
    a=int(input("Enter 0 to exit or 1 to buy: "))
    if(a==1):
        p=input("Enter name of product: ")
        for i in range(n):
            if(p==x[i].name):
                print("No .of items availiable:",x[i].amount)
                z=int(input("Enter number of items:"))
                bill+=x[i].get_price(z)
                x[i].make_purchase(z)
                print("No .of items availiable:",x[i].amount)
                print()
print("Total bill:$%.2f"%bill)
