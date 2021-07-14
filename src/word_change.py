stage = 0


def solution(begin, target, words):
    answer = 0

    DFS(begin, target, words, 0)
    answer = stage

    return answer

'''
DFS 방식으로 풀게되면 최소 단계가 자동으로 결정됨 
깊이가 얕은게 가장 나중에 실행되기 때문
'''

def DFS(begin, target, words, count):
    global stage
    if begin == target:
        stage = count
        return
    for index, word in enumerate(words):
        diff = 0

        for num in range(len(word)):
            if begin[num] != word[num]:
                diff += 1
        if diff == 1:
            words.remove(word)
            DFS(word, target, words, count + 1)
            words.insert(index, word)

    return
