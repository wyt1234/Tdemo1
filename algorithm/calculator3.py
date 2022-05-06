def calculator3(s: str) -> int:
    s = s.replace(' ', '')
    if not len(s): return 0
    stack = []
    sign = '+'
    res = 0
    pre = 0
    i = 1
    while (i < len(s)):
        ch = s[i]
        # //处理两位数的问题
        if ch.isdigit():
            pre = pre * 10 + ord(ch) - ord('0')
        # 碰到左括号，就把括号里面当做一个新的被加数
        if (ch == '('):
            j = findClosing(s[i:])
            pre = calculator3(s[i + 1:i + j])
            i += j
        if i == len(s) - 1 or not ch.isdigit():
            # 将所有结果压栈，最后统一加起来
            if sign == '+':
                stack.append(pre)
                break
            elif sign == '-':
                stack.append(-pre)
                break
            elif sign == '*':
                stack.append(stack.pop() * pre)
                break
            elif sign == '/':
                stack.append(stack.pop() / pre)
                break
            pre = 0
            # 记录当前符号
            sign = ch
        i += 1
    # 本质上说全都是加法
    while len(stack):
        res += stack.pop()
    return res


# //删除所有的括号对，并返回右括号的位置
def findClosing(s: str):
    level = 0
    i = 0
    for i in range(len(s)):
        if s[i] == '(':
            level += 1
        elif s[i] == ')':
            level -= 1
            if level == 0:
                break
        else:
            continue
    return i


print(calculator3('(2+6* 3+5- (3*14/7+2)*5)+3'))
