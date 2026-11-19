
# Q1 - Username Validation System

# Accept username from the user
username = input("Enter your username: ")

# Remove extra spaces from beginning and end
clean_username = username.strip()

# Check username conditions
if clean_username == "":
    print("Invalid Username: Username cannot contain only spaces.")

elif len(clean_username) < 5:
    print("Invalid Username: Username must contain at least 5 characters.")

elif clean_username.lower() == "admin":
    print("Invalid Username: 'admin' is not allowed.")

else:
    print("Valid Username: Username accepted.")
