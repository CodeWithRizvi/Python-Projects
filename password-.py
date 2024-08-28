#                                ## Sample code 
# # Define the correct password
# password="Younas Ali"
# # Prompt the user to enter the password initially
# your_input=input("Enter password : ")
# # Loop while the entered password is not correct
# while password != your_input:
#     # Loop while the entered password is not correct
#     your_input = input("Enter password : ")
#     # This block is executed once the entered password matches the correct password
# else:
#     print("Unlocked !")




                               ## Advance pattern 
# Define the correct password
password = "Younas Ali"

# Set the maximum number of attempts allowed
max_attempts = 3

# Initialize the number of attempts made
attempts = 0

# Loop to allow user to enter the password up to the maximum number of attempts
while attempts < max_attempts:
    # Prompt the user to enter the password
    your_input = input("Enter password: ")
    
    # Check if the entered password matches the correct password
    if your_input == password:
        print("Unlocked!")
        break  # Exit the loop if the password is correct
    else:
        # Increment the number of attempts made
        attempts += 1
        
        # Calculate the remaining number of attempts
        remaining_attempts = max_attempts - attempts
        
        # Provide feedback to the user
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempts left.")
        else:
            print("Too many incorrect attempts. Access denied.")
