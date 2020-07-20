'''
Problem
Given a binary tree, populate an array 
to represent its level-by-level traversal
in reverse order, i.e., the lowest level
comes first. You should populate the 
values of all nodes in each level from left
to right in separate sub-arrays.

Idea
You could do a simple level order traversal
and reverse the array before returning it or 
append the current level to the beginning of
the list using a deque structure for result.

Other options include:
- result.insert(0, curr_level) which mutates the existing
result object
- other (much slower) option is curr_level + result 
which is slower because '+' creates a new object

Complexity
- Time: O(n) where n is the number of nodes in the tree
- Space: O(n) as the result deque contains all nodes in
the tree and O(m) for the queue object where m is the max
number of nodes in a level in the tree
'''
from collections import deque
class TreeNode(self, val):
    self.val = val
    self.left, self.right = None, None

def reverse_traverse(root):
    result = deque()
    if root is None:
        return result
    
    # init
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        curr_level = []

        for i in range(level_size):
            # pop from queue
            curr_node = queue.popleft()
            # add to current level
            curr_level.append(curr_node.val)
            # add children to queue
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.appendleft(curr_level)
    return result