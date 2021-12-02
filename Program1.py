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
