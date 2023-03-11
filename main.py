class dog:

    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        name=self.name
        age=self.age
        print(f"Dog:{name} age:{age}")

d1 = dog("lord", 4)
d1.info()
d2 = dog("rex", 1)
d2.info()
