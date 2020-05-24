import sys
import tkinterHomework as th

class train:
    def __init__(self):
        self.T_data = []                                            # 열차 데이터
        self.train_time = []                                        # 시간 찾기위한 time 데이터
        self.blank = ' '
        # self.TK = th.trainTk()


    def program_set(self):
        try:
            self.train_data = open('C:/Users/Assistant_2/paeng/VS_Code_Practice/Python_Study_to_eon/TrainList.txt', 'r')            # train_data에 파일 읽어오기
            while True:
                self.train_read = self.train_data.readline()        # train_read에 한 줄 읽고
                if not self.train_read:                             # train_read가 마지막줄이면 break
                    break
                self.train_read_data = self.train_read.split()      # train_read_data에 한 줄 씩 읽은 train_read를 공백마다 리스트 저장
                self.T_data.append(self.train_read_data)            # T_data에 하나씩 추가

            self.T_data.pop(0)                                      # T_data에 첫 리스트는 삭제
            return True
        except IOError as err:
            print('I/O Error:{0}'.format(err))                      # 예외처리
            return False



    def program_start(self):
        print('메뉴를 선택하세요')
        print('1. 빠른시간 기차 검색 및 예매')
        print('2. 전체 기차 리스트 출력')
        print('3. 나의 예매 현황 출력 및 예매 취소')
        print('4. 프로그램 종료')
        try:
            select = int(input('명령어를 입력해주십시오 : '))              # 명령어 select 입력
        except ValueError:
            print('입력이 잘못되었습니다.')                                # 예외처리

        if select == 1:
            self.menu_1()
        elif select == 2:
            self.menu_2()
        elif select == 3:
            self.menu_3()
        elif select == 4:
            self.menu_4()

        self.program_start()     # program_start는 
        return select


    def direct_reservation(self):
        select = int(input('직접 예약할 번호를 입력해주십시오 : '))
        if int(self.T_data[select][5]) <= 0:
            print('자리가 꽉 차서 예매하실 수 없습니다. 죄송합니다.')
        else:
            self.T_data[select][5] = str(int(self.T_data[select][5]) - 1)
            print('예약되었습니다.')
            self.my_ticketing = self.T_data[select]

    def find_closer_time(self):
        for i in range(len(self.T_data)):
            train_time_buffer = self.T_data[i][0]
            train_time_buffer = train_time_buffer[:2] + train_time_buffer[3:]#.pop(2) # 가운데 :제거에서 리스트말고 문자열로 고칠것
            self.train_time.append(train_time_buffer)
        #print(self.train_time)
        self.input_train_data_buffer = input('찾으시는 기차 정보를 입력해주세요 - ex) 0934(시간) 서울(출발역) 부산(도착역) KTX(열차종류) : ')
        self.input_train_data = self.input_train_data_buffer.split()#['0705', '서울', '부산', 'KTX']

        test_time = (int(self.input_train_data[0][:2]) * 60 + int(self.input_train_data[0][2:4]))
        test_time_first = 0
        test_time_second = 0
        for i in range(len(self.T_data)):
            if (self.T_data[i][1] == self.input_train_data[1]) and (self.T_data[i][3] == self.input_train_data[2]) and (self.T_data[i][4] == self.input_train_data[3]):
                if test_time > abs((int(self.input_train_data[0][:2])*60 + int(self.input_train_data[0][2:4]))-(int(self.train_time[i][:2])*60 + int(self.train_time[i][2:4]))):
                    test_time_second = test_time_first
                    test_time_first = i
                    test_time = abs((int(self.input_train_data[0][:2])*60 + int(self.input_train_data[0][2:4]))-(int(self.train_time[i][:2])*60 + int(self.train_time[i][2:4])))
        print('입력한 시간과 가장 가까운 기차입니다. 둘 중 하나를 골라 예매해주십시오. 돌아가고싶다면 0을 입력해주십시오.')
        print('1.', self.T_data[test_time_first])
        print('2.', self.T_data[test_time_second])
        select = int(input())
        if select == 1:
            if int(self.T_data[test_time_first][5]) <= 0:
                print('자리가 꽉 차서 예매하실 수 없습니다. 죄송합니다.')
            else:
                self.T_data[test_time_first][5] = str(int(self.T_data[test_time_first][5]) - 1)
                print('예약되었습니다.')
                self.my_ticketing = self.T_data[test_time_first]
        elif select == 2:
            if self.T_data[test_time_second][5] <= 0:
                print('자리가 꽉 차서 예매하실 수 없습니다. 죄송합니다.')
            else:
                self.T_data[test_time_first][5] = str(int(self.T_data[test_time_first][5]) - 1)
                print('예약되었습니다.')
                self.my_ticketing = self.T_data[test_time_second]
        elif select == 0:
            self.menu_1()
        else:
            print('잘못된 입력입니다.')

    def menu_1(self):
        self.menu_2()
        print('가까운 시간을 찾으시겠습니까? 직접 예약하시겠습니까?')
        select = int(input('1번 : 가까운 시간 찾기 / 2번 : 직접 예약 / 0번 : 뒤로가기'))
        if select == 1:
            self.find_closer_time()
        elif select == 2:
            self.direct_reservation()
        # elif select == 0:
        #     self.program_start()

    def menu_2(self):
        self.whole_train = self.T_data
        for i in range(len(self.whole_train)):
            if self.whole_train[i][5] == '0':
                self.whole_train[i][5] = '매진'
            print(i, '. ', self.blank.join(self.whole_train[i]))
        

    def menu_3(self):
        print(self.blank.join(self.my_ticketing))

    def menu_4(self):
        return


if __name__ == "__main__":
    print('바로타(BAROTA) 프로그램')
    barota = train()
    barota.program_set()
    barota.program_start()