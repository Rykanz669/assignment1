class Cat:
    def speak(self):
        print("meow!")

class Dog:
    def speak(self):
        print("woof!")

def make_animal_speak(animal):
    animal.speak()

make_animal_speak(Cat())