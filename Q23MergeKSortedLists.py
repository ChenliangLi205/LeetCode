import time

T1 = [[1,4,5],[1,3,4],[2,6]]


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def buildList(l):
    head = ListNode(l[0])
    current = head
    for val in l[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def showList(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals


def solution(lists):
    lists = [buildList(l) for l in lists]
    if len(lists) == 0:
        return
    if len(lists) == 1:
        return lists[0]
    if not any(lists):
        return []
    currents = lists
    length = len(lists)
    notNone = set()
    for i in range(length):
        if currents[i]:
            notNone.add(i)
    minNode, minVal = -1, None
    for i in notNone:
        if minNode < 0:
            minNode = i
            minVal = currents[i].val
            continue
        if currents[i].val < minVal:
            minNode = i
            minVal = currents[i].val
    head = currents[minNode]
    currents[minNode] = currents[minNode].next
    if currents[minNode] is None:
        notNone.remove(minNode)
    current = head
    while True:
        if len(notNone) == 0:
            break
        minNode, minVal = -1, None
        for i in notNone:
            if minNode < 0:
                minNode = i
                minVal = currents[i].val
                continue
            if currents[i].val < minVal:
                minNode = i
                minVal = currents[i].val
        current.next = currents[minNode]
        currents[minNode] = currents[minNode].next
        if currents[minNode] is None:
            notNone.remove(minNode)
        current = current.next
    return head


if __name__ == '__main__':
    t1 = time.time()
    head = solution(T1)
    print(showList(head))
    print(time.time()-t1)
