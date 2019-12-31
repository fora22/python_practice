import re

class node:
    def __init__(self, item):
        self.item = item
        self.right_node = None
        self.left_node = None

class calculator():  # Calculator 객체 선언
    def __init__(self):
        self.result = []
        self.root



    def add(self, x, y):
        add_result = x + y
        return add_result

    def substract(self, x, y):
        substract_result = x - y
        return substract_result

    def multifly(self, x, y):
        multifly_result = x * y
        return multifly_result

    def divide(self, x, y):
        divide_result = x / y
        return divide_result



def delete_blank(test):
    i = 0
    while i != len(test):
        if test[i] == " ":
            test.pop(i)
            i = i -1
        i = i + 1
    return test

def is_number(str):
    try:
        temp = float(str)
        return True
    except ValueError:
        return False

stack = []
postfix_notation = []


p = re.compile("\W|\d+")
mathmatical_expression = p.findall("2+3*(5+4*2)-3+6")
mathmatical_expression = delete_blank(mathmatical_expression)



for m in mathmatical_expression:
    if is_number(m):
        postfix_notation.append(m)
    else:
        stack.append(m)





for i in range(len(t)):
    if t[i].isdecimal():
        postfix_notation.append(t[i])
    elif t[i] == ')':
        for j in range(len(stack)):
            postfix_notation.append(stack[j])
        del stack[:]
        postfix_notation.remove("(")
    elif i == (len(t)-1):
        for j in range(len(stack)):
            postfix_notation.append(stack[j])
        del stack[:]
    else:
        stack.append(t[i])

print(t)

