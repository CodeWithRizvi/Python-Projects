def generateTable(n):
    # Initialize an empty string to store the multiplication table
    table=""
    # Loop through numbers from 1 to 10
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    # Open a file in the "tables" directory with a name based on the number 'n'
    # For example, if n=5, the file will be named "table_5.txt"
    with open(f"tables/table_{n}.txt","w") as f:
        # Write the multiplication table to the file
        f.write(table)
# Loop through numbers from 2 to 20
for i in range(2,21):
    # Call the generateTable function for each number in the loop
    # This will create a multiplication table for each number from 2 to 20
    generateTable(i)
