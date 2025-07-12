#functions
'''
def greet(name):
   print(f"hello, {name}")

greet("Alice")

def add(a, b):
   return a + b

results = add(2, 5)
print(results)

'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    def greet(name, greeting="hello"):
        print(f"{greeting}, {name}")
        
        greet("bob", "good morinig")