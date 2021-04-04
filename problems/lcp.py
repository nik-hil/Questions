# longest common prefix
# https://leetcode.com/problems/longest-common-prefix/

strs = ["flower","flow","flight"]
res = ""
stop = False
for i in range(len(strs[0])):
    c = strs[0][i]
    for j in range(len(strs)):
        if i >= len(strs[j]) or c != strs[j][i]:
            stop = True
            break
    if not stop:
        res += c
    else:
        break
    
print (res)
