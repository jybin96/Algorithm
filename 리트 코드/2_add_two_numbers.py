class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumNode(head1: ListNode, head2: ListNode) -> ListNode:
    str_num1 = ''
    str_num2 = ''
    while head1:
        str_num1 += str(head1.val)
        head1 = head1.next
    while head2:
        str_num2 += str(head2.val)
        head2 = head2.next

    result = int(str_num1[::-1]) + int(str_num2[::-1])
    parse_nodes = [ListNode(int(num)) for num in list(str(result)[::-1])]
    new_head = parse_nodes.pop(0)
    current_node = new_head

    for node in parse_nodes:
        current_node.next = node
        current_node = node

    return new_head

# 입력값 위해 init
nodes1 = [ListNode(num1) for num1 in list(map(int, input().split()))]
nodes2 = [ListNode(num2) for num2 in list(map(int, input().split()))]

head1, head2 = nodes1.pop(0), nodes2.pop(0)
current_node1, current_node2 = head1, head2

for node1 in nodes1:
    current_node1.next = node1
    current_node1 = node1

for node2 in nodes2:
    current_node2.next = node2
    current_node2 = node2

############

new_head = addTwoNumNode(head1, head2)
while new_head:
    print(new_head.val, end='->')
    new_head = new_head.next

