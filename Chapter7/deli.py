sandwich_orders = ["club", "blt", "chicken", "italian", "peanut butter and jelly", "grilled cheese", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []

print("\nWe are out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich.title()} sandwich.")

print("\n------Sandwiches Made-------")

for sandwich in finished_sandwiches:
    print(sandwich.title())
