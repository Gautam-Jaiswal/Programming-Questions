class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

def oddeven(head):
    if head==None or head.next==None or head.next.next==None:
        return head
    even = head.next
    odd = head
    temp = head.next
    while even.next and even:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = temp
    
    return head

if __name__ == '__main__':
    
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(18)
    
    head = oddeven(head)
    
    temp = head
    while temp:
        print(temp.data ,end = "-->")
        temp=temp.next
    print("None")