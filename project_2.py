# Python Project :- 2
# Project Name :- Password Strength Checker.

import re          # regular expression module

# Password Strength Checker Condition :-
#  min 8 chars,digit,uppercase,lowercase,special chars.

def check_password_strength(password):
# for checking length of password
    if len(password)<8:
        return "Weak:Password Must be atleast 8 characters"

# for checking digits is present in password or not
    if not any(char.isdigit()for char in password):
        return "Weak:Password Must Contain a Digit"

# for checking uppercase is present in password or not  
    if not any(char.isupper()for char in password):
        return "Weak:Password Must Contain a Uppercase char"  

# for checking lowercase is present in password or not
    if not any(char.islower()for char in password):
        return "Weak:Password Must Contain a Lowercase Char"    

# for checking special char is present in password or not
    if not re.search (r'[!@#$%^&*(){}<>?.]',password):
        return "Medium:Password Must Contain a Special Char"    

    return "Strong:Your Password is Secured...!"


# User Input  
def password_checker():
    print("Welcome To The Password Strength Checker")

    while True:
        password =input("Enter Your Password(Or Type 'Exit' To Quit): ")

        if password.lower()=='exit':
            print("Thank You For Using This Tool")
            break

        result=check_password_strength(password)
        print (result)


# run the password checker tool
if __name__=="__main__":
    password_checker()        