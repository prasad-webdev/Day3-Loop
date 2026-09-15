# correct_pass = "741852" 
# not_found = True

# while not_found:
#     passw = input("enter passs: ")
#     if passw == correct_pass:
#         break
#         # not_found = False

# print("password match")

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1
