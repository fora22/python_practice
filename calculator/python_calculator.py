import re

class calculator():  # Calculator 객체 선언
    def __init__(self):
        self.stack = []
        self.postfix_notation = []
        self.operator = ["*", "/", "+", "-"]
        self.bracket = ["(", ")"]

    def input_infix(self, input_infix):
        p = re.compile("\W|\d+")
        self.mathmatical_expression = p.findall(input_infix)  # 2+3*(5+4*2)-3+6
        self.mathmatical_expression = self.delete_blank(self.mathmatical_expression)

    def delete_blank(self, m_e):
        i = 0
        while i != len(m_e):
            if m_e[i] == " ":
                m_e.pop(i)
                i = i - 1
            i = i + 1
        return m_e

    def is_number(self, x):
        if x not in self.operator and x not in self.bracket:
            return True
        else:
            return False

    def priority_judge(self, x):
        if (x == "*") or (x == "/"):
            return 1
        elif (x == "+") or (x == "-"):
            return 0
        elif (x == "("):
            return -1

    def change_postfix(self, mathmatical_expression):
        for m_e in mathmatical_expression:
            if self.is_number(m_e):
                self.postfix_notation.append(m_e)
            elif m_e in self.operator:
                prime_number = self.priority_judge(m_e)
                while len(self.stack) > 0:
                    top_of_stack = self.stack[-1]
                    if self.priority_judge(top_of_stack) < prime_number:  # 우선순위 구분이 이상함
                        break
                    while len(self.stack) > 0:
                        self.postfix_notation.append(self.stack.pop())
                self.stack.append(m_e)
            elif m_e == "(":
                self.stack.append(m_e)
            elif m_e == ")":
                while True:
                    temp = self.stack.pop()
                    if temp == "(":
                        break
                    self.postfix_notation.append(temp)

        while len(self.stack) > 0:
            self.postfix_notation.append(self.stack.pop())

    def calc_data(self):
        for op in self.postfix_notation:
            if self.is_number(op):
                self.stack.append(op)
            elif op in self.operator:
                y_stack = self.stack.pop()
                x_stack = self.stack.pop()
                temp = self.operation(x_stack, y_stack, op)
                self.stack.append(temp)
        if len(self.mathmatical_expression) == 0:
            print("수식을 잘못 입력하셨습니다.")
            print(" ")
        else:
            print(self.stack[0])
            print(" ")

    def operation(self, x, y, oper):
        if oper == "+":
            return float(x) + float(y)
        elif oper == "-":
            return float(x) - float(y)
        elif oper == "*":
            return float(x) * float(y)
        elif oper == "/":
            return float(x) / float(y)

    def calculator_start(self, input_data):
        try:
            self.input_infix(input_data)
            self.change_postfix(self.mathmatical_expression)
            self.calc_data()
        except IndexError:
            print("수식을 잘못 입력하셨습니다.")ㄴ
            print(" ")



if __name__ == "__main__":
    while True:
        print("c : 계산기 실행")
        print("s : 계산기 프로그램 종료")
        command = input("명령어를 입력하세요 : ")
        if command == "c":
            calc = calculator()
            data = input("수식을 입력하세요 : ")
            calc.calculator_start(data)
        elif command == "s":
            print(" ")
            print("프로그램이 종료됩니다.")
            break
        else:
            print("잘못된 입력입니다.")
            print(" ")

# def is_number(str):
#     try:
#         temp = float(str)
#         return True
#     except ValueError:
#         return False














