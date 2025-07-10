def solution(babbling):
    ment = ["aya", "ye", "woo", "ma"]
    answer = 0

    for string in babbling:
        temp = string
        for m in ment:
            temp = temp.replace(m, " ")
        if temp.strip() == "":
            answer += 1

    return answer