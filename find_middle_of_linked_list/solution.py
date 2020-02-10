from listnode import ListNode

class Solution:
    def middleNode(self, head):
        if head == None:
            return head

        slow, fast = head

        while fast != None or fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow