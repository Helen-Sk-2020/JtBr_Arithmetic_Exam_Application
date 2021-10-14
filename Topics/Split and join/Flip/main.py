text = input()
words = text.split()
for word in words:
    if word.startswith("www.").lower():
        print(word)
        