def solution(answers):
    real_answer = []
    scores = []

    count1 = 0
    count2 = 0
    count3 = 0

    start2 = 0
    start3 = 0

    for index, answer in enumerate(answers):
        count2_answers = [1, 3, 4, 5]
        count3_answers = [3, 1, 2, 4, 5]

        # 수포자1
        if index % 5 + 1 == answer:
            count1 += 1

        if index % 2 == 0:
            # 수포자2
            if answer == 2:
                count2 += 1
            # 수포자3
            if answer == count3_answers[start3]:
                count3 += 1
        else:

            # 수포자2
            if answer == count2_answers[start2]:
                count2 += 1
            # 수포자3
            if answer == count3_answers[start3]:
                count3 += 1

            start2 += 1
            start2 = start2 % 4

            start3 += 1
            start3 = start3 % 5

    scores.append(count1)
    scores.append(count2)
    scores.append(count3)

    for i in range(3):
        if max(scores) == scores[i]:
            real_answer.append(i + 1)

    return real_answer


'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
'''