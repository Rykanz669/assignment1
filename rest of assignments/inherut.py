class vehical:

 def _init_(self):
    pass
 def make_sound():
    print('loud noise')

class car(vehical):
 def _init_(self):
    pass
 def make_sound():
    print('pomp pomp')

class bike(vehical):
 def _init_(self):
    pass
 def make_sound():
    print('honk honk')

    Bike = bike.make_sound(self = bike)
    Car = car.make_sound()
    Vehical = vehical.make_sound()