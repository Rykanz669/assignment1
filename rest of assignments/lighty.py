class light:
    brand = "samsung"
    color = "white"
    watts = 50
    def turn_on(self):
        print("light turned on")
    def turn_off(self):
        print("light turned off")
    def change_temp(self):
        pass
class room:
    def __init__(self,l):
        self.watts=50
        self.l=l
l=light()
room=room(l)
room.l.turn_on()