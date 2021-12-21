class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val = val

def print_tree(root):
    if root == None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

def insert(root,key):
    if root==None:
        root = Node(key)
        return root
    
    q=[]
    q.append(root)
    
    while len(q)>0:
        
        temp= q[0]
        q.pop(0)
        
        if temp.left == None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        
        if temp.right == None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)
    
    return root

def delete_last_node(root,delete_node):
    q=[]
    q.append(root)
    while len(q)>0:
        temp = q.pop(0)
        if temp is delete_node:
            temp = None
            return
        if temp.right:
            if temp.right is delete_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is delete_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

def delete(root , key):
    if root == None:
        return
    if root.val == key:
        return root
    
    temp = None
    key_node = None
    q = []
    q.append(root)
    while len(q)>0:
        temp = q.pop(0)
        if temp.val == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    #the node to be deleted is the middle or some node but not leaf node
    if key_node:
        st = temp.val
        delete_last_node(root,temp)
        key_node.val = st
    #if the node to be deleted is the leaf node    
    if key_node == temp:
        delete_last_node(root,temp)
    return root
    
def level_order_traversal(root):
    if root == None:
        return
    q=[]
    q.append(root)
    
    while len(q)>0:
        
        temp = q.pop(0)
        print(temp.val)
        
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)


if __name__ == '__main__':
    
    root = Node(1)
    root.left=Node(2)
    root.right = Node(3)
    root.left.left= Node(4)
    root.left.right= Node(5)
    
    #Insertion
    root = insert(root,6)
    root = insert(root,7)
    
    #Deletion
    #root = delete(root,7)
    
    #level_order_traversal
    #level_order_traversal(root)
    
    #Printing
    #print_tree(root)
