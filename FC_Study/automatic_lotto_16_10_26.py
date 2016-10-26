import random

"""
This py file was results of pair programming with Ra.
It's "lotto game."
User can buy tickets as many as possible.
Then he can compare his each lotto to answer_lotto.
Each lotto's price is 1000 won and prize money may differ to the rank he got.

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
         5: {'momey': 500000, 'rank': '3th'},
         4: {'money': 50000, 'rank': '4th'},
         3: {'money': 5000, 'rank': '5th'}
        }

print('Lotto number is ...\n {}'.format(answer_lotto))
print(('-'*40+'\n')*3)
while count <= game_count:

    user_lotto = random.sample(lotto_set, 6)

    match_count = sum([a in user_lotto for a in answer_lotto ])
    total_profit += prize.get(match_count, {'money':0, 'rank':'fail'})['money']



    print('The {count:{game_count_digit}d} game : {user_lotto} is {prize}.'.format(
                                       count=count,
                                       game_count_digit=game_count_digit,
                                       user_lotto=['{:2d}'.format(int(i)) for i in user_lotto],
                                       prize=prize.get(match_count, {'money':0, 'rank':'fail'})['rank']
                                       )
    )
    count += 1

print(('-'*40+'\n')*3)
print('Total purchasing cost is {:,} won.'.format(total_cost))
print('Total Winning prize is {:,} won.'.format(total_profit))
print(('-'*40+'\n')*3)

print('So, you {win_or_not} {money:,} won.'.format(
    win_or_not='won' if total_profit-total_cost > 0 else 'lost',
    money=abs(total_profit-total_cost)
    )
)


"""
Results :

게임 수를 입력해주세요 : 5
Lotto number is ...
 ['9', '24', '33', '42', '35', '18']
----------------------------------------
----------------------------------------
----------------------------------------

The 1 game : ['28', '33', '35', ' 3', '10', '43'] is fail.
The 2 game : ['31', ' 8', '25', ' 3', '29', '38'] is fail.
The 3 game : ['25', '33', '30', '22', '32', ' 8'] is fail.
The 4 game : [' 7', '43', '27', '12', '38', '44'] is fail.
The 5 game : ['28', '14', '13', '23', '10', ' 5'] is fail.
----------------------------------------
----------------------------------------
----------------------------------------

Total purchasing cost is 5,000 won.
Total Winning prize is 0 won.
----------------------------------------
----------------------------------------
----------------------------------------

So, you lost 5,000 won.
"""