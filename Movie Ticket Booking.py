class Movie:
    def __init__(self,name,theatre):
        self.name=name
        self.theatre=theatre
        self.pvr={'GOLD':45, 'SILVER':40, 'RECLINER':20}
        self.inox={'GOLD':45, 'SILVER':40, 'RECLINER':20}
        self.carnival={'GOLD':45, 'SILVER':40, 'RECLINER':20}
    def display_availability(self,t):
        if t=='PVR':
            print(self.pvr)
        elif t=='INOX':
            print(self.inox)
        elif t=='CARNIVAL':
            print(self.carnival)
    def seat_availability(self,t,y,z):
        if t=='PVR':
            self.pvr[y]=self.pvr[y]-z
        elif t=='INOX':
            self.inox[y]=self.inox[y]-z
        elif t=='CARNIVAL':
            self.carnival[y]=self.carnival[y]-z
    def bill(self,y,z,meal):
        total=0.0
        if y=="GOLD":
            total=total+(z*500)
        elif y=="SILVER":
            total=total+(z*300)
        elif y=="RECLINER":
            total=total+(z*150)
        if meal=='yes':
            total=total+500
        total=total+(total*18/100)
        return total
    def info(self,y,z,meal,f):
        print('\nBooking Information:\n')
        print('Movie Name:',x)
        print('Movie Theatre:',t)
        print('Type of Seat:',y)
        print('Number of Seats:',z)
        print('Meal Selected:','yes' if meal=='yes' else 'no')
        print('Total Bill:',f)

m=[]
print('Details to be filled in on the backend:\n')
n=int(input('Enter number of movies available: '))
for i in range(n):
    m.append(Movie(input('Enter movie name: '),['PVR','INOX','CARNIVAL']))
a=1
b=0
print('\nDetails to be filled in for the user: ')
while(a!=0):
    x=input('\nEnter the name of the movie: ')
    for i in range(n):
        if x==m[i].name:
            b=1
            print('Theatres available: ',m[i].theatre)
            t=input('Enter theatre: ').upper()
            print('Seats available:')
            m[i].display_availability(t)
            y=input('Enter the type of ticket: ').upper()
            z=int(input('Enter the number of tickets: '))
            m[i].seat_availability(t,y,z)
            meal=input('Do you want to add a meal? Enter yes or no.: ').lower()
            f=m[i].bill(y,z,meal)
            m[i].info(y,z,meal,f)
    if b==0:
        print('Movie entered is not available.')      
    a=int(input('\nEnter 1 to book again, 0 to exit.: '))
