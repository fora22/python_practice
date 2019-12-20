import re

class calculator():  # Calculator 객체 선언
    def __init__(self):
        self.result = []  #

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

p = re.compile("\W|\d+")
t = p.findall("4 + 4*8+6-2/6+3")

def delete_blank(test):
    buf = []
    i = 0
    while i != len(test):
        if test[i] == " ":
            test.pop(i)
            i = i -1
        i = i + 1
    return test

t = delete_blank(t)
print(t)
