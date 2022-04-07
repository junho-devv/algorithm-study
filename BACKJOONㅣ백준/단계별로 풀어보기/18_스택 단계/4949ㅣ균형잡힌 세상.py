while True:
    in_s = input()

    if in_s == '.':
        break

    brackets = []
    answer = True

    for s in in_s:

        if s == '(' or s == '[':
            brackets.append(s)

        elif s == ')':
            if not brackets or brackets[-1] == '[':
                answer = False
                break
            else:
                brackets.pop()

        elif s == ']':
            if not brackets or brackets[-1] == '(':
                answer = False
                break
            else:
                brackets.pop()

    if answer and not brackets:
        print("yes")
    else:
        print("no")
