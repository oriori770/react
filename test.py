import random

a = [random.randint(0, 100) for i in range(100)]
print(a)
even = []
odd_number = []
for i, num in enumerate(a):
    if i % 2 != num % 2:
        if i % 2 == 0:
            even.append((i, num))
        else:
            odd_number.append((i, num))

print('even', even)
print( 'odd_number', odd_number)
for i in range(min)