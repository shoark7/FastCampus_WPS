"""
This game is called baseball game.
It was created by pair programming with Daejin Ra.

Computer makes a random 3-digit-number with no duplication of any digits.
And the user inputs another 3-digit-number. If two numbers in the same position has
same numbers, it's a Strike. And if the numbers are same but not in the same position
it's a Ball.
123             412             098         123
145             491             901         123
1s              1s 1b           2b          3s

User has to guess what the computer_number is.
The user has 9 times. Else, return False
"""

import random

def baseball():

    print("야구게임을 시작합니다.")
    computer_number = 0
    user_number = 0
    count = 1

    computer_number = str(random.randint(102,987))
    while len(set(computer_number))!=3:
        computer_number = random.randint(102,987)
    print("computer number : {}".format(computer_number))
    while count < 10:
        ball = 0
        strike = 0


        user_number = input("세 자리를 입력해주세요 : ")

        while True:
            if type(user_number) != int:
                user_number = input("정수를 입력해주세요 : ")
                continue
            elif len(str(user_number)) != 3:
                user_number = input("세 자리 정수를 다시 입력해주세요 : ")
                continue
            elif len(set(user_number)) != 3:
                user_number = input("각 자리수는 중복되지 않아야 합니다. : ")
                continue
            else:
                break

        computer_list= [
            int(n)
            for n
            in computer_number
        ]

        user_list = [
            int(n)
            for n
            in user_number
        ]

        # strike = sum([
        #     a == b
        #     for a,b
        #     in zip(computer_list, user_list)
        # ])
        #
        # for i in range(len(user_list)):
        #     for j in range(len(user_list)):
        #         if (i == j):
        #             pass
        #         elif (user_list[i]==computer_list[j]):
        #             ball += 1


        for i in range(len(user_list)):
            for j in range(len(user_list)):
                if i == j and user_list[i] == computer_number[j]:
                    strike += 1
                elif (user_list[i]==computer_list[j]):
                    ball += 1




        if strike == 3:
            print("정답입니다!")
            return "three_strike"
        elif strike == 0 and ball == 0:
            print("Out")

        else:
            print("Strike: {} Ball: {}".format(strike,ball))
        count += 1

    print("Game over!")



baseball()

"""
Pair programming was difficult at first but interesting.
By reviewing the code after completion, we saw many improvements point from previous one.

1. when controlling numbers without arithmetics it's better to make numbers into strings.
2. many combinations of functions can be simplified by making them a help function.
3. By using random.sample, we could make computer_number more tidy.

Pair programming was nice. I hope we have a lots of time with this.
"""