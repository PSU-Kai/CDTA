import glob
import shutil
import os
import time
import subprocess

# Function to create a stack from replicated files
def create_stack(replicated_files):
    stack = []
    for file in replicated_files:
        stack.append(file)
    return stack

# Function to get the most recent file from the stack
def get_most_recent_file(stack):
    stack.sort(key=os.path.getctime, reverse=True)
    return stack[0]

# Get a list of DTMC SimOut CSV files in the directory
csv_files = glob.glob("DTMC*SimOut.csv")

# Loop over the CSV files
for csv_file in csv_files:
    replicated_files = []
    # Generate 10 copies of the CSV file
    for i in range(1, 11):
        replica_file = f"{csv_file[:-4]}_replica_{i}.csv"
        shutil.copy(csv_file, replica_file)
        print(f"Replica {i} created: {replica_file}")
        replicated_files.append(replica_file)
    

    # Create a stack from the replicated CSV files
    csv_stack = create_stack(replicated_files)

    # Get the most recent file from the stack
    most_recent_file = get_most_recent_file(csv_stack)
    print(f"The most recent file is: {most_recent_file}")

# Remove the remaining files
    for file in csv_stack:
        if file != most_recent_file:
            os.remove(file)
            print(f"File removed: {file}")

replica_files = glob.glob("*_replica_*.csv")

# Run merger.py with all the replica files
command3 = f"python3 merger.py -f {' '.join(replica_files)} -o merged_output.csv"

# Run the third command in the terminal
process3 = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout3, stderr3 = process3.communicate()

# Check if any error occurred during execution
if process3.returncode != 0:
    print(f"An error occurred while executing command 3:")
    print(stderr3.decode("utf-8"))
else:
    print("Command 3 executed successfully!")