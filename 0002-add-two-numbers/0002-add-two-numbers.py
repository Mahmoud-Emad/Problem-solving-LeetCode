# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        data_1 = ""
        data_2 = ""
        while (l1 != None):
            data_1 += str(l1.val)
            l1 = l1.next

        while (l2 != None):
            data_2 += str(l2.val)
            l2 = l2.next

        data_1 = int(data_1[::-1])
        data_2 = int(data_2[::-1])

        ans = str(data_1 + data_2)[::-1]

        ret = []
        for i in range(len(ans)):
            ret.append(ListNode(int(ans[i])))

        for i in range(len(ret) - 1):
            ret[i].next = ret[i+1]

        return ret[0]