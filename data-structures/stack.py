

stack = []

def push(item):
    stack.append(item)

def pop():
    item = stack[-1]
    del stack[-1]
    return item

def size():
    return len(stack)

def is_empty():
    return len(stack) == 0

def top():
    return stack[-1]


if __name__ == "__main__":
    action_flag = 1
    while(1):
        try:
            if action_flag == 1:
                action = int(input("1 For Push \n2 For Pop \n3 For Size \n4 For Empty \n5 For Top Element\nChoose Stack Action: "))
            else:
                action = int(input("Choose Stack Action: "))
        except ValueError:
            print("Invalid Input. Try Again!")
            continue
        
        action_flag = 0
        
        if action == 1:
            item = input("Enter item to Push: ")
            push(item)
            print("Current Stack: ", stack)
        elif action == 2:
            if is_empty():
                print("Error: Stack is Empty.")
            else:
                print("Stack after Pop: ", stack)
                print("Popped Item: ", pop())
        elif action == 3:
            print("Size of Stack: ", size())
        elif action == 4:
            print("Stack empty check: ", is_empty())
        elif action == 5:
            print("Top item in Stack: ", top())
        else:
            print("Invalid Input. Try Again!")


            
        
