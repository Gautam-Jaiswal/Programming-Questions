#Merge Sort in Linked list

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

def merge_sort(head):
    
    if head == None or head.next == None:
        return head
    
    temp = None
    slow = fast = head
    
    while  fast and fast.next:
        temp = slow
        slow=slow.next
        fast = fast.next.next
    
    temp.next = None
    
    left_list = merge_sort(head)
    right_list = merge_sort(slow)
    
    return merge(left_list , right_list)

def merge(left_list , right_list):
    
    temp = Node(-1)
    curr = temp
    
    while left_list != None and right_list != None:
        if left_list.data <= right_list.data:
            curr.next = left_list
            left_list = left_list.next
            curr = curr.next
        else:
            curr.next = right_list
            right_list = right_list.next
            curr = curr.next
    
    while left_list != None:
        curr.next = left_list
        left_list = left_list.next
        curr = curr.next    
    while right_list != None:
        curr.next = right_list
        right_list = right_list.next
        curr = curr.next        
    
    return temp.next
    
if __name__ == '__main__':
    
    head = Node(5)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    
    head = merge_sort(head)
    
    temp = head
    while temp:
        print(temp.data ,end = "-->")
        temp=temp.next
    print("None")
    
    
    
