def solution(s, skip, index):
    #아스키코드 a = 97, z = 122
    
    skip_set = set(ord(c) for c in skip)
    result = ""

    for want in s:
        code = ord(want)  

        move = 0
        while move < index:
            code += 1
            if code > 122:  
                code = 97
            if code not in skip_set:
                move += 1

        result += chr(code)

    return result