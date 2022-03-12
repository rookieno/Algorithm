s = "(())()"


def is_correct_parenthesis(string):
    stack = []
    string_index = len(string)
    for i in range(string_index):
        if string[i] == '(':
            stack.append(i)
        elif string[i] == ')':
            if string_index == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!