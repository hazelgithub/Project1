print("Welcome To Calculator")

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    sub = num1 - num2
    return sub

def mult(num1,num2):
    return (num1 * num2)

def div(num1,num2):
    return (num1/num2)


a = 'i am learning Python, what about you !!!'
b = a.split(' ')
print (len(b))
print (b)
i = 0
while i <= len(b):
    print (b[i])
    i = i + 1

c = sub(3,1)
print(c)

