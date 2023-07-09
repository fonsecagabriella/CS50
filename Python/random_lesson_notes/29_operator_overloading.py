class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self. knuts = knuts
    
    def __str__(self):
        return f"{self.galleons} Galleaons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):
        # this other here doesn't need to be the same object
        # it can be any type you would like to add here
        # as long as you define it properly
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
 


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

# combining the values of the vaults
# this is called operator overloading 
# you need to define the function __add__ in the class
total = potter + weasley
print (total)
