class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


nums = list(map(int, input().split()))
nodes = [ListNode(num) for num in nums]
head = nodes.pop(0)
current_node = head

for node in nodes:
    current_node.next = node
    current_node = node

prev = reverseList(head)

while prev:
    print(prev.val, end='->')
    prev = prev.next
print('NULL')