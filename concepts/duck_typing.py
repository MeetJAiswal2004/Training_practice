### Duck typing is a feature of python's dynamic typing system where an object suitability is determined by its behaviour , methods, and attributes rather than its actual class or inheritance.

## Duck typing is closely related to polymorphism in python ,and it does not require inheritance.

## duck typing focuses on behavior of object V/S type checking focuses on object type.

class Dog:
    def sound(self):
        print("bark")

class Cat:
    def sound(self):
        print("meow")


def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)