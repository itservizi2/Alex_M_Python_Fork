text = input("Enter a piece of text: ")

word_list = str.split(text)

word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


for word, count in word_count.items():
    print(f'Word "{word}" was used {count} times.')


