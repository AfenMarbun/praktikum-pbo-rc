import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type
    
    def get_allele(self):
        get_random = random.choice([list(self.blood_type)[0], list(self.blood_type)[1]])
        return get_random

# menggunakan inheritance
class Mother(Father):
    pass

class Child:
    def __init__(self, father, mother):
        father_allele = father.get_allele()
        mother_allele = mother.get_allele()
        self.allele = father_allele + mother_allele
        print(f"child's allele: {self.allele}")

        # rumus untuk tipe darah(A, AB, B, O)
        if self.allele[0] == self.allele[1]:
            self.blood_type = self.allele[0]
        elif self.allele[0] != self.allele[1]:
            if self.allele[1] == 'O' :
                self.blood_type = 'B'
            else:
                self.blood_type = 'AB'
        else:
            self.blood_type = 'O'

    def get_blood_type(self):
        return self.blood_type

father_blood_type = input("Enter father's allele : ")
mother_blood_type = input("Enter mother's allele : ")

father = Father(father_blood_type)
mother = Mother(mother_blood_type)

child = Child(father, mother)
print(f"Child's blood type: {child.get_blood_type()}")
