from typing import Optional
from leetcode_solutions.nodes.nodes import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Assumptions: 
        1. that ALL nodes to the right must be greater than and ALL nodes to the left must be less than
        2. Child nodes on either side can NOT be equal to parent node
        We will need to keep track of range
        A BST is valid if...
        1. The root node is in Range(i -> j) 
        2. The left child BST is in range (i -> root)
        3. the right child BST is in range (root -> j)
        NOTE: if i or j is none there is no bound on that end so don't need to check
        """
        def isBSTInRange(root: Optional[TreeNode], i: Optional[int], j: Optional[int]) -> bool:
            # print(f"isBSTInRange({root.val if root else "None"}, {i}, {j})")
            # BASE CASE 1: val of root is not in current range -> return False
            val = root.val
            if (i is not None and val <= i) or (j is not None and val >= j):
                # print(f"{val} <= {i} OR {val} >= {j} -> NOT VALID")
                return False
            # BASE CASE 2: Bottom of tree -> return True
            if not root or (not root.left and not root.right):
                # print(f"Bottom of tree -> VALID")
                return True
            if root.left:
                left_is_valid = isBSTInRange(root.left, i, val)
                if not left_is_valid:
                    # print(f"left at {root.val} -> NOT VALID")
                    return False
            if root.right:
                right_is_valid = isBSTInRange(root.right, val, j)
                if not right_is_valid:
                    # print(f"right at {root.val} -> NOT VALID")
                    return False
            # print(f"left & right at {root.val} VALID")
            return True

        return isBSTInRange(root, None, None)

            

        