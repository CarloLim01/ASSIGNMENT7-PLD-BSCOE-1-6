#Create a program that check if password is valid
#The password is valid if all criteria are met:
#A. Greater than 15 letters
#B. Have at least one capital letter
#C. Have at least one number
#D. Have at least one special char (!@#$%^&*()_+ etc)
#Example:
#Input: P@ssw0rd+P@ssw0rd
#Ouput: Valid

print("\033[1;37;1mPASSWORD VALIDATOR\033[0m")

password = input("\n\33[1;32;1mEnter your password\33[0m: ")

def password_validator():
    special_character = ("!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ".", "|", ";", ":", "'", "?", ",", "/", "<", ">", "~", "`")
    val = True
    if len(password) < 15:
        print("\n\033[1;31;3mHave atleast 15 letters in your password.\33[0m")
        val = False
    if not any(char.isupper() for char in password):
        print("\n\033[1;31;3mHave atleast 1 capital letter in your password.\33[0m")
        val = False   
    if not any(char.isdigit() for char in password):
        print("\n\033[1;31;3mHave atleast 1 number in your password.\33[0m")
        val = False
    if not any(char in special_character for char in password):
        print("\n\033[1;31;3mHave atleast 1 character in your password.\33[0m")
        val = False
    return val

def valid_invalid():
    if (password_validator()):
        print("\n\033[1;33;1mThe PASSWORD you enter is VALID!\033[0m")
    else:
        print("\n\033[1;33;1mThe PASSWORD you enter is INVALID!\033[0m")
      
valid_invalid()

print("\n\033[1;37;1m-THANK YOU FOR USING PASSWORD VALIDATOR-\033[0m")