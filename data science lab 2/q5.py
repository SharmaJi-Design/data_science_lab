#5. Word Reverser Game 
#Ask the user for a list of words. Reverse each word only if its length is even. Print the new list of 
#words after processing. 

words_input = input("Enter a list of words separated by commas: ")
words = [word.strip() for word in words_input.split(",")]

processed_words = []
for word in words:
    if len(word) % 2 == 0: 
        processed_words.append(word[::-1])
    else: 
        processed_words.append(word)

print("Processed words:", processed_words)





