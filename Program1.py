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

def consonants_number():
    count = 0
    for num in user_sentence:
        if (num == "b" or num ==  "B" or num == "c" or num == "C" or num == "d" or num == "D" or num == "f" or num == "F" or num == "g" or num == "G" or num == "h" or num == "H" or num == "j" or num == "J" or num == "k" or num == "K" or num == "l" or num == "L" or num == "m" or num == "M" or num == "n" or num == "N" or num == "p" or num == "P" or num == "q" or num == "Q" or num == "r" or num == "R" or num == "s" or num == "S" or num == "t" or num == "T" or num == "v" or num == "V" or num == "w" or num == "W" or num == "x" or num == "X" or num == "y" or num == "Y" or num == "z" or num == "Z"):
            count = count + 1
    print(f"Number of Consonants: {count}")
