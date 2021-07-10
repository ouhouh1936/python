# SingleTone
class Person :

    name = ""
    age = 0
    gender = ""

    def data_setter(self, p1, p2, p3) :
        self.name = p1
        self.age = p2
        self.gender = p3
    def __str__(self) :
        return f"{self.name} | {self.age} | {self.gender}"
    def add_age(self) :
        self.age = self.age + 1