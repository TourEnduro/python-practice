haystack = input('haystack> ')
needle = input('needle> ')

haylist = list(haystack)
needlelist = list(needle)

for i in range(len(haylist) - len(needlelist) + 1):
    result = []
    if needlelist[0] == haystack[i]:
        for j in range(len(needlelist)):
            if haylist[i + j] == needlelist[j]:
                result.append(haystack[i+j])
    if result == needlelist:
        print(i)
        break
else:
    print(-1)