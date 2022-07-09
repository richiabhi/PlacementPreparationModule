class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        loop_flag = False
        if not (slow and slow.next and slow.next.next):
            return None
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                loop_flag = True
                break
        if loop_flag:
            if (slow == head):
                return head
            else:
                slow = head
                while (slow.next != fast.next):
                    slow = slow.next
                    fast = fast.next
                return fast.next
        else:
            return None
