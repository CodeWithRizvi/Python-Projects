# Function to perform a transformation on the list 'b'
def transform(b):
    # Iterate over the list 'b' up to the second-to-last element
    for i in range(len(b) - 1):
        # If the current element is '1'
        if b[i] == '1':
            # Change the current element to '0'
            b[i] = '0'
            # If the next element is '0', change it to '1'
            if b[i + 1] == '0':
                b[i + 1] = '1'
            # Otherwise, change it to '0'
            else:
                b[i + 1] = '0'
    # Return the modified list 'b'
    return b

# Main code execution
if __name__ == "__main__":
    # Convert the string "01111111101110111" to a list of characters
    a = list("01111111101110111")
    print(a)  # Print the initial list
    
    # Keep transforming the list until it no longer changes
    while a != transform(a.copy()):
        # Apply the transformation and update 'a'
        a = transform(a.copy())
        print(a)  # Print the list after each transformation
