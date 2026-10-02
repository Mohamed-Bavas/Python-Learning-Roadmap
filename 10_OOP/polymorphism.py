class Dog:
    def sound(self):
        print("Dog: Bow Bow")
class Cat:
    def sound(self):
        print("Cat: Meow")
animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()