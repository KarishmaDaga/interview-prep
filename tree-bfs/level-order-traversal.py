'''
To process the tree level-by-level, we need to start
traverse all nodes in each level before moving onto 
the next level.

We can use a queue to keep track of the nodes to process
because as we can process the nodes in order from left
to right. 

The steps of the algorithm can be broken into the following:
1. Start by pushing the root node to the queue
2. Keep iterating until the queue is empty
3. In each iteration, we process all nodes in a level. 
Since we're growing the queue each time we process a node,
we should keep track of the original number of nodes in
the level. We can simply get the size of the queue before 
the level is processed.
4. In the loop, we remove the node we're processing and
push its value to the result. We then add its children
(if any) to the queue
5. If the queue is not empty (another level to process), 
we repeat from step 3. If not, we simply return the result.

'''
from collections import deque

class TreeNode(self, val):
    self.val = val
    self.left, self.right = None, None

def level_order(root):
    result = []
    if root is None: # ask what to return in this case, could be error msg or []
        return result
    
    # init
    queue = deque()
    queue.append(root)

    while queue:
        # keep track of size of current level
        level_size = len(queue)
        curr_level = [] # for result

        for i in range(level_size):
            # pop beginning of queue
            curr_node = queue.popleft()
            # add current node to the result
            curr_level.append(curr_node.val)
            # add children to queue
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(curr_level)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(level_order(root)))

main()