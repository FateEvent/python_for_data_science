from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)

Jaine = King.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}", end=', ')
print(f"Alive : {Jaine.is_alive}")
print(Jaine.__str__)

Joffrey.set_eyes("blue")
Joffrey.set_hair("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hair())
print(Joffrey.__dict__)
