# Write a list comprehension that generates a list of the lengths of the words in a given sentence. For example, if the
#    sentence is "Hello world, how are you?", the list comprehension should produce [5, 5, 3, 3, 4].

sentence = input("Enter a sentence: ")
lengths = [len(word) for word in sentence.split()]
print(lengths)

