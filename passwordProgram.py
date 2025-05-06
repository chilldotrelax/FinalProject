#Key = "username"
#Value = "password"
userInfo = dict()
def usernameValidationUtility():
    username = input("Please enter a unique username.")
    for i in userInfo.keys():
            if i == username:
                print("This username has been taken! Please try again.")
                username = input("Please enter a unique username.")
    
    return username

def passwordValidationUtility(password):
    u = n = i = 0

    for j in password:
        if j.isupper() == True: u += 1
        elif j.isdigit() == True: n += 1
        elif j.isspace() == True: i += 1
        elif (j == "=") or (j == "?") or (j == ""): i += 1
    
    if u >= 2 and n >= 2 and i == 0 and len(password) >= 8 and ('\t' not in password):
        return True
    else:
        return False


prompt = input("Please enter 1 to sign up or enter 2 to change your password. Enter q or Q to quit.")

while prompt != "q" or prompt != "Q":
    prompt = input("Please enter 1 to sign up or enter 2 to change your password. Enter q or Q to quit.")
    if prompt == "1": #Condition 1: User wants to sign up.
        usernameValidationUtility()

        while True:
            if passwordValidationUtility == True:
                pass
            else:
                break
