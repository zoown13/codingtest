from math import floor


def make_sets(string):

    word_set = dict()
    for i in range(len(string)-1):
        parsed_word = string[i:i+2]
        if parsed_word.isalpha():
            lowered_word = parsed_word.lower()
            if lowered_word in word_set:
                count = word_set[lowered_word] + 1
                word_set[lowered_word] = count
            else:
                word_set[lowered_word] = 1

    return word_set


def calculate_jaccard_index(str1, str2):

    intersect = dict()
    union = dict()

    if len(str1) == 0 and len(str2) == 0:
        return 1 * 65536

    for word in str1.keys():
        if word in str2:
            intersect[word] = min(str1[word], str2[word])
            union[word] = max(str1[word], str2[word])
        else:
            union[word] = str1[word]

    for word in str2.keys():
        if word not in union:
            union[word] = str2[word]

    if len(intersect) == 0:
        return 1 * 65536

    num_intersect = 0
    num_union = 0

    for num in intersect.values():
        num_intersect = num_intersect + num
    for num in union.values():
        num_union = num_union + num

    jaccard_index = floor((num_intersect / num_union) * 65536)

    return jaccard_index


def solution():
    str1 = ""
    str2 = ""

    str1_set = make_sets(str1)
    str2_set = make_sets(str2)

    print(calculate_jaccard_index(str1_set,str2_set))


if __name__ == '__main__':
    solution()