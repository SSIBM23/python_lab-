stack=[]
size=3
def display():
    print("stack elements are")
    for item in stack:
         print(item)
def push(item):
    print(f"push on item to stack:{item}")
    if len (stack)<size:
        stack.append(item)
    else:
        print("stack is full")
def popitem():
    if len(stack)>0:
         print(f"pop an item from stack:{stack.pop()}")
    else:
        print("stack is empty")
push(10)
push(20)
push(30)
display()
push(40)
popitem()
display()
popitem()
popitem()
popitem()