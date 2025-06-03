class light:
    watts = 50
    color = 'white'
    brand = ''
    shape = 'cylindrical'

    def intensity(self):
        pass

    def turn_on(self):
        print('light is on')

    def turn_off(self):
        print('light is off')
light=light

light.turn_on()