# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        # creating a new empty list
        result = []
        # Create a pointer to iterate through linked list1
        node1 = list1
        # Create a loop to take val from linked list1 and put them into result
        while node1:
            result.append(node1.val)
            node1 = node1.next
        # Create a pointer to iterate through linked list2
        node2 = list2
        # Create a loop to take val from linked list2 and put them into result
        while node2:
            result.append(node2.val)
            node2 = node2.next
        # Sort result
        result = sorted(result)
        # Create a dummy linked list
        dummy = ListNode(0)
        # Create a dummy node as entry point
        node = dummy
        # Create a loop to iterate through result list and put values into dummy linked list
        for i in range(len(result)):
            node.next = ListNode(result[i])
            # Moving pointer forward
            node = node.next
        # Return the result
        return dummy.next
    
# Create a linked list from input string

print("Type first string of unsorted numbers")
input_list1 = input('> ').split()

print("Type second string of unsorted numbers")
input_list2 = input('> ').split()
    
dummy1 = ListNode(0)
node1 = dummy1

for i in range(len(input_list1)):
    node1.next = ListNode(int(input_list1[i]))
    node1 = node1.next
list1 = dummy1.next

dummy2 = ListNode(0)
node2 = dummy2

for i in range(len(input_list2)):
    node2.next = ListNode(int(input_list2[i]))
    node2 = node2.next
list2 = dummy2.next

solution = Solution()
result = solution.mergeTwoLists(list1, list2)

node = result

while node:
    print(node.val)
    node = node.next