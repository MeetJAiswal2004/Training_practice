## monkey patching is a feature in python that allows you to dynamically modify or replace the existing methods, functions and attributes of the class at run time without changing its actual source code.

## moneky patching real world use case = testing , debugging , no need to modify original code 

## it does not require subclassing 

class Animal:
    def sound(self):
        print("animal makes sound")


def new_sound(self):
    print("this animal barks")

# monkey patching
Animal.sound = new_sound

obj = Animal()
obj.sound()
