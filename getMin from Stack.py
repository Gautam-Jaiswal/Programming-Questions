def push(stack , aux_stack , val):
    
    if len(stack) ==0 and len(aux_stack) ==0:
        stack.append(val)
        aux_stack.append(val)
    else:
        stack.append(val)
        temp = aux_stack[-1]
        if temp > val:
            aux_stack.append(val)
        else:
            aux_stack.append(temp)

def pop(stack , aux_stack):
    temp = 0
    if len(stack) == 0:
        print("Empty Stack")
        return
    if stack[-1] == aux_stack[-1]:
        temp = stack.pop()
        if len(stack) ==0:
            aux_stack.clear()
        else:    
            while temp == aux_stack[-1]:
                aux_stack.pop()
    else:
        temp = stack.pop()
    
    print(f"Deleted element is {temp}")


def getMin(aux_stack):
    Minimum = aux_stack[-1]
    print(f"Minimum value is {Minimum}")
    
def print_stack(stack):
    for i in reversed(stack):
        print(i , end = " ")

def print_aux_stack(aux_stack):
    for i in reversed(aux_stack):
        print(i , end = " ")


if __name__ == '__main__':
    
    stack = []
    aux_stack = []
    
    push(stack , aux_stack , 1)
    push(stack , aux_stack , 2)
    push(stack , aux_stack , 3)
    push(stack , aux_stack , 0)
    push(stack , aux_stack , 4)
    push(stack , aux_stack , 5)
    push(stack , aux_stack , 6)
    
    print_stack(stack)
    print()
    print_aux_stack(aux_stack)
    print()
    getMin(aux_stack)
    print()
    pop(stack,aux_stack)
    pop(stack,aux_stack)
    pop(stack,aux_stack)
    pop(stack,aux_stack)
    pop(stack,aux_stack)
    print()
    print_stack(stack)
    print()
    print_aux_stack(aux_stack)
    print()
    getMin(aux_stack)
    pop(stack,aux_stack)
    print()
    print_stack(stack)
    print()
    print_aux_stack(aux_stack)
    print()
    pop(stack,aux_stack)
    print()
    print()
    print_stack(stack)
    print()
    print_aux_stack(aux_stack)
    print()
    pop(stack,aux_stack)
    