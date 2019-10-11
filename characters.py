from copy import deepcopy


def valid_braces(word):
    chars = deepcopy(list(word))
    valid_braces = ['{}', '()', '[]']
    actual_braces = []
    for index, ch in enumerate(list(word)):
        if len(chars) > 0:
            actual_second_brace = chars[-1]
            actual_braces.append(ch + actual_second_brace)
            chars.remove(actual_second_brace)
            try:
                chars.remove(ch)
            except ValueError or IndexError:
                break
    return set(actual_braces) <= set(valid_braces)


print(valid_braces('{[(]}'))  # => False
print(valid_braces('{[((]}'))  # => False
print(valid_braces('{[]}'))  # => True
print(valid_braces('{[()]}'))  # => True
