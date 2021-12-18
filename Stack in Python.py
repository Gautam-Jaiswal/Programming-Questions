##stack in python

def push(stack , val):
    stack.append(val)

def pop(stack):
    if isEmpty(stack):
        print("Cannot Pop----Stack Empty")
        return
    val= stack.pop()
    print(f"Element deleted is {val}")
    
def isEmpty(stack):
    return len(stack) == 0

def top_val(stack):
    if not isEmpty(stack):
        return stack[-1]
    else:
        print("Stack is Empty")

def print_stack(stack):
    for i in reversed(stack):
        print(i)
    
    
if __name__ == '__main__':
    stack = []
    
    n = int(input("enter number of elements of stack :- "))
    for i in range(n):
        push(stack , int(input("enter value :- ")))
    
    print_stack(stack)
    print()
    
    push(stack,6)
    print_stack(stack)
    print()
    
    print(top_val(stack))
    print()
    
    pop(stack)
    print_stack(stack)
    print()
    
    pop(stack)
    pop(stack)
    pop(stack)
    pop(stack)
    
    pop(stack)
    pop(stack)