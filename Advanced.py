y = 4
print(type(y))

a= 5
b= 10
string="Sravya"
print(string + "B")

def func_mul(x):
    return x+1
print(type(func_mul))

string="venkat"
print(string.upper())

class book:
    def page(self):
        print("1")
    def colour(self):
        print("blue")
d=book()
print(d.page())

class puppy:
    def speak(self):
        print("bow")
    def speak_normal_func(self):
        print("bow")
    print(type(speak_normal_func))
