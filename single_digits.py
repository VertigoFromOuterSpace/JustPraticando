# Your code below:
single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
cubes = [num ** 3 for num in single_digits]
for num in single_digits:
  squares.append(num ** 2)
  print(num)
print(squares)
print(cubes)
