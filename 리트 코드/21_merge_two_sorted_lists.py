class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def connectedSortedLists(head1: ListNode, head2: ListNode) -> ListNode:
    new_head1 = head1
    new_head2 = head2
    connected_head = None
    node_list = []
    current_node = None

    while new_head1 is not None:
        if new_head1.val == new_head2.val:
            node_list.append(ListNode(new_head1.val))
            node_list.append(ListNode(new_head2.val))
            new_head1 = new_head1.next
            new_head2 = new_head2.next
        elif new_head1.val > new_head2.val:
            node_list.append(ListNode(new_head2.val))
            new_head2 = new_head2.next
        else:
            node_list.append(ListNode(new_head1.val))
            new_head1 = new_head1.next

    for i, node in enumerate(node_list):
        if i == 0:
            connected_head = node
            current_node = connected_head
            continue
        current_node.next = node
        current_node = node

    return connected_head


# 입렵값을 받아 연결 리스트로 변환해주는 부분 -> 입력 부분이 연결리스트로 주어 주기떄문에 이렇게 하였습니다.
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums1.sort()
nums2.sort()

head1 = None
head2 = None
nodes1 = []
nodes2 = []
current_node1 = None
current_node2 = None

for num1, num2 in zip(nums1, nums2):
    new_node1 = ListNode(num1)
    new_node2 = ListNode(num2)
    nodes1.append(new_node1)
    nodes2.append(new_node2)

for i, (node1, node2) in enumerate(zip(nodes1, nodes2)):
    if i == 0:
        head1 = node1
        current_node1 = head1
        head2 = node2
        current_node2 = head2
        continue

    current_node1.next = node1
    current_node1 = node1

    current_node2.next = node2
    current_node2 = node2

connected_node = connectedSortedLists(head1, head2)

while connected_node is not None:
    if connected_node.next is None:
        print(connected_node.val, end='')
    else:
        print(connected_node.val, end='->')
    connected_node = connected_node.next

########
