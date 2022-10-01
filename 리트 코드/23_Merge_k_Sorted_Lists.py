import heapq


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

case = list()
for i in range(3):
    nodes = [ListNode(i) for i in list(map(int, input().split()))]
    head = nodes.pop(0)
    current_node = head
    for node in nodes:
        current_node.next = node
        current_node = node
    case.append(head)

# for node in case:
#     while node:
#         print(node.val, end='')
#         node = node.next
#     print('')

## 시작
root = result = ListNode(None)
heap = []
for i in range(len(case)):
    if case[i]:
        heapq.heappush(heap, (case[i].val, i, case[i]))

while heap:
    node = heapq.heappop(heap)
    idx = node[1]
    result.next = node[2]

    result = result.next
    if result.next:
        heapq.heappush(heap, (result.next.val, idx, result.next))

while root.next:
    print(root.next.val, end='')
    root.next = root.next.next
