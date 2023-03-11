class Dog:
    name = "Ayra"
    years = 5
    def dog_years(self):
        return self.years*7
    def speak(self):
        print("Hello name is {} . Baw Baw".format(self.name))

ayra = Dog()
ayra.speak()
print(ayra.name)
ayra.years = int(input("How old is your dog? "))
print(ayra.dog_years())
print(ayra.years)


