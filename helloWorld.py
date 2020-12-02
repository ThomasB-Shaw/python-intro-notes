print("Hello World!!!")

if 5>2:
    print("Five is greater than 2!")

x = 5
y = "Hello, World"

print(x)
print(y)

x, y, z = "Brigador", "Hades", "ROR2"

print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


def fizzBuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Buzz"
    elif input % 3 ==0:
        return "Fizz"
    else:
        return input

print(fizzBuzz(5))
print(fizzBuzz(3))
print(fizzBuzz(15))
print(fizzBuzz(19))