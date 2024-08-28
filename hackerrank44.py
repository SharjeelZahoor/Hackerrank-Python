from collections import deque  # Import deque from collections module

# Initialize an empty deque
d = deque()

# Read the number of operations to perform
for i in range(int(input())):
    # Read the operation input
    inp = input()

    # Perform the operation based on the input
    if inp == "pop":
        # Remove and return an element from the right end of the deque
        d.pop()
    elif inp == "popleft":
        # Remove and return an element from the left end of the deque
        d.popleft()
    else:
        # Split the input into command and value
        command, value = inp.split()
        value = int(value)  # Convert value to an integer

        # Perform the operation based on the command
        if command == "append":
            # Add value to the right end of the deque
            d.append(value)
        else:
            # Add value to the left end of the deque
            d.appendleft(value)

# Print the elements of the deque separated by a space
print(*d)


