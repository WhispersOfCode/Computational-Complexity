import csv
import time
import matplotlib.pyplot as plt

# Create or open a CSV file to store input sizes and elapsed times
filename = "time_data.csv"
results = []

n = int(input("How many different input sizes do you want to test? "))

for _ in range(n):
    List = [];
    i = int(input("Enter the number of elements in the list: "));

    if i % 2 == 0:
        i += 1 # Ensure i is odd, therefore we add 1 to it implying that the list will have 1 element more than the input if it is even
        print("The number of elements in the list is even, so it has been incremented by 1 to make it odd.")
        print("The number of elements in the list is now:", i)
    else:
        i = i
    range_list = range(1,(i+1)//2,1);

    start_time = time.time()

    def generate_list1(range_list):
        for j in range_list:
            List.append(j);
        return List
    generate_list1(range_list)

    List.append((i + 1) // 2)

    def generate_list2(range_list):
        a = list(range_list)[::-1]  # Reverse the list
        List.extend(a)  # Extend instead of append
        return List
    generate_list2(range_list)

    print(List)
# This code generates a list of integers based on user input, ensuring the list has a specific structure.   
# The list starts with numbers from 1 to (i+1)//2, followed by the middle element, and then the reverse of the first half.  
# The final list is printed, showing the complete sequence. 
# The code ensures that the input number of elements is odd, and constructs a symmetric list around the middle element. 

    copy_List = List.copy()  # Create a copy of the original list   
    copy_List.reverse()  # Reverse the copied list
    if(copy_List == List):
        print("The generated List is a palindrome")
    else:
        print("The generated List is not a palindrome")
# The code generates a symmetric list based on user input and checks if it is a palindrome.

    end_time = time.time()
    elapsed_time = end_time - start_time
    results.append((i, elapsed_time))  # store the full set

# Graphical Interpretation of Polynomial time:
# Write all new results at once (overwrite mode)
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["input_size", "time_taken"])
    writer.writerows(results)

# Read and plot
input_sizes = []
time_taken = []

with open(filename, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        input_sizes.append(int(row["input_size"]))
        time_taken.append(float(row["time_taken"]))

plt.plot(input_sizes, time_taken, marker='o', color='blue')
plt.title("Input Size vs Time Taken")
plt.xlabel("Input Size (i)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)
plt.show()