def isValid(s: str):
    pairs = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for parenthesis in s:
        if parenthesis in pairs:
            stack.append(parenthesis)
        elif not stack or pairs[stack.pop()] != parenthesis:
            return False

    return len(stack) == 0


in1 = "()"
in2 = "()[{}"
in3 = "(]"
in4 = "())"

print(isValid(in1))
print(isValid(in2))
print(isValid(in3))
print(isValid(in4))
