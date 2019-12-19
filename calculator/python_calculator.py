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

p = re.compile("[0-9]+")
m = p.search("python")
print(m)
t = p.findall("31python")
print(t)
print()