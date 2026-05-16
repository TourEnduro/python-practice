s = input('> ')
class Solution:
    # creating a method for subtracting any types of parentheses from the original string
    def subtract(self, s):
        # creating a dict with all types of parentheses
        parentheses = {
        1: "()",
        2: "[]",
        3: "{}"
        }
        # creating a copy of the original string to work with
        result = s
        # subtracting parentheses from the string using the dict
        for key, value in parentheses.items():
            result = result.replace(value, "")
        # returning result
        return result
    # creating a method for checking the length of the new string after subtraction
    def isValid(self, s: str) -> bool:
        # checking if the original string wasn't empty in the beginning
        if len(s) == 0:
            return False
        # comparing the length before and after subtraction
        before = len(s)
        result = self.subtract(s)
        after = len(result)
        # if the length is the same -> nothing happened, return False
        if before == after:
            return False
        # if the subtraction worked out -> repeat it until we get the length of an After string = 0
        while after < before:
            before = after
            result = self.subtract(result)
            after = len(result)
            if after == 0:
                return True
        else:
            return False
        
Solution = Solution()
print(Solution.isValid(s))