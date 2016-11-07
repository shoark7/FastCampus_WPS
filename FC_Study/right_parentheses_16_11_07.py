"""
We use '()': parentheses in expressions.
For example '(3+4) * 5' is right format.
However, '))3 + 4 ((' wouldn't be right format.
We check if given expressions have right type of parentheses.
"""


def check_right_format(text):
    """
    Check if the parentheses usage in given text is right or wrong.
    :param text: given expression.
    :return: True if format is right else False.
    """
    check_count = 0
    for c in text:
        if c == '(':
            check_count += 1
        elif c == ')':
            check_count -= 1

        if check_count < 0:
            print("올바르지 않은 형식입니다.")
            return False
    if check_count == 0:
        print('올바른 형식입니다.')
        return True
    else:
        print("올바르지 않은 형식입니다.")
        return False

