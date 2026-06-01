
class MyPerson:
    def __init__(self, name, surname, alias = ("Sin Alias")):
        self.full_name = f"{name} {surname} ({alias})"

    def sleep(self):
        print(f"{self.full_name} esta durmiendo")

my_person = MyPerson("Baro", "Vero")
print(my_person.full_name)
my_person.sleep()

my_other_person = MyPerson("Yuli", "Almeida", "La Yoli")
print(my_other_person.full_name)
my_other_person.sleep()

my_other_person.full_name = "Cosme Fulanito (Ay amor!)"
print(my_other_person.full_name)
print(my_other_person.full_name)
my_other_person.sleep()

def nombre(nombre,apellido):
    print(nombre,apellido)

nombre("Mariano" , "Gualla")