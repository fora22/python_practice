import sys

class Passenger:
    def __init__(self):
        self.userID = None
        self.userPW = None
        self.userReservation = {}

    def returnIDPW(self):
        return self.userID, self.userPW

    def getIDPW(self):
        try:
            print("ID 와 PW를 입력해주십시오")
            self.userID = input("ID : ")
            self.userPW = input("PW : ")
            return self.userID, self.userPW
        except IOError:
            print("잘못된 입력입니다.\n")
            self.getIDPW()

    def selectMenuNumber(self):
        try:
            select = int(input('명령어를 입력해주십시오 : '))              # 명령어 select 입력
            return select
        except ValueError:
            print('입력이 잘못되었습니다.\n')                                # 예외처리
            self.selectMenuNumber()

    def userReservationInfo(self):
        inputTrainDataBuffer = input('찾으시는 기차 정보를 입력해주세요 - ex) 09:34(시간) 서울(출발역) 부산(도착역) KTX(열차종류) : ')
        userReservationTrainData = ['08:00', '서울', '부산', '새마을호']#inputTrainDataBuffer.split()#['0705', '서울', '부산', 'KTX']

        return userReservationTrainData

    def saveReservation(self, reservationIndex, reservationInfo):
        self.userReservation[reservationIndex] = reservationInfo

    def checkIDPW(self):
        try:
            print("예매 취소를 위해 ID 와 PW를 재입력해주십시오")
            whoID = input("ID : ")
            whoPW = input("PW : ")
            
            if (self.userID == whoID) and (self.userPW == whoPW):
                return True
            else:
                print("잘못된 ID입니다.")
                return False
            
        except IOError:
            print("잘못된 입력입니다.\n")
            self.getIDPW()

    def myReservationInfo(self):
        print("1. 예매현황 출력")
        print("2. 예매 취소하기")
        print("이외의 것을 누를경우 나가기")
        print()

        try:
            reservationSelection = int(input("명령어를 입력해주십시오 : "))
        except ValueError:
            print('입력이 잘못되었습니다.\n')                                # 예외처리
            self.myReservationInfo()

        if self.checkIDPW():

            if reservationSelection == 1:
                for i in self.userReservation:
                    print(self.userReservation[i])
                    print()
                self.myReservationInfo()
            elif reservationSelection == 2:
                for i in self.userReservation:
                    print("예매번호 : ", i, ", 예매정보 : ", self.userReservation[i])
                
                deleteKey = int(input("삭제할 예매번호를 입력해주세요 : "))
                self.userReservation.pop(deleteKey)

                return deleteKey
            else:
                return
        
        else:
            return


            
        
        


