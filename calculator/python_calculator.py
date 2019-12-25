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
    buf = []
    i = 0
    while i != len(test):
        if test[i] == " ":
            test.pop(i)
            i = i -1
        i = i + 1
    return test

stack = []
postfix_notation = []


p = re.compile("\W|\d+")
t = p.findall("4 + 46*8+6-2/6+3")
t = delete_blank(t)

for i in range(len(t)):
    if t[i].isdecimal():
        postfix_notation.append(t[i])
    else:
        stack.append(t[i])

print(stack)
print(postfix_notation)

