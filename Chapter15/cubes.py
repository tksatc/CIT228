import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]

# Plot 1 - Cubes
cubes = []

for num in input_values:
    cubes.append(num*num*num)

ax1 = plt.subplot(1, 2, 1)
ax1.plot(input_values, cubes, marker='*', ls='dashed', lw='2', c='#326C4C')
plt.title("Cubed Numbers")
plt.xlabel("Input Values")
plt.ylabel("Values Cubed")
plt.grid()

# Plot 2 - Raised to the 2nd Power
pow = []

for num in input_values:
    pow.append(num**2)

ax2 = plt.subplot(1, 2, 2)
plt.style.use("seaborn-paper")
ax2.plot(input_values, pow, color='purple', marker='^')
plt.title("Raised Numbers")
plt.xlabel("Input Values")
plt.ylabel("2nd Power Value")
plt.grid(color='gainsboro')

# Draw graphs
plt.suptitle("Fun with Numbers", c='red', fontfamily="Bookman Old Style", fontsize="16")
plt.show()
