

queue = []

def enqueue(item):
    queue.append(item)

def dequeue():
    item = queue.pop(0)
    return item

def size():
    return len(queue)

def is_empty():
    return len(queue) == 0

def front():
    return queue[-1]


if __name__ == "__main__":
    action_flag = 1
    while(1):
        try:
            if action_flag == 1:
                action = int(input("1 For Enqueue \n2 For Dequeue \n3 For Size \n4 For Empty \n5 For Front Element\nChoose Queue Action: "))
            else:
                action = int(input("Choose Queue Action: "))
        except ValueError:
            print("Invalid Input. Try Again!")
            continue
        
        action_flag = 0
        
        if action == 1:
            item = input("Enter item to Enqueue: ")
            enqueue(item)
            print("Current Queue: ", queue)
        elif action == 2:
            if is_empty():
                print("Error: Queue is Empty.")
            else:
                print("Queue after Dequeue: ", queue)
                print("Dequeue Item: ", dequeue())
        elif action == 3:
            print("Size of Queue: ", size())
        elif action == 4:
            print("Queue empty check: ", is_empty())
        elif action == 5:
            print("Front item in Queue: ", front())
        else:
            print("Invalid Input. Try Again!")


