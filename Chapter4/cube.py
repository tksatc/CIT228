print("\n-----------------Exercise 4-8------------------")

cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

print(cubes)

print("\n-----------------Exercise 4-9------------------")

cubes = [number**3 for number in range(1, 11)]
print(cubes)
