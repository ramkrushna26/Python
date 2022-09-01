



stack = []
stack_dup = []

def push(item):
    stack.append(item)

def pop():
    item = stack_dup[-1]
    del stack_dup[-1]
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
                action = int(input("1 For Enqueue \n2 For Dequeue \n3 For Size \n4 For Empty \n5 For Top Element\nChoose Queue Action: "))
            else:
                action = int(input("Choose Queue Action: "))
        except ValueError:
            print("Invalid Input. Try Again!")
            continue
        
        action_flag = 0
        
        if action == 1:
            item = input("Enter item to Enqueue: ")
            push(item)
            print("Current Queue: ", stack)
        elif action == 2:
            if is_empty():
                print("Error: Queue is Empty.")
            else:
                stack_dup = []
                for idn in range(len(stack)):
                    stack_dup.insert(0,stack[idn])
                print("Dequeue Item: ", pop())
                stack = []
                for idn in range(len(stack_dup)):
                    stack.insert(0,stack_dup[idn])
                print("Queue after Dequeue: ", stack)
        elif action == 3:
            print("Size of Stack: ", size())
        elif action == 4:
            print("Queue empty check: ", is_empty())
        elif action == 5:
            print("Front item in Queue: ", top())
        else:
            print("Invalid Input. Try Again!")

