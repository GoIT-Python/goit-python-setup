riddle = "mi1rewopret"
word_length = 5
start_letter = "p"


def solve_riddle(riddle, word_length, start_letter, reverse=True):
    if reverse:
        riddle = riddle[::-1]
    start = riddle.find(start_letter)
    end = start + word_length
    res = riddle[start:end]
    return res


solve_riddle(riddle, word_length, start_letter)
