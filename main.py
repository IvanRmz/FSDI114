from MyStack import Stack
from MyQueue import Queue2Stacks

def reverseStr(string):
    stack = Stack()
    for character in string:
        stack.push(character)

    newStr = ''
    while stack.size() > 0:
        newStr += stack.pop()

    return newStr

specialCase = {
    '[' : ']',
    ']' : '[',
    '(' : ')',
    ')' : '(',
    '{' : '}',
    '}' : '{',
}
def balance_check(s):
    if len(s) == 0 or len(s)%2 != 0:
        return False

    j = len(s)-1
    for i  in range(j):
        if i > j:
            return True
        elif s[i] in specialCase:
            if specialCase[s[i]] == s[j]:
                j-=1
                continue
            else:
                return False
        elif s[i] == s[j]:
            j-=1
            continue
        else:
            return False


def test ():
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


if __name__  == "__main__":
    # string = "Ivan"
    # print(f'Reverse ({string})  = {reverseStr("Ivan")}')

    # stringToBalanceCheck = "[(dd)]"
    # print(f'String to check balance ({stringToBalanceCheck}) = {balance_check(stringToBalanceCheck)}')

    # test()
    n = 5
    print(f'Factorial of {n} = {fact(n)}')
    print(f'Fibonacii of {n} = {fib(n)}')