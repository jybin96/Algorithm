class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def isPalindrome(node_head: ListNode) -> bool:
    q = []

    if not node_head:
        return True

    init_node = node_head
    # 리스트 변환
    while init_node is not None:
        q.append(init_node.val)
        init_node = init_node.next

    # 펠린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


# 입렵값을 받아 연결 리스트로 변환해주는 부분 -> 입력 부분이 연결리스트로 주어 주기떄문에 이렇게 하였습니다.
nums = list(map(int, input().split()))
head = None
nodes = []
current_node = None
for num in nums:
    new_node = ListNode(num)
    nodes.append(new_node)

for i, node in enumerate(nodes):
    if i == 0:
        head = node
        current_node = head
        continue
    current_node.next = node
    current_node = node
########

print(isPalindrome(head))
