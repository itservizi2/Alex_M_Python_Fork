 # Write a list comprehension that generates a list of the first letter of each word in a given sentence. For example,
 #   if the sentence is "Python is awesome", the list comprehension should produce ['P', 'i', 'a'].

sentence = input("Enter a sentence: ")
first_letters = [word[0] for word in sentence.split()]
print(first_letters)


