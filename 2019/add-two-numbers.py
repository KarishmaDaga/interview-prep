https://leetcode.com/problems/add-two-numbers/

  
class Solution(object):
    def addTwoNumbers(self, l1, l2):
    head = ListNode(0);
    p = l1, q = l2, curr = head;
    int carry = 0;
    while p != None or q != None:
        if p == None:
          return 0
        else: 
          x = p.val
        if q == None:
          return 0
        else:
          y = q.val
          
        sum = carry + x + y
        carry = sum / 10;
        curr.next = ListNode(sum % 10);
        curr = curr.next;
        
        if (p != null):
          p = p.next;
        if (q != null):
          q = q.next;
          
        if (carry > 0):
            curr.next = ListNode(carry);
            
    return head.next;
