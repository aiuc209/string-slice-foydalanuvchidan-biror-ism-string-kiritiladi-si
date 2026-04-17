"""
Hayvonlar (Animals) meros olish
Auto-generated Solution
"""

class Animal:
    def __init__(self, name):
        self.name = name
        self.sound = "Noma'lum"

    def make_sound(self):
        print(f"{self.name} ovozi: {self.sound}")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof!"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Meow!"

if __name__ == "__main__":
    it = Dog("Olapar")
    mushuk = Cat("Momiq")
    
    it.make_sound()
    mushuk.make_sound()
