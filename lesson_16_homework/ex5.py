# files/large_text_file.txt

def line_with_most_words(file_path):
    with open(file_path, 'r') as file:
        max_line = ''
        max_word_count = 0
        for line in file:
            word_count = len(line.split())
            if word_count > max_word_count:
                max_line = line
                max_word_count = word_count

    return max_line.rstrip()


file_path = input("Enter the file path: ")
result = line_with_most_words(file_path)
print("Line with most number of words:\n", result)
