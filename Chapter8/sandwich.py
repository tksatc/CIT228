def make_sandwich(*contents):
    """Display list of sandwich contents requested"""
    print("\nYour sandwich contains:")
    for content in contents:
        print(f"\t {content}")

make_sandwich("pepperoni", "ham", "lettuce")
make_sandwich("peanut butter", "jelly")
make_sandwich("tuna", "cheese", "tomato", "mustard")
