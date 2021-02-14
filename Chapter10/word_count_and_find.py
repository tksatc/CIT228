def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename, searchWord):
    """Search for words in a file, counts occurrences of the word"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{filename} wasn't found.")
    else:
        words = contents.split()
        for word in words:
            word.lower()
        wordToSearch = searchWord.lower()
        timesInText = contents.count(wordToSearch)
        print(f"\nThe word, {searchWord}, occurred {timesInText} times in the {filename} file.")

filenames = ['Chapter10/pride_prejudice.txt', 'Chapter10/jekyll_hyde.txt', 'Chapter10/sherlock_holmes.txt', 'Chapter10/a_tale_of_two_cities.txt', 'Chapter10/huckleberry_finn.txt', 'Chapter10/mountain_interval.txt']
for filename in filenames:
    count_words(filename)

word = input("\nEnter a common word to search for in the books: ")

for filename in filenames:
    find_words(filename, word)