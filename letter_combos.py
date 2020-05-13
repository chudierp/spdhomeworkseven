''' Leetcode # 17 - https://leetcode.com/problems/letter-combinations-of-a-phone-number/ - Medium
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
    Example:
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution(object):
    def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
        mapping = { 
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }

        def step(combos, digits):
            if not digits:
                return combos
            combos = [i + each for i in combos for each in mapping.get(digits[0])]
            print(f"Combos: {combos}")
            return step(combos, digits[1:])

        if not digits:
            return []
        return step([i for i in mapping.get(digits[0])] , digits[1:])

if __name__ == "__main__":
    digits = "239"

    # test = map(lambda x, y: x + y, mapping.get(digits[0]), mapping.get(digits[1]))
    
    # print(list(test))
    # combos = []
    # for each in mapping.get(digits[0]):
    #     for val in mapping.get(digits[1]):
    #         combos.append(each + val)
    # print(combos)

    test = Solution().letterCombinations(digits)
    print(test)
    # print(digits)
    # print(digits[1:])

''' Variable Table
digits = "239"
          ^
mapping = { 
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
    }
in mapping.get(digit[0]):
    each = [ "a", "b", "c" ]
    i = ["ad", "ae", "af" ...]
    combo = [ "adw", "adx", "ady", "adz" ... ]
'''