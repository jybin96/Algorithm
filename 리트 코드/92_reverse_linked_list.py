class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reversLinkedList(head: ListNode, m: int, n: int) -> ListNode:
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head
    for _ in range(m-1):
        start = start.next
    end = start.next

    for _ in range(n-m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next


nodes = [ListNode(num) for num in list(map(int, input().split()))]
m = int(input())
n = int(input())

head = nodes.pop(0)
current_node = head
for node in nodes:
    current_node.next = node
    current_node = node

result = reversLinkedList(head, m, n)
while result:
    print(result.val, end='->')
    result = result.next