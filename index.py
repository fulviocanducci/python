def Source(a):
    return (a)


def Sum(a, b):
    return a + b


class People:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def setName(self, name):
        self.name = name
        return self

    def setId(self, id):
        self.id = id
        return self

    def getId(self):
        return self.id

    def getName(self):
        return self.name


print(Source('Fúlvio'))
print(Source('Hugo'))
print(Sum(10, 20))

people = People(1, "Fulvio")
print(str.format("{0} {1}",  people.getId(), people.getName()))

print(people.id)
