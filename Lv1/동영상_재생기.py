def solution(video_len, pos, op_start, op_end, commands):
    def second(t):
        m, s = map(int, t.split(':'))
        return m * 60 + s

    def mmss(sec):
        m = sec//60
        s = sec%60
        return f'{m:02d}:{s:02d}'

    total = second(video_len)
    now = second(pos)
    op_s = second(op_start)
    op_e = second(op_end)
    if op_s <= now <= op_e:
        now = op_e

    for c in commands:
        if c == "prev":
            now = max(0, now - 10)
        else: 
            now = min(total, now + 10)
        if op_s <= now <= op_e:  
            now = op_e

    return mmss(now)