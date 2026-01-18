  LeetCode Submissions  body { font-family: Arial, sans-serif; background-color: #f0f0f0; color: #333; padding: 20px; print-color-adjust: exact; } .header { background-color: #f8f9fa; padding: 20px; text-align: center; margin-bottom: 20px; height: } .header h1 { color: #007bff; margin: 0; } .header-buttons { margin-top: 10px; } .button { background-color: #007bff; color: #fff; border: none; padding: 10px 20px; font-size: 16px; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; margin-right: 10px; transition: background-color 0.3s ease; } .button:hover { background-color: #0056b3; } .question { margin-bottom: 40px; border: 1px solid #ccc; padding: 20px; background-color: #fff; } .title { font-size: 24px; font-weight: bold; margin-bottom: 10px; color: #333; } .language { font-style: italic; color: #666; margin-bottom: 10px; } .description { margin-bottom: 20px; } .solution { margin-top: 20px; } .solution-status { color: green; font-weight: bold; margin-bottom: 10px; } pre { padding: 2rem; border: 1px grey solid; padding: 10px; border-radius: 4px; overflow-x: auto; } .keyword{ color: #0e77ae; } .comment{ color: green; } .flipX video::-webkit-media-text-track-display { transform: matrix(-1, 0, 0, 1, 0, 0) !important; } .flipXY video::-webkit-media-text-track-display { transform: matrix(-1, 0, 0, -1, 0, 0) !important; } .flipXYX video::-webkit-media-text-track-display { transform: matrix(1, 0, 0, -1, 0, 0) !important; } @keyframes blinkWarning { 0% { color: red; } 100% { color: white; } } @-webkit-keyframes blinkWarning { 0% { color: red; } 100% { color: white; } } .blinkWarning { -webkit-animation: blinkWarning 1s linear infinite; -moz-animation: blinkWarning 1s linear infinite; animation: blinkWarning 1s linear infinite; }

My LeetCode Submissions
=======================

[**1 Two Sum** (link)](https://leetcode.com/problems/two-sum/description)

Description
-----------

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

**Example 1:**

**Input:** nums = \[2,7,11,15\], target = 9
**Output:** \[0,1\]
**Explanation:** Because nums\[0\] + nums\[1\] == 9, we return \[0, 1\].

**Example 2:**

**Input:** nums = \[3,2,4\], target = 6
**Output:** \[1,2\]

**Example 3:**

**Input:** nums = \[3,3\], target = 6
**Output:** \[0,1\]

**Constraints:**

*   `2 <= nums.length <= 104`
*   `-109 <= nums[i] <= 109`
*   `-109 <= target <= 109`
*   **Only one valid answer exists.**

**Follow-up:** Can you come up with an algorithm that is less than `O(n2)` time complexity?

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            nums2 = sorted(nums)
    
            def get_ab(nums2):
                w = len(nums2)
                for i, a in enumerate(nums2):
                    for j in range(i+1, w):
                        b = nums2[j]
                        if a + b == target:
                            return a, b
    
            
    
            a, b = get_ab(nums2)
            result = []
            for index, i in enumerate(nums):
                if i in [a, b]:
                    result.append(index)
    
            return result
    
    

[**2 Add Two Numbers** (link)](https://leetcode.com/problems/add-two-numbers/description)

Description
-----------

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg)

**Input:** l1 = \[2,4,3\], l2 = \[5,6,4\]
**Output:** \[7,0,8\]
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = \[0\], l2 = \[0\]
**Output:** \[0\]

**Example 3:**

**Input:** l1 = \[9,9,9,9,9,9,9\], l2 = \[9,9,9,9\]
**Output:** \[8,9,9,9,0,0,0,1\]

**Constraints:**

*   The number of nodes in each linked list is in the range `[1, 100]`.
*   `0 <= Node.val <= 9`
*   It is guaranteed that the list represents a number that does not have leading zeros.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    
    
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    
    class Solution:
        # Definition for singly-linked list.
        def list_to_linked_list(self, arr):
            if not arr:
                return None
    
            head = ListNode(arr[0])
            current = head
    
            for value in arr[1:]:
                current.next = ListNode(value)
                current = current.next
    
            return head
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            x = 0
    
            curr = l1.val
            lx = []
            while True:
                lx.append(l1.val)
                l1 = l1.next
                if not l1:
                    break
        
                
    
            ly = []
            while True:
                ly.append(l2.val)
                l2 = l2.next
                if not l2:
                    break
    
            lxr = lx[::-1]
            lyr = ly[::-1]
    
            lxr = int("".join([str(a) for a in lxr]))
            lyr = int("".join([str(y) for y in lyr]))
    
            sumxy = lxr + lyr
    
            f =[]
    
            while(sumxy):
                f.append(sumxy%10)
                sumxy = sumxy//10
    
            print(f)
    
    
        
    
            if not f:
                return ListNode(val=0)
    
            fr = ListNode(val=f[0])
    
            curr = fr
    
            for x in f[1:]:
                curr.next = ListNode(val=x)
                # curr.val = x
                curr = curr.next
    
            return fr
    
    
    
    
    
            
    

[**21 Merge Two Sorted Lists** (link)](https://leetcode.com/problems/merge-two-sorted-lists/description)

Description
-----------

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** list1 = \[1,2,4\], list2 = \[1,3,4\]
**Output:** \[1,1,2,3,4,4\]

**Example 2:**

**Input:** list1 = \[\], list2 = \[\]
**Output:** \[\]

**Example 3:**

**Input:** list1 = \[\], list2 = \[0\]
**Output:** \[0\]

**Constraints:**

*   The number of nodes in both lists is in the range `[0, 50]`.
*   `-100 <= Node.val <= 100`
*   Both `list1` and `list2` are sorted in **non-decreasing** order.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            ret = ListNode()
            curr = ret
            while True:
                if list1 == None:
                    curr.next = list2
                    break
                elif list2 == None:
                    curr.next = list1
                    break
                else:
                    h1 = list1.val
                    h2 = list2.val
                    # print(h1, h2)
                    if h1 < h2:
                        curr.next = ListNode(h1)
                        list1 = list1.next
                    else:
                        curr.next = ListNode(h2)
                        list2 = list2.next
                    curr = curr.next
                    # print(curr.val)
                # curr.next = ListNode()
                
    
            return ret.next
     
    
            
    

[**26 Remove Duplicates from Sorted Array** (link)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description)

Description
-----------

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of _unique elements_ in `nums` to be `k**​​​​​​​**`​​​​​​​. After removing duplicates, return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

The judge will test your solution with the following code:

int\[\] nums = \[...\]; // Input array
int\[\] expectedNums = \[...\]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums\[i\] == expectedNums\[i\];
}

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

**Input:** nums = \[1,1,2\]
**Output:** 2, nums = \[1,2,\_\]
**Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Example 2:**

**Input:** nums = \[0,0,1,1,1,2,2,3,3,4\]
**Output:** 5, nums = \[0,1,2,3,4,\_,\_,\_,\_,\_\]
**Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

**Constraints:**

*   `1 <= nums.length <= 3 * 104`
*   `-100 <= nums[i] <= 100`
*   `nums` is sorted in **non-decreasing** order.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
    
            start_index  = 0
            start_value = None
            for (index, value) in enumerate(nums):
                if value != start_value:
                    nums[start_index] = value
                    start_value = value
                    start_index+=1
    
            return start_index
    
    
            
    

[**747 Min Cost Climbing Stairs** (link)](https://leetcode.com/problems/min-cost-climbing-stairs/description)

Description
-----------

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return _the minimum cost to reach the top of the floor_.

**Example 1:**

**Input:** cost = \[10,15,20\]
**Output:** 15
**Explanation:** You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

**Example 2:**

**Input:** cost = \[1,100,1,1,1,100,1,1,100,1\]
**Output:** 6
**Explanation:** You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

**Constraints:**

*   `2 <= cost.length <= 1000`
*   `0 <= cost[i] <= 999`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # class Solution:
    #     def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    
    #         @lru_cache(None)
    #         def total_cost(i):
    
    #             if i-2 < 0:
    #                 return 0
    #             else:
    #                 return min(
    #                 total_cost(i-1)+cost[i-1],
    #                 total_cost(i-2) + cost[i-2]
    #                 )
    
    #         total_len = len(cost)
    
    #         return total_cost(total_len)
    
    
    class Solution:
        def minCostClimbingStairs(self, cost: List[int]) -> int:
            prev2 = prev1 = 0
    
            for i in range(2, len(cost) + 1):
                curr = min(
                    prev1 + cost[i - 1],
                    prev2 + cost[i - 2]
                )
                prev2, prev1 = prev1, curr
    
            return prev1
    
    

[**64 Minimum Path Sum** (link)](https://leetcode.com/problems/minimum-path-sum/description)

Description
-----------

Given a `m x n` `grid` filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg)

**Input:** grid = \[\[1,3,1\],\[1,5,1\],\[4,2,1\]\]
**Output:** 7
**Explanation:** Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

**Example 2:**

**Input:** grid = \[\[1,2,3\],\[4,5,6\]\]
**Output:** 12

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 200`
*   `0 <= grid[i][j] <= 200`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # class Solution:
    #     def minPathSum(self, grid: List[List[int]]) -> int:
    
    #         leny = len(grid)
    #         lenx = len(grid[0])
                    
    #         @lru_cache(None)
    #         def total_cost(i, j):
    #             if i== 0 and j == 0:
    #                 return 0
    #             elif i == 0:
    #                 return total_cost(i, j-1) + grid[j-1][i]
    #             elif j == 0:
    #                 return total_cost(i-1, j) + grid[j][i-1]
    #             else:
    #                 return min(
    #                     total_cost(i-1, j) + grid[j][i-1],
    #                     total_cost(i, j-1) + grid[j-1][i]
    #                 )
    
    #         return total_cost(lenx-1, leny-1) + grid[leny-1][lenx-1]
    class Solution:
        def minPathSum(self, grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
    
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = grid[0][0]
    
            for i in range(1, m):
                dp[i][0] = dp[i-1][0] + grid[i][0]
    
            for j in range(1, n):
                dp[0][j] = dp[0][j-1] + grid[0][j]
    
            for i in range(1, m):
                for j in range(1, n):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
            return dp[m-1][n-1]
    
    

[**2470 Removing Stars From a String** (link)](https://leetcode.com/problems/removing-stars-from-a-string/description)

Description
-----------

You are given a string `s`, which contains stars `*`.

In one operation, you can:

*   Choose a star in `s`.
*   Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return _the string after **all** stars have been removed_.

**Note:**

*   The input will be generated such that the operation is always possible.
*   It can be shown that the resulting string will always be unique.

**Example 1:**

**Input:** s = "leet\*\*cod\*e"
**Output:** "lecoe"
**Explanation:** Performing the removals from left to right:
- The closest character to the 1st star is 't' in "lee**t**\*\*cod\*e". s becomes "lee\*cod\*e".
- The closest character to the 2nd star is 'e' in "le**e**\*cod\*e". s becomes "lecod\*e".
- The closest character to the 3rd star is 'd' in "leco**d**\*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

**Example 2:**

**Input:** s = "erase\*\*\*\*\*"
**Output:** ""
**Explanation:** The entire string is removed, so we return an empty string.

**Constraints:**

*   `1 <= s.length <= 105`
*   `s` consists of lowercase English letters and stars `*`.
*   The operation above can be performed on `s`.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # class Solution:
    #     def removeStars(self, s: str) -> str:
    
    #         f = ''
    #         residue = 0
    #         for x in s[::-1]:
    
    #             if x!='*':
    #                 if residue == 0:
    #                     f = f+x
    #                 else:
    #                     residue-=1
    
    #             else:
    #                 residue +=1
    
    #         return f[::-1]
                
    
                
    
            
    class Solution:
        def removeStars(self, s: str) -> str:
    
            f = []
    
            for x in s:
    
                if x == '*':
                    f.pop()
                else:
                    f.append(x)
    
            return ''.join(f)
    
            return f
                
    
                
    
            
    

[**735 Asteroid Collision** (link)](https://leetcode.com/problems/asteroid-collision/description)

Description
-----------

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Example 1:**

**Input:** asteroids = \[5,10,-5\]
**Output:** \[5,10\]
**Explanation:** The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

**Example 2:**

**Input:** asteroids = \[8,-8\]
**Output:** \[\]
**Explanation:** The 8 and -8 collide exploding each other.

**Example 3:**

**Input:** asteroids = \[10,2,-5\]
**Output:** \[10\]
**Explanation:** The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

**Example 4:**

**Input:** asteroids = \[3,5,-6,2,-1,4\]​​​​​​​
**Output:** \[-6,2,4\]
**Explanation:** The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

**Constraints:**

*   `2 <= asteroids.length <= 104`
*   `-1000 <= asteroids[i] <= 1000`
*   `asteroids[i] != 0`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            break_loop = False
            current = asteroids
            while not break_loop:
                break_loop = True
                f = [current[0]]
    
                for x in current[1:]:
    
                    if x > 0:
                        f.append(x)
                    else:
                        if not f:
                            f.append(x)
                        elif abs(x) == f[-1] :
                            f.pop()
                        elif abs(x) > f[-1] and f[-1]> 0:
                            break_loop = False
                            f[-1] = x
                        elif f[-1] < 0:
                            f.append(x)
                current = f
            
            return current
    
    
    
    
            
    

[**226 Invert Binary Tree** (link)](https://leetcode.com/problems/invert-binary-tree/description)

Description
-----------

Given the `root` of a binary tree, invert the tree, and return _its root_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

**Input:** root = \[4,2,7,1,3,6,9\]
**Output:** \[4,7,2,9,6,3,1\]

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

**Input:** root = \[2,1,3\]
**Output:** \[2,3,1\]

**Example 3:**

**Input:** root = \[\]
**Output:** \[\]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    
    
            def invert_node(node):
                if not node:
                    return node
                node.left, node.right = invert_node(node.right), invert_node(node.left)
                return node
    
            return invert_node(root)
            
    

[**104 Maximum Depth of Binary Tree** (link)](https://leetcode.com/problems/maximum-depth-of-binary-tree/description)

Description
-----------

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** 3

**Example 2:**

**Input:** root = \[1,null,2\]
**Output:** 2

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 104]`.
*   `-100 <= Node.val <= 100`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def maxDepth(self, root: Optional[TreeNode]) -> int:
    
            def depth(root):
                if not root:
                    return 0
    
                max_left = depth(root.left) 
    
                max_right = depth(root.right)
    
                return max(max_left, max_right) + 1
    
            return depth(root)
            
    

[**110 Balanced Binary Tree** (link)](https://leetcode.com/problems/balanced-binary-tree/description)

Description
-----------

Given a binary tree, determine if it is **height-balanced**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**Input:** root = \[1,2,2,3,3,null,null,4,4\]
**Output:** false

**Example 3:**

**Input:** root = \[\]
**Output:** true

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 5000]`.
*   `-104 <= Node.val <= 104`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
            def depth(node):
                if not node:
                    return 0
                
                return max(depth(node.left), depth(node.right))+1
    
            def isBalance(node):
                if not node:
                    return True
                    
                length_r = depth(node.right)
                length_l = depth(node.left)
    
                diff = length_r - length_l
    
                if abs(diff) <= 1:
                    balance = True
                else:
                    balance = False
    
                return balance and isBalance(node.left) and isBalance(node.right)
    
            return isBalance(root)
            
    

[**543 Diameter of Binary Tree** (link)](https://leetcode.com/problems/diameter-of-binary-tree/description)

Description
-----------

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

**Input:** root = \[1,2,3,4,5\]
**Output:** 3
**Explanation:** 3 is the length of the path \[4,2,1,3\] or \[5,2,1,3\].

**Example 2:**

**Input:** root = \[1,2\]
**Output:** 1

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-100 <= Node.val <= 100`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    
            def depth(node):
                if not node:
                    return 0
                else:
                    return max(depth(node.left), depth(node.right)) + 1
    
            def dia(root):
                if not root:
                    return 0
    
                return max( [dia(root.left), dia(root.right), depth(root.left) +depth(root.right) + 1])
    
            return dia(root)-1
    
    
            
    

[**572 Subtree of Another Tree** (link)](https://leetcode.com/problems/subtree-of-another-tree/description)

Description
-----------

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg)

**Input:** root = \[3,4,5,1,2\], subRoot = \[4,1,2\]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg)

**Input:** root = \[3,4,5,1,2,null,null,null,null,0\], subRoot = \[4,1,2\]
**Output:** false

**Constraints:**

*   The number of nodes in the `root` tree is in the range `[1, 2000]`.
*   The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
*   `-104 <= root.val <= 104`
*   `-104 <= subRoot.val <= 104`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # # Definition for a binary tree node.
    # # class TreeNode:
    # #     def __init__(self, val=0, left=None, right=None):
    # #         self.val = val
    # #         self.left = left
    # #         self.right = right
    # class Solution:
    #     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
    #         # a = True
    #         def leaf_same(root, subRoot):
    #             a = True
    #             if subRoot == None and root== None:
    #                 return False
    #             elif (subRoot!=None and root ==None) or (subRoot==None and root !=None):
    #                 return True
    #             # elif subRoot == None:
    #             #     return True
    #             # elif root == None:
    #             #     return True
    #             elif subRoot.val == root.val:
    #                 print(3, subRoot.val , root.val)
    #                 return leaf_same(root.left, subRoot.left) and leaf_same(root.right, subRoot.right)
    #             else:
    #                 return leaf_same(root.left, subRoot) and leaf_same(root.right, subRoot)
    
    #         return  not leaf_same(root, subRoot)
            
    
    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    # class Solution:
    #     part = False
    #     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
            
    
    #         def isSame(a , b):
    #             if  not a and not b:
    #                 return 1
    #             elif (a and not b) or (not a and b):
    #                 return 0
    #             elif a.val != b.val:
    #                 return 0
    #             else:
    #                 return isSame(a.left, b.left) and isSame(a.right, b.right)
    
    
    #         def leaf_same(root, subRoot):
    #             if self.part:
    #                 return
    #             elif root  and isSame(root, subRoot):
    #                 self.part = True
                
    #             elif root:
    #                 leaf_same(root.left, subRoot) 
    #                 leaf_same(root.right, subRoot) 
    
    #         leaf_same(root, subRoot)
    #         return  self.part
    
    class Solution:
        def isSubtree(self, root, subRoot):
            def hash_tree(node, store):
                if not node:
                    return None
    
                left = hash_tree(node.left, store)
                right = hash_tree(node.right, store)
    
                h = (node.val, left, right)
                store.add(h)
                return h
    
            root_hashes = set()
            hash_tree(root, root_hashes)
    
            sub_hash = hash_tree(subRoot, set())
            return sub_hash in root_hashes
    
            
    

[**235 Lowest Common Ancestor of a Binary Search Tree** (link)](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description)

Description
-----------

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

**Input:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 8
**Output:** 6
**Explanation:** The LCA of nodes 2 and 8 is 6.

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

**Input:** root = \[6,2,8,0,4,7,9,null,null,3,5\], p = 2, q = 4
**Output:** 2
**Explanation:** The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

**Example 3:**

**Input:** root = \[2,1\], p = 2, q = 1
**Output:** 2

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 105]`.
*   `-109 <= Node.val <= 109`
*   All `Node.val` are **unique**.
*   `p != q`
*   `p` and `q` will exist in the BST.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            @lru_cache(None)
            def isInTree(root, node):
    
                if not root:
                    return False
                val = root.val
                if  val==node:
                    return True
                elif val > node:
                    return isInTree(root.left, node)
                else:
                    return isInTree(root.right, node)
    
            def isBothInTree(root, p, q):
                if isInTree(root, p) and isInTree(root, q):
                    return True
                else:
                    return False
    
            
    
            p1 = p.val
            q1 = q.val
            def parent_node(root, p, q):
    
                if isBothInTree(root, p, q):
                    if isBothInTree(root.right, p, q):
                        return parent_node(root.right, p, q)
                    elif isBothInTree(root.left, p, q):
                        return parent_node(root.left, p, q)
                    else:
                        return root.val
    
            x = TreeNode(parent_node(root, p1, q1))
            return x
    
    
            
    

[**70 Climbing Stairs** (link)](https://leetcode.com/problems/climbing-stairs/description)

Description
-----------

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

**Input:** n = 2
**Output:** 2
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**

**Input:** n = 3
**Output:** 3
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

**Constraints:**

*   `1 <= n <= 45`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def climbStairs(self, n: int) -> int:
    
            @lru_cache(None)
            def step(n):
                if n == 1:
                    return 1
                elif n == 2:
                    return 2
                else:
                    return step(n-2) + step(n-1)
    
            return step(n)
            
    

[**152 Maximum Product Subarray** (link)](https://leetcode.com/problems/maximum-product-subarray/description)

Description
-----------

Given an integer array `nums`, find a subarray that has the largest product, and return _the product_.

The test cases are generated so that the answer will fit in a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

**Example 1:**

**Input:** nums = \[2,3,-2,4\]
**Output:** 6
**Explanation:** \[2,3\] has the largest product 6.

**Example 2:**

**Input:** nums = \[-2,0,-1\]
**Output:** 0
**Explanation:** The result cannot be 2, because \[-2,-1\] is not a subarray.

**Constraints:**

*   `1 <= nums.length <= 2 * 104`
*   `-10 <= nums[i] <= 10`
*   The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def maxProduct(self, nums: List[int]) -> int:
    
            products = [1]*len(nums)
    
            def maxProduct(nums):
                curr = nums[0]
                currs = []
                currs.append(curr)
                for n in nums[1:]:
                    curr, prev = n*curr, curr
                    currs.append(curr)
    
                return max(currs)
            
            prods = []
            for i in range(len(nums)):
                prod = maxProduct(nums[i:])
                prods.append(prod)
    
            return max(prods)
    
            
    

[**198 House Robber** (link)](https://leetcode.com/problems/house-robber/description)

Description
-----------

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

**Example 1:**

**Input:** nums = \[1,2,3,1\]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

**Example 2:**

**Input:** nums = \[2,7,9,3,1\]
**Output:** 12
**Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

**Constraints:**

*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 400`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def rob(self, nums: List[int]) -> int:
    
            prev, curr = 0, 0
    
            for n in nums:
                prev, curr = curr, max(curr, prev+n)
            
            return curr
    
            
    

[**213 House Robber II** (link)](https://leetcode.com/problems/house-robber-ii/description)

Description
-----------

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

**Example 1:**

**Input:** nums = \[2,3,2\]
**Output:** 3
**Explanation:** You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

**Example 2:**

**Input:** nums = \[1,2,3,1\]
**Output:** 4
**Explanation:** Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

**Example 3:**

**Input:** nums = \[1,2,3\]
**Output:** 3

**Constraints:**

*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 1000`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def rob(self, nums: List[int]) -> int:
    
            if len(nums) == 1:
                return nums[0]
    
            prev, curr = 0, 0 
            for n in nums[0: -1]:
                prev, curr = curr, max(curr, prev+n)
            curr1 = curr
            prev, curr = 0, 0 
            for n in nums[1:]:
                prev, curr = curr, max(curr, prev+n)
            curr2 = curr
    
            return max(curr1, curr2)
    
    
            
    

[**322 Coin Change** (link)](https://leetcode.com/problems/coin-change/description)

Description
-----------

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

**Example 1:**

**Input:** coins = \[1,2,5\], amount = 11
**Output:** 3
**Explanation:** 11 = 5 + 5 + 1

**Example 2:**

**Input:** coins = \[2\], amount = 3
**Output:** -1

**Example 3:**

**Input:** coins = \[1\], amount = 0
**Output:** 0

**Constraints:**

*   `1 <= coins.length <= 12`
*   `1 <= coins[i] <= 231 - 1`
*   `0 <= amount <= 104`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def coinChange(self, coins: List[int], amount: int) -> int:
    
            costs = [float('inf')]*(amount+1)
    
            costs[0] = 0
    
            for i in range(1,amount+1):
                for coin in coins:
                    if i - coin >= 0:
                        costs[i] = min(costs[i], costs[i-coin]+1)
    
            return costs[amount] if costs[amount]!=float('inf') else -1
            
    

[**907 Koko Eating Bananas** (link)](https://leetcode.com/problems/koko-eating-bananas/description)

Description
-----------

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `k` _such that she can eat all the bananas within_ `h` _hours_.

**Example 1:**

**Input:** piles = \[3,6,7,11\], h = 8
**Output:** 4

**Example 2:**

**Input:** piles = \[30,11,23,4,20\], h = 5
**Output:** 30

**Example 3:**

**Input:** piles = \[30,11,23,4,20\], h = 6
**Output:** 23

**Constraints:**

*   `1 <= piles.length <= 104`
*   `piles.length <= h <= 109`
*   `1 <= piles[i] <= 109`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
            h = h-len(piles)
    
            def isValid(i):
                total_hours = 0
                for p in piles:
                    hours = (p-1)//i
                    # if not p%i:
                        # hours = hours-1
                    total_hours+= hours
                return total_hours - h
    
            # if negative eat less, if positive eat less
    
            left, right = 1, max(piles)
            while left <= right:
                curr = (left+right)//2
                if isValid(curr) <= 0:
                    right = curr-1
                else:
                    left = curr+1
            if isValid(curr) > 0:
                return curr+1
            else:
                return curr
    
    
    
    
            
    

[**62 Unique Paths** (link)](https://leetcode.com/problems/unique-paths/description)

Description
-----------

There is a robot on an `m x n` grid. The robot is initially located at the **top-left corner** (i.e., `grid[0][0]`). The robot tries to move to the **bottom-right corner** (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return _the number of possible unique paths that the robot can take to reach the bottom-right corner_.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

**Input:** m = 3, n = 7
**Output:** 28

**Example 2:**

**Input:** m = 3, n = 2
**Output:** 3
**Explanation:** From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

**Constraints:**

*   `1 <= m, n <= 100`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def uniquePaths(self, m: int, n: int) -> int:
            grid = [[0]*m for _ in range(n)]
            for ys in grid:
                ys[0] = 1
    
            grid[0] = [1]*m
    
            for y in range(1, m):
                for x in range(1,n):
                    grid[x][y] = grid[x][y-1] + grid[x-1][y]
    
            return grid[n-1][m-1]
    
    
    
    
    
            
    

[**238 Product of Array Except Self** (link)](https://leetcode.com/problems/product-of-array-except-self/description)

Description
-----------

Given an integer array `nums`, return _an array_ `answer` _such that_ `answer[i]` _is equal to the product of all the elements of_ `nums` _except_ `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

**Input:** nums = \[1,2,3,4\]
**Output:** \[24,12,8,6\]

**Example 2:**

**Input:** nums = \[-1,1,0,-3,3\]
**Output:** \[0,0,9,0,0\]

**Constraints:**

*   `2 <= nums.length <= 105`
*   `-30 <= nums[i] <= 30`
*   The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            num_zeros = 0
            for n in nums:
                if not n:
                    num_zeros+=1
    
            if num_zeros >=2:
                return [0]*len(nums)
            
            non_zero_prod = 1
            for n in nums:
                if n:
                    non_zero_prod = n*non_zero_prod
    
            if num_zeros == 1:
                return [0 if n else non_zero_prod for n in nums]
    
            else:
                return [non_zero_prod//n for n in nums]
            
    

[**792 Binary Search** (link)](https://leetcode.com/problems/binary-search/description)

Description
-----------

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

**Input:** nums = \[-1,0,3,5,9,12\], target = 9
**Output:** 4
**Explanation:** 9 exists in nums and its index is 4

**Example 2:**

**Input:** nums = \[-1,0,3,5,9,12\], target = 2
**Output:** -1
**Explanation:** 2 does not exist in nums so return -1

**Constraints:**

*   `1 <= nums.length <= 104`
*   `-104 < nums[i], target < 104`
*   All the integers in `nums` are **unique**.
*   `nums` is sorted in ascending order.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def search(self, nums: List[int], target: int) -> int:
    
            size = len(nums)
            min_ = 0
            max_ = len(nums)
            prev = -1
            while True:
                curr = n = (min_ + max_)//2
    
                if curr == prev:
                    return -1
                
                a = nums[n]
                if a == target:
                    return n
                else:
                    if a > target:
                        max_ = n
                    else:
                        min_ = n
                    
                    prev = n
    
    
    
            
    

[**695 Max Area of Island** (link)](https://leetcode.com/problems/max-area-of-island/description)

Description
-----------

You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area** of an island is the number of cells with a value `1` in the island.

Return _the maximum **area** of an island in_ `grid`. If there is no island, return `0`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

**Input:** grid = \[\[0,0,1,0,0,0,0,1,0,0,0,0,0\],\[0,0,0,0,0,0,0,1,1,1,0,0,0\],\[0,1,1,0,1,0,0,0,0,0,0,0,0\],\[0,1,0,0,1,1,0,0,1,0,1,0,0\],\[0,1,0,0,1,1,0,0,1,1,1,0,0\],\[0,0,0,0,0,0,0,0,0,0,1,0,0\],\[0,0,0,0,0,0,0,1,1,1,0,0,0\],\[0,0,0,0,0,0,0,1,1,0,0,0,0\]\]
**Output:** 6
**Explanation:** The answer is not 11, because the island must be connected 4-directionally.

**Example 2:**

**Input:** grid = \[\[0,0,0,0,0,0,0,0\]\]
**Output:** 0

**Constraints:**

*   `m == grid.length`
*   `n == grid[i].length`
*   `1 <= m, n <= 50`
*   `grid[i][j]` is either `0` or `1`.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            height = len(grid)
            width = len(grid[0])
            visited = set()
    
            def find_area(j, i):
                if j<0 or j>=height:
                    return 0
                if i < 0 or i>=width:
                    return 0
                if grid[j][i] == 0:
                    return 0
                grid[j][i] = 0 
                return 1 + find_area(j+1, i) +find_area(j-1, i)+find_area(j, i-1)+find_area(j, i+1)
    
            max_area = 0
            for j in range(0, height):
                for i in range(0, width):
                    if grid[j][i] != 0:
                        max_area = max(max_area, find_area(j, i))
    
            return max_area
    
                        
            
    

[**133 Clone Graph** (link)](https://leetcode.com/problems/clone-graph/description)

Description
-----------

Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

**Test case format:**

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with `val == 1`, the second node with `val == 2`, and so on. The graph is represented in the test case using an adjacency list.

**An adjacency list** is a collection of unordered **lists** used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the **copy of the given node** as a reference to the cloned graph.

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)

**Input:** adjList = \[\[2,4\],\[1,3\],\[2,4\],\[1,3\]\]
**Output:** \[\[2,4\],\[1,3\],\[2,4\],\[1,3\]\]
**Explanation:** There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/01/07/graph.png)

**Input:** adjList = \[\[\]\]
**Output:** \[\[\]\]
**Explanation:** Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

**Example 3:**

**Input:** adjList = \[\]
**Output:** \[\]
**Explanation:** This an empty graph, it does not have any nodes.

**Constraints:**

*   The number of nodes in the graph is in the range `[0, 100]`.
*   `1 <= Node.val <= 100`
*   `Node.val` is unique for each node.
*   There are no repeated edges and no self-loops in the graph.
*   The Graph is connected and all nodes can be visited starting from the given node.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    """
    # Definition for a Node.
    class Node:
        def __init__(self, val = 0, neighbors = None):
            self.val = val
            self.neighbors = neighbors if neighbors is not None else []
    """
    
    from typing import Optional
    from copy import deepcopy
    class Solution:
        def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
            return deepcopy(node)
            
    
            
            
    

[**102 Binary Tree Level Order Traversal** (link)](https://leetcode.com/problems/binary-tree-level-order-traversal/description)

Description
-----------

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**Input:** root = \[3,9,20,null,null,15,7\]
**Output:** \[\[3\],\[9,20\],\[15,7\]\]

**Example 2:**

**Input:** root = \[1\]
**Output:** \[\[1\]\]

**Example 3:**

**Input:** root = \[\]
**Output:** \[\]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 2000]`.
*   `-1000 <= Node.val <= 1000`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        o = []
        x = 0
        def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
                o = []
                def f(root, x =-1 ):
                    if not root:
                        return
                    x+=1
                    if len(o) == x:
                        o.append([])
    
                    o[x].append(root.val)
    
                    f(root.left, x)
                    f(root.right, x)
                f(root)
                return o
    
    
    

[**99 Recover Binary Search Tree** (link)](https://leetcode.com/problems/recover-binary-search-tree/description)

Description
-----------

You are given the `root` of a binary search tree (BST), where the values of **exactly** two nodes of the tree were swapped by mistake. _Recover the tree without changing its structure_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)

**Input:** root = \[1,3,null,null,2\]
**Output:** \[3,1,null,null,2\]
**Explanation:** 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)

**Input:** root = \[3,1,4,null,null,2\]
**Output:** \[2,1,4,null,null,3\]
**Explanation:** 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

**Constraints:**

*   The number of nodes in the tree is in the range `[2, 1000]`.
*   `-231 <= Node.val <= 231 - 1`

**Follow up:** A solution using `O(n)` space is pretty straight-forward. Could you devise a constant `O(1)` space solution?

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def recoverTree(self, root: Optional[TreeNode]) -> None:
            """
            Do not return anything, modify root in-place instead.
            """
            items = []
            def inorder(root):
                if root:
                    items.append(inorder(root.left))
                    items.append(root.val)
                    items.append(inorder(root.right))
    
            inorder(root)
            
            items = [i for i in items if i!=None]
    
            items2 = sorted(items)
            print(items, items2)
            for (x,y) in zip(items, items2):
                if x!=y:
                    print(x,y)
                    break
            
            items = [x,y]
            print(x,y)
    
            mapper = {x:y, y:x}
    
            wanted = []
            def f(tree):
    
                if not tree:
                    return
    
                if tree.val in items:
                    wanted.append(tree)
                f(tree.left)
                f(tree.right)
            
            f(root)
            print(wanted)
    
            for tree in wanted:
                tree.val = mapper[tree.val]
    
    
                        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

[**101 Symmetric Tree** (link)](https://leetcode.com/problems/symmetric-tree/description)

Description
-----------

Given the `root` of a binary tree, _check whether it is a mirror of itself_ (i.e., symmetric around its center).

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg)

**Input:** root = \[1,2,2,3,4,4,3\]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg)

**Input:** root = \[1,2,2,null,3,null,3\]
**Output:** false

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 1000]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Could you solve it both recursively and iteratively?

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            def helper(node1, node2):
                if not node1 and not node2:
                    return True
                
                if (node1 and not node2) or (node2 and not node1):
                    return False
    
                if node1.val!=node2.val:
                    return False
                
                return helper(node1.right, node2.left) and helper(node1.left, node2.right)
    
            return helper(root.left,root.right )
            
    

[**100 Same Tree** (link)](https://leetcode.com/problems/same-tree/description)

Description
-----------

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg)

**Input:** p = \[1,2,3\], q = \[1,2,3\]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg)

**Input:** p = \[1,2\], q = \[1,null,2\]
**Output:** false

**Example 3:**

![](https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg)

**Input:** p = \[1,2,1\], q = \[1,1,2\]
**Output:** false

**Constraints:**

*   The number of nodes in both trees is in the range `[0, 100]`.
*   `-104 <= Node.val <= 104`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
            def helper(node1, node2):
                if not node1 and not node2:
                    return True
                
                if (node1 and not node2) or (node2 and not node1):
                    return False
    
                if node1.val!=node2.val:
                    return False
                
                return helper(node1.right, node2.right) and helper(node1.left, node2.left)
    
            return helper(p,q )
            
    

[**98 Validate Binary Search Tree** (link)](https://leetcode.com/problems/validate-binary-search-tree/description)

Description
-----------

Given the `root` of a binary tree, _determine if it is a valid binary search tree (BST)_.

A **valid BST** is defined as follows:

*   The left subtree of a node contains only nodes with keys **strictly less than** the node's key.
*   The right subtree of a node contains only nodes with keys **strictly greater than** the node's key.
*   Both the left and right subtrees must also be binary search trees.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg)

**Input:** root = \[2,1,3\]
**Output:** true

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg)

**Input:** root = \[5,1,4,null,null,3,6\]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

**Constraints:**

*   The number of nodes in the tree is in the range `[1, 104]`.
*   `-231 <= Node.val <= 231 - 1`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isValidBST(self, root: Optional[TreeNode]) -> bool:
            def helper(root, lower=float('-inf'), upper=float('inf')):
    
                if not root:
                    return True
    
                if not(upper>root.val>lower):
                    return False
    
                return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
    
            return helper(root)
    

[**95 Unique Binary Search Trees II** (link)](https://leetcode.com/problems/unique-binary-search-trees-ii/description)

Description
-----------

Given an integer `n`, return _all the structurally unique **BST'**s (binary search trees), which has exactly_ `n` _nodes of unique values from_ `1` _to_ `n`. Return the answer in **any order**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

**Input:** n = 3
**Output:** \[\[1,null,2,null,3\],\[1,null,3,2\],\[2,1,3\],\[3,1,null,null,2\],\[3,2,null,1\]\]

**Example 2:**

**Input:** n = 1
**Output:** \[\[1\]\]

**Constraints:**

*   `1 <= n <= 8`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    class TreeNodeq:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
        def __repr__(self):
            return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"
    
    
    class Solution:
        def generateTrees(self, n: int):
            if n == 0:
                return []
    
            memo = {}
    
            def generate(start, end):
                if start > end:
                    return [None]
                all_trees = []
                for i in range(start, end + 1):
                    if ((start, i-1)) in memo:
                        left_trees = memo[(start, i - 1)]
                    else:
                        left_trees = generate(start, i - 1)
                        memo[(start, i - 1)] = left_trees
                    if ((i + 1, end)) in memo:
                        right_trees = memo[(i + 1, end)]
                    else:
                        right_trees = generate(i + 1, end)
                        memo[(i + 1, end)] = right_trees
                    for left in left_trees:
                        for right in right_trees:
                            root = TreeNode(i)
                            root.left = left
                            root.right = right
                            all_trees.append(root)
                return all_trees
    
            return generate(1, n)
    

[**96 Unique Binary Search Trees** (link)](https://leetcode.com/problems/unique-binary-search-trees/description)

Description
-----------

Given an integer `n`, return _the number of structurally unique **BST'**s (binary search trees) which has exactly_ `n` _nodes of unique values from_ `1` _to_ `n`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

**Input:** n = 3
**Output:** 5

**Example 2:**

**Input:** n = 1
**Output:** 1

**Constraints:**

*   `1 <= n <= 19`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def numTrees(self, n: int) -> int:
    
            values= {}
    
            def f(x):
                if x == 1:
                    return 1
                elif x == 0:
                    return 1
                elif x == 2:
                    return 2
                else:
                    k = 0
                    for i in range(x):
                        if i in values:
                            a= values[i]
                        else:
                            a = f(i)
                            values[i] = a
    
                        j = x-1-i
                        if j in values:
                            b = values[j]
                        else:
                            b = f(j)
                            values[j] = b
                            
                        k = k + a*b
                    return k
            return f(n)
            
    

[**94 Binary Tree Inorder Traversal** (link)](https://leetcode.com/problems/binary-tree-inorder-traversal/description)

Description
-----------

Given the `root` of a binary tree, return _the inorder traversal of its nodes' values_.

**Example 1:**

**Input:** root = \[1,null,2,3\]

**Output:** \[1,3,2\]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/08/29/screenshot-2024-08-29-202743.png)

**Example 2:**

**Input:** root = \[1,2,3,4,5,null,8,null,null,6,7,9\]

**Output:** \[4,2,6,5,7,1,3,9,8\]

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/08/29/tree_2.png)

**Example 3:**

**Input:** root = \[\]

**Output:** \[\]

**Example 4:**

**Input:** root = \[1\]

**Output:** \[1\]

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 100]`.
*   `-100 <= Node.val <= 100`

**Follow up:** Recursive solution is trivial, could you do it iteratively?

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode], index=0, output=[]) -> List[int]:
            what = []
            def f(root):
                if root:
                    f(root.left)
                    print(root.val)
                    what.append(root.val)
                    f(root.right)
    
            f(root)
    
            return what
    
    
    
    
            
            
    

[**9 Palindrome Number** (link)](https://leetcode.com/problems/palindrome-number/description)

Description
-----------

Given an integer `x`, return `true` _if_ `x` _is a_ _**palindrome**__, and_ `false` _otherwise_.

**Example 1:**

**Input:** x = 121
**Output:** true
**Explanation:** 121 reads as 121 from left to right and from right to left.

**Example 2:**

**Input:** x = -121
**Output:** false
**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

**Example 3:**

**Input:** x = 10
**Output:** false
**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

**Constraints:**

*   `-231 <= x <= 231 - 1`

**Follow up:** Could you solve it without converting the integer to a string?

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def isPalindrome(self, x: int) -> bool:
            if x < 0:
                return False
            x = str(x)
            length = len(x)//2
            for i in range(length):
                if x[i]!=x[-i-1]:
                    return False
            
            return True
            
    

[**5 Longest Palindromic Substring** (link)](https://leetcode.com/problems/longest-palindromic-substring/description)

Description
-----------

Given a string `s`, return _the longest_ _palindromic_ _substring_ in `s`.

**Example 1:**

**Input:** s = "babad"
**Output:** "bab"
**Explanation:** "aba" is also a valid answer.

**Example 2:**

**Input:** s = "cbbd"
**Output:** "bb"

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consist of only digits and English letters.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def longestPalindrome(self, s: str) -> str:
            if len(s) == 1:
                return s
            max_length = 0
            ii = 0
            # for i in [5]:
            for i in range(0,len(s)-1):
                if (s[i] != s[i+1]) or (s[i]==s[i+1]==s[i-1]):
                    start = s[:i][::-1]
                    end = s[i+1:]
                    length = 0
                    for x, y in zip(end, start):
                        if x == y:
                            length += 1
                        else:
                            break
                    length = 2*length + 1
                    if length > max_length:
                        max_length = length
                        ii = i 
    
                if s[i] == s[i+1]:
                    start = s[:i+1][::-1]
                    end = s[i+1:]
                    length = 0
                    for x, y in zip(end, start):
                        if x == y:
                            length += 1
                        else:
                            break
                    length = 2*length
                    if length > max_length:
                        max_length = length
                        ii = i 
            if max_length % 2 == 0:
                sub = max_length//2
                return  s[ii+1-sub:ii+1] + s[ii+1:ii+1+sub]
            else:
                t = (max_length-1)//2
                return s[ii-t:ii] + s[ii] + s[ii+1:ii+t+1]
            return None
                
    
            
    

[**42 Trapping Rain Water** (link)](https://leetcode.com/problems/trapping-rain-water/description)

Description
-----------

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

**Input:** height = \[0,1,0,2,1,0,1,3,2,1,2,1\]
**Output:** 6
**Explanation:** The above elevation map (black section) is represented by array \[0,1,0,2,1,0,1,3,2,1,2,1\]. In this case, 6 units of rain water (blue section) are being trapped.

**Example 2:**

**Input:** height = \[4,2,0,3,2,5\]
**Output:** 9

**Constraints:**

*   `n == height.length`
*   `1 <= n <= 2 * 104`
*   `0 <= height[i] <= 105`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def trap(self, height: List[int]) -> int:
    
            
            start_h = 0
            left_heights = []
            for h in height:
                if h > start_h:
                    left_heights.append(h)
                    start_h = h
                else:
                    left_heights.append(start_h)
            
            start_h = 0
            right_heights = []
            for h in height[::-1]:
                if h > start_h:
                    right_heights.append(h)
                    start_h = h
                else:
                    right_heights.append(start_h)
    
            right_heights = right_heights[::-1]
    
            water_amount = 0
            for h, h1, h2 in zip(height, left_heights, right_heights):
                min_h = min(h1, h2)
                water_amount += (min_h - h)
    
            return water_amount
    
    
    
    
            
    

[**37 Sudoku Solver** (link)](https://leetcode.com/problems/sudoku-solver/description)

Description
-----------

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1.  Each of the digits `1-9` must occur exactly once in each row.
2.  Each of the digits `1-9` must occur exactly once in each column.
3.  Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

**Example 1:**

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

**Input:** board = \[\["5","3",".",".","7",".",".",".","."\],\["6",".",".","1","9","5",".",".","."\],\[".","9","8",".",".",".",".","6","."\],\["8",".",".",".","6",".",".",".","3"\],\["4",".",".","8",".","3",".",".","1"\],\["7",".",".",".","2",".",".",".","6"\],\[".","6",".",".",".",".","2","8","."\],\[".",".",".","4","1","9",".",".","5"\],\[".",".",".",".","8",".",".","7","9"\]\]
**Output:** \[\["5","3","4","6","7","8","9","1","2"\],\["6","7","2","1","9","5","3","4","8"\],\["1","9","8","3","4","2","5","6","7"\],\["8","5","9","7","6","1","4","2","3"\],\["4","2","6","8","5","3","7","9","1"\],\["7","1","3","9","2","4","8","5","6"\],\["9","6","1","5","3","7","2","8","4"\],\["2","8","7","4","1","9","6","3","5"\],\["3","4","5","2","8","6","1","7","9"\]\]
**Explanation:** The input board is shown above and the only valid solution is shown below:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)

**Constraints:**

*   `board.length == 9`
*   `board[i].length == 9`
*   `board[i][j]` is a digit or `'.'`.
*   It is **guaranteed** that the input board has only one solution.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    from itertools import chain
    class Solution:
        def solveSudoku(self, board: List[List[str]]) -> None:
            """
            Do not return anything, modify board in-place instead.
            """
            rows = [set() for i in range(9)]
            columns = [set() for i in range(9)]
            boxes = [set() for i  in range(9)]
    
            for jj in range(9):
                for ii in range(9):
                    if board[jj][ii] != '.':
                        rows[jj].add(board[jj][ii])
                        columns[ii].add(board[jj][ii])
    
                        col_index = 3*(ii//3) + (jj//3)
                        boxes[col_index].add(board[jj][ii])
    
            def is_valid(j,i, num):
                if num in rows[j]:
                    return False
                
                if num in columns[i]:
                    return False
    
                box_index = 3*(i//3) + (j//3)
                if num in boxes[box_index]:
                    return False
    
                return True
    
            def solve(board, start_y, start_x):
                for y in chain(range(start_y, 9), range(0, start_y)):
                    for x in chain(range(start_x, 9), range(0, start_x)):
                        if board[y][x] == '.':
                            for num in range(1,10):
                                num = str(num)
                                if is_valid(y, x, num):
                                    board[y][x] = num
                                    rows[y].add(num)
                                    columns[x].add(num)
                                    boxes[3*(x//3)+(y//3)].add(num)
                                    start_x = x
                                    start_y = y
                                    if solve(board, start_y, start_x):
                                        return True
                                    board[y][x] = '.'
                                    rows[y].remove(num)
                                    columns[x].remove(num)
                                    boxes[3*(x//3)+(y//3)].remove(num)
                            return False
                return True
    
            start_x = 0
            start_y = 0
            solve(board,start_y, start_x )
    
                            
    

[**41 First Missing Positive** (link)](https://leetcode.com/problems/first-missing-positive/description)

Description
-----------

Given an unsorted integer array `nums`. Return the _smallest positive integer_ that is _not present_ in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

**Example 1:**

**Input:** nums = \[1,2,0\]
**Output:** 3
**Explanation:** The numbers in the range \[1,2\] are all in the array.

**Example 2:**

**Input:** nums = \[3,4,-1,1\]
**Output:** 2
**Explanation:** 1 is in the array but 2 is missing.

**Example 3:**

**Input:** nums = \[7,8,9,11,12\]
**Output:** 1
**Explanation:** The smallest positive integer 1 is missing.

**Constraints:**

*   `1 <= nums.length <= 105`
*   `-231 <= nums[i] <= 231 - 1`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def firstMissingPositive(self, nums: List[int]) -> int:
            minimum = sorted([x for x in nums if x >0])
            if len(minimum)==0:
                return 1
            minima = min(minimum)
            if minima > 1:
                return 1
            last = minima - 1
            for x in minimum:
                if x - last > 1:
                    return last+1
                last = x
            return x+1
            
    
            
    

[**3 Longest Substring Without Repeating Characters** (link)](https://leetcode.com/problems/longest-substring-without-repeating-characters/description)

Description
-----------

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

**Example 1:**

**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3. Note that `"bca"` and `"cab"` are also correct answers.

**Example 2:**

**Input:** s = "bbbbb"
**Output:** 1
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

**Constraints:**

*   `0 <= s.length <= 5 * 104`
*   `s` consists of English letters, digits, symbols and spaces.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            last = ''
            max_len= 0
            last_item = ''
            for x in s:
                if x not in last:
                    last += x
                    length = len(last)
                    max_len = max(length, max_len)
                else:
                    length = len(last)
                    max_len = max(length, max_len)
                    if x != last_item:
                        last = last.split(x)[-1] +x
                    else:
                        last = x
                last_item = x
            return max_len
            
    

[**4 Median of Two Sorted Arrays** (link)](https://leetcode.com/problems/median-of-two-sorted-arrays/description)

Description
-----------

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

**Input:** nums1 = \[1,3\], nums2 = \[2\]
**Output:** 2.00000
**Explanation:** merged array = \[1,2,3\] and median is 2.

**Example 2:**

**Input:** nums1 = \[1,2\], nums2 = \[3,4\]
**Output:** 2.50000
**Explanation:** merged array = \[1,2,3,4\] and median is (2 + 3) / 2 = 2.5.

**Constraints:**

*   `nums1.length == m`
*   `nums2.length == n`
*   `0 <= m <= 1000`
*   `0 <= n <= 1000`
*   `1 <= m + n <= 2000`
*   `-106 <= nums1[i], nums2[i] <= 106`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  
            f = sorted([*nums1, *nums2])
    
            length = len(f)
    
            if length%2 == 0:
                med = f[length//2-1] + f[length//2]
                return med/2
            else:
                return f[length//2]
    
            
    

[**7 Reverse Integer** (link)](https://leetcode.com/problems/reverse-integer/description)

Description
-----------

Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

**Input:** x = 123
**Output:** 321

**Example 2:**

**Input:** x = -123
**Output:** -321

**Example 3:**

**Input:** x = 120
**Output:** 21

**Constraints:**

*   `-231 <= x <= 231 - 1`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def reverse(self, x: int) -> int:
            reversed = str(x)[::-1]
            if reversed[-1] == '-':
                reversed = '-' + reversed[:-1]
    
            reversed = str(int(reversed))
            answer = int(reversed)
            if answer > (pow(2, 31) -1) or answer < -pow(2, 31):
                answer = 0 
            return answer
    

[**6 Zigzag Conversion** (link)](https://leetcode.com/problems/zigzag-conversion/description)

Description
-----------

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

**Example 1:**

**Input:** s = "PAYPALISHIRING", numRows = 3
**Output:** "PAHNAPLSIIGYIR"

**Example 2:**

**Input:** s = "PAYPALISHIRING", numRows = 4
**Output:** "PINALSIGYAHRPI"
**Explanation:**
P     I    N
A   L S  I G
Y A   H R
P     I

**Example 3:**

**Input:** s = "A", numRows = 1
**Output:** "A"

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
*   `1 <= numRows <= 1000`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    import copy
    class Solution:
        def convert(self, s: str, numRows: int) -> str:
            length = len(s)
            height = numRows
            box_width = 1 if height in [1,2] else (1+height-2)
            num_items = height + height - 2 if height not in [1] else 1
            num_boxes = length//num_items
            width2 = box_width*num_boxes
            remaining_width = length%num_items
            if not remaining_width:
                width3 = width2
            elif remaining_width <= height:
                # add 1
                width3 = width2+1
            else:
                width3 = width2+1+(remaining_width-height)
                
            print(height,box_width, num_items, num_boxes,width2,  remaining_width, width3)
                
            matrix = [[0 for _ in range(height)] for _ in range(width3)]
            print(matrix)
    #         matrix = copy.deepcopy([copy.deepcopy([0]*height)]*width3)
            start_row = 0
            start_col = 0
            for index, i in enumerate(s):
                matrix[start_col][start_row] = i
                if height == 1:
                    start_col +=1
                elif not start_col % box_width and start_row!=height-1:
                    start_row += 1
                else:
                    start_row -= 1
                    start_col += 1
            c = ''
            for i in range(height):
                for j in range(width3):
                    item = matrix[j][i]
                    if item:
                        c+=item
                        
            return c
    
    
    
    
    

[**93 Restore IP Addresses** (link)](https://leetcode.com/problems/restore-ip-addresses/description)

Description
-----------

A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

*   For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return _all possible valid IP addresses that can be formed by inserting dots into_ `s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

**Example 1:**

**Input:** s = "25525511135"
**Output:** \["255.255.11.135","255.255.111.35"\]

**Example 2:**

**Input:** s = "0000"
**Output:** \["0.0.0.0"\]

**Example 3:**

**Input:** s = "101023"
**Output:** \["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"\]

**Constraints:**

*   `1 <= s.length <= 20`
*   `s` consists of digits only.

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def restoreIpAddresses(self, s: str) -> List[str]:
            length = len(s)
            sets = set()
            for i in range(0,3):
                for j in range(0,3):
                    for k in range(0,3):
                        for l in range(0,3):
                            if (i + j + k + l) == length-4:
                                sets.add((i+1,j+1,k+1,l+1))
    
            valid_ips = []
            for (a, b, c, d) in sets:
                a1 = s[0:a]
                if not (int(a1) <= 255 and a1==str(int(a1))):
                    continue
                b1 = s[a:a+b]
                if not (int(b1) <= 255 and b1==str(int(b1))):
                    continue
                c1 = s[a+b:a+b+c]
                if not (int(c1) <= 255 and c1==str(int(c1))):
                    continue
                d1 = s[a+b+c:a+b+c+d]
                if not (int(d1) <= 255 and d1==str(int(d1))):
                    continue
                valid_ips.append(f"{a1}.{b1}.{c1}.{d1}")
    
            return valid_ips
    
    
    
    
    
    
            
    

[**11 Container With Most Water** (link)](https://leetcode.com/problems/container-with-most-water/description)

Description
-----------

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return _the maximum amount of water a container can store_.

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

**Input:** height = \[1,8,6,2,5,4,8,3,7\]
**Output:** 49
**Explanation:** The above vertical lines are represented by array \[1,8,6,2,5,4,8,3,7\]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

**Input:** height = \[1,1\]
**Output:** 1

**Constraints:**

*   `n == height.length`
*   `2 <= n <= 105`
*   `0 <= height[i] <= 104`

(scroll down for solution)

  

Solution
--------

Language: python3

Status: Accepted

    class Solution:
        def maxArea(self, height: List[int]) -> int:
            left = 0
            right = len(height) -1
            max_area = 0
            while left < right:
                max_area = max(max_area, (right-left)*(min(height[right], height[left])))
                if height[right] > height[left]:
                    left = left+1
                else:
                    right = right -1
    
            return max_area
    
    

[**20 Valid Parentheses** (link)](https://leetcode.com/problems/valid-parentheses/description)

Description
-----------

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

**Input:** s = "()"

**Output:** true

**Example 2:**

**Input:** s = "()\[\]{}"

**Output:** true

**Example 3:**

**Input:** s = "(\]"

**Output:** false

**Example 4:**

**Input:** s = "(\[\])"

**Output:** true

**Example 5:**

**Input:** s = "(\[)\]"

**Output:** false

**Constraints:**

*   `1 <= s.length <= 104`
*   `s` consists of parentheses only `'()[]{}'`.

(scroll down for solution)

  

Solution
--------

Language: python

Status: Accepted

    class Solution(object):
        def isValid(self, s):
            """
            :type s: str
            :rtype: bool
            """
            
            while True:
                old_len = len(s)
                s_new = s.replace('()', '').replace('{}', '').replace('[]', '')
                new_len = len(s_new)
                if new_len != old_len:
                    s = s_new
                elif not s_new:
                    return True
                else:
                    return False
            
    

[**120 Triangle** (link)](https://leetcode.com/problems/triangle/description)

Description
-----------

Given a `triangle` array, return _the minimum path sum from top to bottom_.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

**Example 1:**

**Input:** triangle = \[\[2\],\[3,4\],\[6,5,7\],\[4,1,8,3\]\]
**Output:** 11
**Explanation:** The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

**Example 2:**

**Input:** triangle = \[\[-10\]\]
**Output:** -10

**Constraints:**

*   `1 <= triangle.length <= 200`
*   `triangle[0].length == 1`
*   `triangle[i].length == triangle[i - 1].length + 1`
*   `-104 <= triangle[i][j] <= 104`

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?

(scroll down for solution)

  

Solution
--------

Language: python

Status: Accepted

    class Solution(object):
        def minimumTotal(self, triangle):
            """
            :type triangle: List[List[int]]
            :rtype: int
            """
            height = len(triangle)
            width = len(triangle[-1])
    
            for h in range(1, height):
                triangle[h][0] = triangle[h-1][0] + triangle[h][0]
                triangle[h][-1] = triangle[h-1][-1] + triangle[h][-1]
                
            for h in range(2, height):
                for w in range(1, h):
                    triangle[h][w] = triangle[h][w] + min(triangle[h-1][w-1], triangle[h-1][w])
                    
            return min(triangle[-1])