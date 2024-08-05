import user_scan as srm

# Defining the list to store the inputted data
user_data = []

print("***Enter the user data***")

choice = True
i = 1
# Loop to get as many records as you want
while choice:
    print("User ", i)
    name = input("Enter name: ")
    email = input("Enter email: ")
    data = f"{name},{email}"
    user_data.append(data)
    more = input("Do you want to add another user? (yes/no): ")
    # Using .lower() to account for case sensitivity
    if more.lower() == "yes":
        i += 1
    else:
        choice = False

# Concatenate all user data into a single string separated by newlines
all_user_data = "\n".join(user_data)
# Calling the functions to get the outputs
srm.generate_qr_code(all_user_data)

srm.RegisterUserFromSmartScan("imgqr.png")