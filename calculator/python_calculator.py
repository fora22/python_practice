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

# def is_number(str):
#     try:
#         temp = float(str)
#         return True
#     except ValueError:
#         return False

def is_number(x):
    if x not in operator and x not in bracket:
        return True
    else:
        return False

def priority_judge(x):
    if (x == "*") or (x == "/"):
        return 1
    elif (x == "+") or (x == "-") or (x == "("):
        return 0



stack = []
postfix_notation = []
operator = ["*", "/", "+", "-"]
bracket = ["(", ")"]

p = re.compile("\W|\d+")
mathmatical_expression = p.findall("(2+5)*3*(2+1)") #2+3*(5+4*2)-3+6
mathmatical_expression = delete_blank(mathmatical_expression)

for m_e in mathmatical_expression:
    if is_number(m_e):
        postfix_notation.append(m_e)
    elif m_e in operator:
        prime_number = priority_judge(m_e)
        while len(stack) > 0:
            top_of_stack = stack[-1]
            if priority_judge(top_of_stack) <= prime_number:            # 우선순위 구분이 이상함
                break
            # while len(stack) > 0:
            #     temp = stack.pop()
            #     if temp == "(":
            #         break
            #     postfix_notation.append(temp)
            postfix_notation.append(stack.pop())
        stack.append(m_e)

    elif m_e == "(":
        stack.append(m_e)
    elif m_e == ")":
        while True:
            temp = stack.pop()
            if temp == "(":
                break
            postfix_notation.append(temp)

while len(stack) > 0:
    postfix_notation.append(stack.pop())


# def count_bracket(math_exp):        # 괄호 개수를 세는 함수
#     count_left = 0
#     count_right = 0
#     for m_e in math_exp:
#         if m_e == "(":
#             count_left = count_left + 1
#         elif m_e == ")":
#             count_right = count_right + 1
#
#     if count_right == count_left:
#         return count_right
#     else:
#         print("수식이 잘못 입력되었습니다.")
#         return -1
#
# count = count_bracket(mathmatical_expression)
# stack = [[] for x in range(count + 1)]          # comprehension을 활용한 satck list
# postfix_notation = [[] for x in range(count + 1)]



'''
number = 0
for m_e in mathmatical_expression:          # 후위 표기법 작성
    if m_e == "(":
        number = number + 1
    elif m_e == ")":
        for p_n in postfix_notation[number]:
            postfix_notation[number-1].append(p_n)
        number = number - 1
    elif is_number(m_e):
        postfix_notation[number].append(m_e)
    else:
        if (m_e == "*") or (m_e == "/"):
            if (stack[number][-1] == "*") or (stack[number][-1] == "/"):
                stack[number].append(m_e)
            elif (stack[number][-1] == "+") or (stack[number][-1] == "-"):
                postfix_notation[number] = postfix_notation[number] + stack[number]
        elif (m_e == "+") or (m_e == "-"):
            # 여기부터 해야되는데...
            stack[number].append(m_e)
'''



# for m in mathmatical_expression:
#     if is_number(m):
#         postfix_notation.append(m)
#     else:
#         stack.append(m)





# for i in range(len(t)):
#     if t[i].isdecimal():
#         postfix_notation.append(t[i])
#     elif t[i] == ')':
#         for j in range(len(stack)):
#             postfix_notation.append(stack[j])
#         del stack[:]
#         postfix_notation.remove("(")
#     elif i == (len(t)-1):
#         for j in range(len(stack)):
#             postfix_notation.append(stack[j])
#         del stack[:]
#     else:
#         stack.append(t[i])
#
# print(t)

