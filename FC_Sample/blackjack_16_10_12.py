import random

# Make a decklist. J, Q, K are all treated as 10 here.
DECK_LIST = [1,2,3,4,5,6,7,8,9,10,10,10,'A'] * 4

# Each player has these functions and attributes.
class Player:
    def __init__(self, name):
        self.name = name
        self.status = 0
        self.deck = []

    @property
    def deck_sum(self):
        if 'A' not in self.deck:
            return sum(self.deck)
        else:
            # 'A' can be either 1 or 11.
            # You have to count 'A' specially.
            len_of_A = self.deck.count('A')

            # 1. 10 보다 크면 11
            # 2.  9 보다 크면 11 + 1
            # 3 . 8 보다 크면 11 + 1 + 1
            other_sum = sum(n if n is not 'A' else 0 for n in self.deck)
            if other_sum > 11 - len_of_A:
                return other_sum + len_of_A
            else:
                return other_sum + 11 + (len_of_A - 1)

# Check it the player can draw more cards.
    def is_drawable(self):
        if self.deck_sum > 21:
            self.status = 0
            return False
        elif self.deck_sum == 21:
            self.status = 1
            return False
        else:
            return True

# If he or she can draw more, draw a card.
    def draw_card(self, number=1):
        for i in range(number):
            if self.is_drawable():
                card = random.choice(DECK_LIST)
                DECK_LIST.remove(card)
                self.deck.append(card)
        # the card goes into the player's deck and pops up from the DECK.



def main():
    user = Player('성환')
    dealer = Player('딜러')
    user_choice = ''


    print('게임을 시작하지.')
    print('=' * 60)
    user.draw_card(2)
    dealer.draw_card()

    while user.is_drawable() and user_choice != 's':
        print(str(user.deck)+', 총합 : {}'.format(user.deck_sum))
        user_choice = input('Hit? or Stop?(h or s) : ').strip().lower()
        # Get player's choice. He can choose to draw a card or not.
        print()
        if user_choice == 'h':
            user.draw_card()
        else:
            break
    # Dealer can't draw more cards when sum of his cards go over 17.
    while dealer.is_drawable():
        dealer.draw_card()
        if dealer.deck_sum >= 17:
            dealer.status = 1
            break

    print('유저 총합 : {:2}, 카드 셋 {}'.format(user.deck_sum if user.deck_sum < 22 else '파산', user.deck))
    print('딜러 총합 : {:2}, 카드 셋 {}'.format(dealer.deck_sum if dealer.deck_sum < 22 else '파산', dealer.deck))
    print()

    if user.status == 1 and dealer.status == 1:
        print('최종 결과 : {} 승리!'.format(user.name if user.deck_sum >= dealer.deck_sum else dealer.name))
    elif user.status == 0 and dealer.status == 0:
        print('최종 결과 : 무승부!')
    else:
        if user.status == 1:
            print('최종 결과 : {} 승리!'.format(user.name))

        else:
            print('최종 결과 : {} 승리!'.format(dealer.name))



if __name__ == '__main__':
    main()