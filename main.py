# This is an example of how the CLASS can be made in Python script.
class Šuņuks:

    kind = 'krancis'         # class variable shared by all instances

    def __init__(self, name, age):
        self.name = name    # instance variable unique to each instance
        self.vecums = age

    # Another instance method
    def speak(self, sound):
        return f"{self.name} saka {sound}"


# Creating INSTANCES (Instantiation of the 'Šūņuks' CLASS)
s1 = Šuņuks('Rembo', 3)
s2 = Šuņuks('Tontons', 10)

# The BUSINESS & LOGIC
print('Manu vienu suniiti sauc ' + s1.name + ', modelis ir ' + s1.kind + ', bet vecums ir ' + str(s1.vecums))
print('Mana otrā suņuka marka ir ' + s2.kind + ', un to vienkārši sauc - ' + s2.name)
print(s1.speak("Wow"))

