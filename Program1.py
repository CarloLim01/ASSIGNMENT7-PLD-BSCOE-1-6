#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants1 in the input 
#Example:
#Input: Bahala kayo dyan
#Output:
#Words: 3
#Vowels: 6
#Consonants: 8

user_sentence = input("Enter a sentence: ")

def words_number():
    words = len(user_sentence.split())
    print(f"Number of Words: {words}")

def vowels_number():
    count = 0
    for num in user_sentence:
        if (num == "a" or num == "A" or num == "e" or num == "E" or num == "i" or num == "I" or num == "o" or num == "O" or num == "u" or num == "U"):
            count = count + 1
    print(f"Number of Vowels: {count}")
