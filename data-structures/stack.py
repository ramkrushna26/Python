

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        item = self.elements[-1]
        del self.elements[-1]
        return item

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return len(self.elements) == 0

    def top(self):
        return self.elements[-1]

    def get_stack(self):
        return self.elements

if __name__ == "__main__":
    action_flag = 1
    stack = Stack()
    
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
            stack.push(item)
            print("Current Stack: ", stack.get_stack())
        elif action == 2:
            if stack.is_empty():
                print("Error: Stack is Empty.")
            else:
                print("Popped Item: ", stack.pop())
                print("Stack after Pop: ", stack.get_stack())
        elif action == 3:
            print("Size of Stack: ", stack.size())
        elif action == 4:
            print("Stack empty check: ", stack.is_empty())
        elif action == 5:
            print("Top item in Stack: ", stack.top())
        else:
            print("Invalid Input. Try Again!")


            
