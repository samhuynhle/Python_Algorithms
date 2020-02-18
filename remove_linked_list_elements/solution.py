class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head
        ret = head
        
        while curr:
            current_val = curr.val
            
            # if our current nodes val isn't the target we advance our prev marker
            if current_val != val:
                prev = curr

            # if the current nodes val is and we have a valid prev marker, we point prev to our current's next
            elif current_val == val and prev:
                prev.next = curr.next      

            # In this case we are removing the very first node in our linked list, can be done multiple times
            else:
                ret = curr.next
                
            # always move current marker
            curr = curr.next
            
        return ret