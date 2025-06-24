def removeKdigits(num, k):
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    final = ''.join(stack[:len(stack)-k]).lstrip('0')
    return final or "0"
print(removeKdigits("1432219", 3)) 
