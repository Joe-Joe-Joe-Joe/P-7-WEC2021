with open("Test1.txt", 'r') as f:
    words_lines = f.readlines()

words_lines = [word.strip() for word in words_lines]

print(words_lines)
