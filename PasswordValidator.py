while True:
    password = input()
    u = n = i = 0

    for j in password:
        if j.isupper() == True: u += 1
        elif j.isdigit() == True: n += 1
        elif (j == " ")or (j == "=") or (j == "?") or (j == "\t"): i += 1
    
    if u >= 2 and n >2 and i == 0 and len(password) >= 8:
        print("The password you entered is valid")
        break
    else:
        print(f'Invalid Password, Please Enter a new password')
        continue


