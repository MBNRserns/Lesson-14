class DBZ:
    def __init__(self, name, race, transformations, atk):
        self.name= name
        self.race= race
        self.transformations= transformations
        self.atk= atk

    def displayDetails(self):
        print("The DBZ Character and stats")
        print("Name: ", self.name)
        print("Race: ", self.race)
        print("Top Transformation: ", self.transformations)
        print("Signature Attack: ", self.atk)
    
z1=DBZ("Goku", "Saiyan", "MUI", "Kamehameha")
z2=DBZ("Vegeta", "Saiyan", "Untra Ego", "Galic Gun")
z3=DBZ("Piccolo", "Namekian", "Orange", "Special Beam Cannon")
z4=DBZ("Gohan", "Half Saiyan", "Beast", "One Handed Kamehameha")

z1.displayDetails()
z2.displayDetails()
z3.displayDetails()
z4.displayDetails()