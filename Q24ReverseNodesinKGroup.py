import time

T1 = ([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)


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


def solution(head, k):
    head = buildList(head)
    if head is None:
        return head
    if k == 1:
        return head
    tmpList, cnt, cur = [head], 1, head
    while cnt < k:
        cur = cur.next
        if cur:
            tmpList.append(cur)
            cnt += 1
        else:
            return head
    head = cur
    preEnd = None
    while True:
        if len(tmpList) < k:
            break
        if preEnd:
            preEnd.next = tmpList[-1]
        nextStart = tmpList[-1].next
        for i in range(len(tmpList)-1, 0, -1):
            tmpList[i].next = tmpList[i-1]
        tmpList[0].next = nextStart
        preEnd = tmpList[0]
        tmpList, cur, cnt = [nextStart], nextStart, 1
        if cur is None:
            break
        while cnt < k:
            cur = cur.next
            if cur:
                tmpList.append(cur)
                cnt += 1
            else:
                break
    return head


if __name__ == '__main__':
    t1 = time.time()
    head = solution(*T1)
    print(showList(head))
    print(time.time()-t1)
