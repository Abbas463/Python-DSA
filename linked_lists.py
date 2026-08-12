class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# # Create nodes
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# # Link them
# node1.next = node2
# node2.next = node3
# # Head points to first node
# head = node1
# print(head.data)  # 10


def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Create list: 10 -> 20 -> 30
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3

print_list(node1)  # 10 -> 20 -> 30 -> None