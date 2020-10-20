print(id(1))

x = 1
print(id(x))

print(id("a"))

x = "a"
print(id(x))

a = [1,2,3]
b = [1,2,3]

print(a)
print(b)

print(id(a))
print(id(b))

a.append(4)
print(a,b)

# Because they have different memory addresses, even though they are the same, they do not impact each other!


#****Be Careful!*****
c = [1,2,3]
d = c

print(c,d)
print(id(c))
print(id(d))

c.append(4)
print(c,d)

# Because they are at the same memory address, one changes the other!

