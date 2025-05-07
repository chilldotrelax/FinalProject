'''
Andy Huang (ECE 160: Password Program) 
'''

'''
Things to do next:
1) Clean up the functions, divide masterUtility() into multiple smaller functions.
2) Add improved checking for prescence of passwords.txt 
3) Rewrite some of the code to only open the file once and once only.
4) Eventually rebuild the entire program using classes.
5) Add additional features such as password strength, hidden password, encryption, etc.
6) Employ data bases (such as my sql).
'''
userInfo = dict()

def upon_open(): 
    with open("passwords.txt","r") as f:
        files = f.readlines()
    for i in range(0,len(files)):
        b = []
        files[i] = files[i][:(len(files[i]) - 1)] #Back by 2, get rid of the \n at the end.
        b = files[i].split(',')
        userInfo.update({b[0]:b[1]})
     
def savePassword(): #Save on demand. i hate my life :(
    open('passwords.txt', 'w').close()
    for i in zip(userInfo.items()):
        with open("passwords.txt", "a") as f:
            f.write(f'{i[0][0]},{i[0][1]}\n')

def usernameValidationUtility():
    while True:
        username = input("Please enter a unique username:")
        if username not in userInfo.keys():
            return username
        else:
            print(f'This username has already been taken! Please try again:')
            continue
        
def passwordValidationUtility(username):
    while True:
        password = input("Please type your password:")
        confirmPassword = input("Please confirm your password:")
        u = n = i = 0
        for j in password:
            if j.isupper() == True: u += 1
            elif j.isdigit() == True: n += 1
            elif j.isspace() == True: i += 1
            elif (j == "=") or (j == "?") or (j == ""): i += 1
        if u >= 2 and n >= 2 and i == 0 and len(password) >= 8 and ('\t' not in password) and (confirmPassword == password):
            print(f'Sucess!')
            userInfo.update({username:password})
            savePassword()
            masterUtlity()
            break
        else:
            print("Does not meet the requirements!")
            continue

def passwordValidationUtilityUponPassChange(password):
    u = n = i = 0
    for j in password:
        if j.isupper() == True: u += 1
        elif j.isdigit() == True: n += 1
        elif j.isspace() == True: i += 1
        elif (j == "=") or (j == "?") or (j == ""): i += 1
    if u >= 2 and n >= 2 and i == 0 and len(password) >= 8 and ('\t' not in password):
        return password
    else:
        return False
#THIS WHAT THE FUCK IS "INCORRECT INPUTS I DID NOT FIND THAT IN THE PDF PLEASE FOR THE LOVE OF GOD WHAT THE FUCK IS 'INCORRECT INPUTS'"
def usernameValidationforPassChange():
    username_prompt = input("Please enter your username:")
    for i in userInfo.keys():
        if username_prompt == i:
            passwordChange(username_prompt)
    
    print("Username does not exist.")
    username_prompt = ""
    masterUtlity()

def passwordChange(username): #On the event that the user wants to change their password 
       a = 0
       while True:
            password = input("Please, enter your old password:")
            if a < 2:
                if password != userInfo.get(username):
                    print("Incorrect Password! Try again.") #If u actually get the password wrong three times you are def special
                    a += 1
                    continue
                else:
                    while True:
                        newPassword = input("Please enter your new password:") 
                        passwordChange1 = passwordValidationUtilityUponPassChange(newPassword)
                        if passwordChange1 is not False:
                            print(f'Password changed')
                            userInfo[username] = newPassword
                            savePassword()
                            username = password = ""
                            masterUtlity()
                            break
                        elif passwordChange1 == False:
                            print('Does not meet requirements!')
                            continue
            else: 
                print("You entered the wrong password too many times!")
                masterUtlity()
                 
def masterUtlity(): #I need to clean this shit up 
    while True:
        prompt = input("Please enter 1 to sign up or enter 2 to change your password. Enter q or Q to quit:")
        if prompt == "1": #Condition 1: User wants to sign up.
            username = usernameValidationUtility() # <== This first.
            passwordValidationUtility(username) # <== This second.
        elif prompt == "2": #Conditon 2: User wants to change their password.           
            usernameValidationforPassChange()
        elif prompt == "q" or prompt == "Q": quit()
        else: continue

if __name__ == "__main__":
    upon_open() #DO THIS FIRST DONT MFUCKING MOVE IT
    masterUtlity() #First in sequence.

