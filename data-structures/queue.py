

class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self,item):
        self.elements.append(item)

    def dequeue(self):
        item = self.elements.pop(0)
        return item

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def front(self):
        return self.elements[-1]

    def get_queue(self):
        return self.elements

if __name__ == "__main__":
    action_flag = 1
    queue = Queue()
    
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
            if item:
                queue.enqueue(item)
                print("Current Queue: ", queue.get_queue())
        elif action == 2:
            if queue.is_empty():
                print("Error: Queue is Empty.")
            else:
                print("Dequeue Item: ", queue.dequeue())
                print("Queue after Dequeue: ", queue.get_queue())
        elif action == 3:
            print("Size of Queue: ", queue.size())
        elif action == 4:
            print("Queue empty check: ", queue.is_empty())
        elif action == 5:
            print("Front item in Queue: ", queue.front())
        else:
            print("Invalid Input. Try Again!")

