import re

class calculator():  # Calculator 객체 선언
    def __init__(self):
        self.stack = []                     # stack
        self.postfix_notation = []          # 후위 표기법으로 표현될 수식 그릇
        self.operator = ["*", "/", "+", "-"]   # 연산자 모음
        self.bracket = ["(", ")"]               # 괄호 모음(is_number 함수에 사용)

    def input_infix(self, input_infix):
        p = re.compile("\W|\d+")                # /d 숫자와 매칭, /W 문자+숫자가 아닌 문자와 매칭
        # 예시 : 2+3*(5+4*2)-3+6
        self.mathmatical_expression = p.findall(input_infix)       # 각각 단어를 구분해 리스트로 반환
        self.mathmatical_expression = self.delete_blank(self.mathmatical_expression)        # 공백 제거

    def delete_blank(self, m_e):
        i = 0
        while i != len(m_e):
            if m_e[i] == " ":
                m_e.pop(i)
                i = i - 1
            i = i + 1
        return m_e

    # operator와 bracket 에 없으면 숫자로 판단
    def is_number(self, x):
        if x not in self.operator and x not in self.bracket:
            return True
        else:
            return False

    # 우선순위 판단
    def priority_judge(self, x):
        if (x == "*") or (x == "/"):
            return 1
        elif (x == "+") or (x == "-"):
            return 0
        elif (x == "("):
            return -1

    # 후위표기법으로 변환
    def change_postfix(self, mathmatical_expression):
        for m_e in mathmatical_expression:
            if self.is_number(m_e):
                self.postfix_notation.append(m_e)   # 숫자이면 후위표기 배열에 추가
            elif m_e in self.operator:
                prime_number = self.priority_judge(m_e)
                while len(self.stack) > 0:
                    top_of_stack = self.stack[-1]
                    # stack에 있는 연산자보다 현재 연산자가 우선순위가 낮다면 stack에 있는 연산자를 다 후위표기 배열로 추가
                    if self.priority_judge(top_of_stack) < prime_number:        # 우선순위를 비교함
                        break
                    while len(self.stack) > 0:
                        self.postfix_notation.append(self.stack.pop())
                self.stack.append(m_e)
            elif m_e == "(":
                self.stack.append(m_e)      # ( 괄호 추가
            elif m_e == ")":
                # ( 를 만날 때 까지 stack에 있는 연산자를 다 후위표기 배열로 추가
                while True:
                    temp = self.stack.pop()
                    if temp == "(":
                        break
                    self.postfix_notation.append(temp)

        # stack에 남아있는 연사자 전부 후위표기 배열로 추가
        while len(self.stack) > 0:
            self.postfix_notation.append(self.stack.pop())

    def calc_data(self):
        for op in self.postfix_notation:
            if self.is_number(op):
                self.stack.append(op)
            elif op in self.operator:
                # 연산자를 만났기 때문에 stack에 있는 피연산자 2개 꺼내어 연산함
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
    
    # 계산기 사칙연산
    # git test
    def operation(self, x, y, oper):
        if oper == "+":
            return float(x) + float(y)
        elif oper == "-":
            return float(x) - float(y)
        elif oper == "*":
            return float(x) * float(y)
        elif oper == "/":
            return float(x) / float(y)

    # 계산기 시작
    def calculator_start(self, input_data):
        try:
            self.input_infix(input_data)
            self.change_postfix(self.mathmatical_expression)
            self.calc_data()
        except IndexError:
            print("수식을 잘못 입력하셨습니다.")
            print(" ")


# main 함수 시작
if __name__ == "__main__":
    while True:
        print("c : 계산기 실행")
        print("s : 계산기 프로그램 종료")
        command = input("명령어를 입력하세요 : ")
        if command == "c":
            calc = calculator()         # 객체를 연산때마다 부르니 불필요 (메모리 낭비) / 근데 수정하기 귀찮
            data = input("수식을 입력하세요 : ")
            calc.calculator_start(data)
        elif command == "s":
            print(" ")
            print("프로그램이 종료됩니다.")
            break
        else:
            print("잘못된 입력입니다.")
            print(" ")