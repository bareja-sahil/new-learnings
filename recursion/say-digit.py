eng_dict = {0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'}


def say_digit(num):
    if num == 0:
        return
    say_digit(int(num / 10))
    print(eng_dict[num % 10], end=' ')

say_digit(432)