def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

sum = add(3, 4, 5, 5, 2, 3, 20202, 2039)
print(sum)

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["edwin"]
    n *= kwargs["noah"]

    print(n)

calculate(2, edwin = 41, noah = 6)

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)