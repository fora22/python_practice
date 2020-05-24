import sys
import copy

class ServerOfTrain:
    def __init__(self):
        self.trainData = []
        self.program_set()

    def program_set(self):
        try:
            train_data = open('C:/Users/Assistant_2/paeng/VS_Code_Practice/Python_Study_to_eon/TrainList.txt', 'r')            # train_data에 파일 읽어오기
            while True:
                train_read = train_data.readline()        # train_read에 한 줄 읽고
                if not train_read:                             # train_read가 마지막줄이면 break
                    break
                train_read_data = train_read.split()      # train_read_data에 한 줄 씩 읽은 train_read를 공백마다 리스트 저장
                self.trainData.append(train_read_data)            # T_data에 하나씩 추가

            self.trainData.pop(0)                                      # T_data에 첫 리스트는 삭제

            return self.trainData
        except IOError as err:
            print('I/O Error:{0}'.format(err))                      # 예외처리
            return False

    def trainDataPrint(self):
        for i in range(len(self.trainData)):
            if self.trainData[i][5] == '0':
                self.trainData[i][5] = '매진'
            print(i, '. ', ' '.join(self.trainData[i]))

    def findCloseTime(self, userReservationinfo):
        timeBuffer = []
        copytDB = copy.deepcopy(self.trainData)

        for i in range(len(copytDB)):  
            if copytDB[i][1] != userReservationinfo[1]: 
                # 출발역과 다른 것 찾기
                copytDB[i][0] = '00000'
            
            if copytDB[i][3] != userReservationinfo[2]:
                # 도착역과 다른 것 찾기
                copytDB[i][0] = '00000'
            
            if copytDB[i][4] != userReservationinfo[3]:
                # 기차종류와 다른 것 찾기
                copytDB[i][0] = '00000'
            
        userReservationTime = int(userReservationinfo[0][:2]) * 60 + int(userReservationinfo[0][3:])
        for i in range(len(copytDB)):
            trainDataTime = int(copytDB[i][0][:2]) * 60 + int(copytDB[i][0][3:])
            timeBuffer.append(abs(trainDataTime - userReservationTime))

        closeTimeIndex = timeBuffer.index(min(timeBuffer))
        
        return closeTimeIndex
        
    def reservationComplete(self, searchCloseTimeIndex):
        temp = int(self.trainData[searchCloseTimeIndex][-1])
        temp = temp - 1
        self.trainData[searchCloseTimeIndex][-1] = str(temp)

        return searchCloseTimeIndex, self.trainData[searchCloseTimeIndex]
    
    def cancelReservation(self, cancelIndex):
        if cancelIndex != None:
            temp = int(self.trainData[cancelIndex][-1])
            temp = temp + 1
            self.trainData[cancelIndex][-1] = str(temp)