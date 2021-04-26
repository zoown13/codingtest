stack = []
sentence = input()
for i in range(len(sentence)):
    if sentence[i] == '{' or sentence[i] == '(':
        stack.append(sentence[i])
    elif sentence[i] == '}' and stack and stack[-1] == '{':
        stack.pop()
    elif sentence[i] == ')' and stack and stack[-1] == '(':
        stack.pop()
    else:
        pass

if stack or sentence.count('{') != sentence.count('}') or sentence.count('(') != sentence.count(')'):
    print('Not Correct Sentence')
else:
    print('Correct Sentence')
