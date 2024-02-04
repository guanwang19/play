# mymodule.py

def add_numbers(a, b):
    print(f"I am in {__name__}")
    return a + b

if (__name__ == '__main__'):
    print(add_numbers(2,3))
