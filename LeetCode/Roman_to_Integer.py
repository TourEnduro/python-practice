s = input('> ')
intlist = []
result = 0
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = list(s)
        for l in roman:
            if l == "I":
                intlist.append(1)
            elif l == "V":
                if intlist and intlist[-1] == 1:
                    intlist.pop()
                    intlist.append(4)
                else:
                    intlist.append(5)
            elif l == "X":
                if intlist and intlist[-1] == 1:
                    intlist.pop()
                    intlist.append(9)
                else:
                    intlist.append(10)
            elif l == "L":
                if intlist and intlist[-1] == 10:
                    intlist.pop()
                    intlist.append(40)
                else:
                    intlist.append(50)
            elif l == "C":
                if intlist and intlist[-1] == 10:
                    intlist.pop()
                    intlist.append(90)
                else:
                    intlist.append(100)
            elif l == "D":
                if intlist and intlist[-1] == 100:
                    intlist.pop()
                    intlist.append(400)
                else:
                    intlist.append(500)
            elif l == "M":
                if intlist and intlist[-1] == 100:
                    intlist.pop()
                    intlist.append(900)
                else:
                    intlist.append(1000)
            else:
                exit()
        return sum(intlist)
solution = Solution()
print(solution.romanToInt(s))