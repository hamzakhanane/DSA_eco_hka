# Runtime O(n)
# Memory O(n)

def isValid(s):
    stack = []
    char_map = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    for char in s:
        if char in char_map:
            stack.append(char)
        else:
            if len(stack) > 0 and char == char_map[stack[-1]]:
                stack.pop()
            else:
                return False
    return True if len(stack) == 0 else False