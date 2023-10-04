class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def intersection_node(head_a, head_b):
    # create a set for storing all nodes of the first linked list 
    nodes = set()
    # traverse the first linked list wih a loop and put each node in the set 
    while head_a:
        nodes.add(head_a)
        head_a= head_a.next
    # then loop through second linked list and check if each node is in the set
    while head_b:
        if head_b in nodes: 
            return head_b
        head_b= head_b.next

    # if node is in the set, then return that node
    # if there is no intersection, return NONE
    return None 
