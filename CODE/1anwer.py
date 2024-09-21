def insert_at_bottom(stack, item):
    # Base case: If the stack is empty, insert the item
    if not stack:
        stack.append(item)
    else:
        # Recursively pop all elements and insert the item at the bottom
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    # Base case: If the stack is empty, return
    if not stack:
        return
    # Pop the top element and reverse the remaining stack
    top = stack.pop()
    reverse_stack(stack)
    # Insert the popped element at the bottom of the reversed stack
    insert_at_bottom(stack, top)

# Example usage
stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)  # Output should be [5, 4, 3, 2, 1]
