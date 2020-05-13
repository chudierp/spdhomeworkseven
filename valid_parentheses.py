''' Leetcode #20 - https://leetcode.com/problems/valid-parentheses/ - Easy
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
    Input: "()"     Output: true
Example 2:
    Input: "()[]{}" Output: true
Example 3:
    Input: "(]"     Output: false
Example 4:
    Input: "([)]"   Output: false
Example 5:
    Input: "{[]}"   Output: true
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        stack = []
        opened = ["(", "{", "["]
        closed = [")", "}", "]"]

        for each in s:
            if each in opened:
                stack.append(each)
            elif each in closed:
                index = closed.index(each)
                if len(stack) > 0 and (stack[len(stack)-1] == opened[index]):
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False    

if __name__ == "__main__":
    paren = "({[])"

    print(Solution().isValid(paren))

''' Variable Table
paren = "({[])"
opened = ["(", "{", "["]
closed = [")", "}", "]"]
stack = []
--------------
paren = "({[])"
         ^
opened = ["(", "{", "["]
           ^
closed = [")", "}", "]"]
stack | [ "(" ]
--------------
paren = "({[])"
          ^
opened = ["(", "{", "["]
                ^
closed = [")", "}", "]"]
stack | [ "(", "{" ]
--------------
paren = "({[])"
           ^
opened = ["(", "{", "["]
                     ^
closed = [")", "}", "]"]
stack | ["(", "{", "["]
                    ^
--------------
paren = "({[])"
            ^ 
stack | ["(", "{", "["]
                     ^
closed = [")", "}", "]"]
                     ^
stack | [ "(", "{" ] (pop)
--------------
paren = "({[])"
             ^ 
stack | ["(", "{" ]
               ^
closed = [")", "}", "]"]
           ^
stack | [ "(", "{"] (returns False)
'''