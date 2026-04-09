class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Lion(Animal):
    def roar(self):
        print("RRRRRRRRRWWWWAAAHHHHHH")


dog = Dog("Oreo")
cat = Cat("Mike")
lion = Lion("Sheru")

print(lion.name)
lion.roar()
print(lion.is_alive)

