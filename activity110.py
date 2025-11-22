class Dog:
    
    animal = "Dog"

    def _init_(self, breed, color):

        self.breed = breed
        self.color = color

    def display(self):
        print(f"Animal: {Dog.animal}")
        print(f"Breed : {self.breed}")
        print(f"Color : {self.color}")
        print("------------------------")

dog1 = Dog("German Shepherd", "Black and Tan")
dog2 = Dog("Labrador", "Golden")

print("Details of Dog 1:")
dog1.display()

print("Details of Dog 2:")
dog2.display()