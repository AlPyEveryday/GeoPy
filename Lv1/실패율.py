def solution(N, stages):
    count = [0] * (N + 2)  # index 1~N, N+1은 클리어한 사람들

    for s in stages:
        count[s] += 1

    total = len(stages)
    result = []

    for i in range(1, N + 1):
        if total == 0:
            fail = 0
        else:
            fail = count[i] / total

        result.append((i, fail))
        total -= count[i]

    result.sort(key=lambda x: (-x[1], x[0]))
    return [x[0] for x in result]
