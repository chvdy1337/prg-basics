import queue

# Create a stack using LifoQueue
stack = queue.LifoQueue()

# Push numbers onto the stack
stack.put(2)
stack.put(3)
stack.put(7)
stack.put(4)
stack.put(1)
stack.put(9)
stack.put(8)

# Sum the last two numbers and print the result
# Pop the last two numbers from the stack
last = stack.get()  # Pop the last element
second_last = stack.get()  # Pop the second last element

# Sum of the last two numbers
sum_last_two = last + second_last
print(f"Sum of the last two numbers: {sum_last_two}")

# Calculate the sum of the remaining stack elements
remaining_sum = 0
while not stack.empty():
    remaining_sum += stack.get()

print(f"Sum of the remaining stack elements: {remaining_sum}")
