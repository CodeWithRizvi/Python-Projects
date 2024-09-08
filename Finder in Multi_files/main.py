import os

def isRizvi(filename):
    with open(filename, "r") as f:
        fileContent=f.read()

    if "rizvi" in fileContent.lower():
        return True
    # else:
    #     return False
    
if __name__ == "__main__":

    dir_contents = os.listdir()
    nRizvi = 0
    for item in dir_contents:
        if item.endswith("txt"):
            print(f"Detecting Rizvi in {item}")
            # Call the isRizvi function to check if 'rizvi' is in the file
            flag= isRizvi(item)
            # If 'rizvi' is found, increase the counter and print a message
            if(flag):
                print(f"Rizvi found in {item}")
                nRizvi +=1
            else:
                # If 'rizvi' is not found, print a different message
                print(f"Rizvi not found in {item}")
        # Print a summary of the results
    print("*****Rizvi Detector Summary******")
    print(f"{nRizvi} files found with Rizvi hidden intoo them")
