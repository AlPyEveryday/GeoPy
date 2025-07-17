def solution(lottos, win_nums):
    def bitmask(nums):
        mask = 0
        for n in nums:
            if n != 0:       
                mask |= 1 << (n - 1) 
        return mask

    def count_bits(x):
        return bin(x).count('1')

    unknown = lottos.count(0)

    mask_win_nums = bitmask(win_nums)
    mask_lottos   = bitmask(lottos)

    matched = count_bits(mask_win_nums & mask_lottos)

    best = matched + unknown
    worst = matched

    def rank(x):
        if x>= 2:
            return 7 - x
        else:
            return 6

    return [rank(best), rank(worst)]
