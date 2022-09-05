class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenListNode(head: ListNode) -> ListNode:
    p = head
    even_start_node = even_point = ListNode(None)
    odd_start_node = odd_point = ListNode(None)

    while p:
        p_next = p.next
        if p.val % 2 == 0:
            even_point.next = p
            even_point = p
        else:
            odd_point.next = p
            odd_point = p
        p.next = None
        p = p_next

    odd_point.next = even_start_node.next

    return odd_start_node.next


nodes = [ListNode(num) for num in list(map(int, input().split()))]
head = nodes.pop(0)
current_node = head
for node in nodes:
    current_node.next = node
    current_node = node

result = oddEvenListNode(head)

while result:
    print(result.val, end='->')
    result = result.next
