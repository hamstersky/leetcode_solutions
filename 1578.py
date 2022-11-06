def minCost(colors, neededTime):
    time = 0
    cur_sequence = []
    for i, color in enumerate(colors):
        if not i + 1 < len(colors):
            if cur_sequence:
                cur_sequence.append(neededTime[i])
                time += sum(cur_sequence) - max(cur_sequence)
                cur_sequence = []
            break
        if colors[i + 1] == color:
            cur_sequence.append(neededTime[i])
        else:
            if cur_sequence:
                cur_sequence.append(neededTime[i])
                time += sum(cur_sequence) - max(cur_sequence)
                cur_sequence = []

    return time


# print(minCost("abaac", [1, 2, 3, 4, 5]))
# print(minCost("abc", [1, 2, 3]))
# print(minCost("aabaa", [1, 2, 3, 4, 1]))
print(minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
