# Functions examples

def Sumnumbers(a, b):
    print(a + b)

def GreetMe():
    print("Good Morning")

def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)


Sumnumbers(12, 43)
GreetMe()
print(opera2("suma", 21, 77))


