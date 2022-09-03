class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head
    while head and head.next:
        b = head.next
        head.next = b.next
        b.next = head

        prev.next = b

        head = head.next
        prev = prev.next.next

    return root.next

nodes = [ListNode(num) for num in list(map(int, input().split()))]
head = nodes.pop(0)
current_node = head
for node in nodes:
    current_node.next = node
    current_node = node


result = swapPairs(head)

while result:
    print(result.val)
    result = result.next

