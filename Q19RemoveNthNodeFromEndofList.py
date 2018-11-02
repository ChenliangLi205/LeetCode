class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        cnt2node = dict()
        current, cnt = head, 0
        while current:
            cnt2node[cnt] = current
            cnt += 1
            current = current.next
        cnt -= 1
        if cnt == 0:
            return None
        toRemove = cnt-n+1
        pre, nex = toRemove-1, toRemove+1
        if pre<0:
            head = cnt2node[nex]
            return head
        if nex>cnt:
            cnt2node[pre].next = None
            return head
        cnt2node[pre].next = cnt2node[nex]
        return head