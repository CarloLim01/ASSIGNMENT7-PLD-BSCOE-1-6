#Create a program that check if password is valid
#The password is valid if all criteria are met:
#A. Greater than 15 letters
#B. Have at least one capital letter
#C. Have at least one number
#D. Have at least one special char (!@#$%^&*()_+ etc)
#Example:
#Input: P@ssw0rd+P@ssw0rd
#Ouput: Valid

password = input("Enter your password: ")

def password_validator():
    special_character = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ".", "|", ";", ":", "'", "?", ",", "/", "<", ">", "~", "`")
    val = True
    if not any(char in special_character for char in password):
        print("Have atleast 1 character in your password.")
        val = False
    return val
