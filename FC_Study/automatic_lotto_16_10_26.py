import random

"""
This py file is results of pair programming with Ra.
It's "lotto game."
User can buy tickets as many as possible.
Then he can compare his each lotto to answer_lotto.
Each lotto's price is 1000 won and winning prize money may differ to the rank he got.

And also I put lots of importance on output string arrangement. I used format functions a lot.
"""


count = 1
game_count = int(input('게임 수를 입력해주세요 : '))
game_count_digit = len(str(game_count))
cost_per_game = 1000
total_cost = cost_per_game * game_count
total_profit = 0

lotto_set = [str(i) for i in range(1, 45+1)]
answer_lotto = random.sample(lotto_set, 6)

prize = {
         6: {'money': 1000000000, 'rank': '1st'},
         5: {'money': 500000, 'rank': '3th'},
         4: {'money': 50000, 'rank': '4th'},
         3: {'money': 5000, 'rank': '5th'}
        }

print('Lotto number is ...\n {}'.format(answer_lotto))
print(('-'*40+'\n')*3)
while count <= game_count:

    user_lotto = random.sample(lotto_set, 6)

    match_count = sum([a in user_lotto for a in answer_lotto ])
    total_profit += prize.get(match_count, {'money': 0, 'rank': 'fail'})['money']



    print('The {count:{game_count_digit}d} game : {user_lotto} is {prize}.'.format(
                                       count=count,
                                       game_count_digit=game_count_digit,
                                       user_lotto=['{:2d}'.format(int(i)) for i in user_lotto],
                                       prize=prize.get(match_count, {'money': 0, 'rank': 'fail'})['rank']
                                       )
    )
    count += 1

print(('-'*40+'\n')*3)
print('Total purchasing cost is {:,} won.'.format(total_cost))
print('Total Winning prize is {:,} won.'.format(total_profit))
print(('-'*40+'\n')*3)

print('So, you {win_or_not} {money:,} won.'.format(
    win_or_not='got' if total_profit-total_cost >= 0 else 'lost',
    money=abs(total_profit-total_cost)
    )
)


"""
Results :

게임 수를 입력해주세요 : 5
Lotto number is ...
 ['43', '39', '6', '17', '2', '35']
----------------------------------------
----------------------------------------
----------------------------------------

The 1 game : ['43', '30', ' 9', '23', '16', '12'] is fail.
The 2 game : ['34', ' 1', ' 3', '11', '18', '22'] is fail.
The 3 game : ['35', ' 2', '37', '33', '39', ' 4'] is 5th.
The 4 game : ['23', '11', '44', ' 6', '17', '25'] is fail.
The 5 game : ['36', '44', '12', '15', '41', '10'] is fail.
----------------------------------------
----------------------------------------
----------------------------------------

Total purchasing cost is 5,000 won.
Total Winning prize is 5,000 won.
----------------------------------------
----------------------------------------
----------------------------------------

So, you got 0 won.
"""