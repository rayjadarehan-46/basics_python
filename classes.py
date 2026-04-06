class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if not self.openseats():
            return False 
        self.passengers.append(name)
        return True
       

    
    def openseats(self):
       return self.capacity - len(self.passengers)

flight = Flight(3)
people = ["fayjal","firoj","nasim","rehan"]

for person in people:
    succes = flight.add_passenger(person) 
    if succes:
        print(f"{person} added succesfully")
    else:
        print(f"unable to add {person}, no seats available")