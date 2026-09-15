correct_pass = "741852" 
not_found = True

while not_found:
    passw = input("enter passs: ")
    if passw == correct_pass:
        not_found = False

print("password match")