StringMap = ["ABCD", "ABBA", "BBAA", "CCDD"]
Palindrome = ""
for i in range(4):
    row = StringMap[i]
    for start in range(1):
        word = row[start:start+4]
        if word == word[::-1]:
            Palindrome = word

print(Palindrome)

for i in range(4):
    col = ""
    for j in range(4):
        col = col+StringMap[j][i]
    for start in range(1):
        word = col[start:start+4]
        if word == word[::-1]:
            Palindrome = word

print(Palindrome)