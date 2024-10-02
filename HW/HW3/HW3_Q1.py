def validateNestedParenthese(brackets):
    paren_map = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    stack = []

    for bracket in brackets:
        if bracket in "({[":
            stack.append(bracket)
        elif len(stack) and paren_map[bracket] == stack[-1]:
            stack.pop()
        else:
            return False

    return True


test1 = "[(({()})())()]"
test2 = " )(){("
print(validateNestedParenthese(test1))
print(validateNestedParenthese(test2))
