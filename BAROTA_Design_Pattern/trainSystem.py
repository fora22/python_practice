import sys
import trainServer
import trainUser


class trainSystem:
    def __init__(self):
        self.tUserList = []
        
        self.tDB = trainServer.ServerOfTrain()

        self.tUserSelection = None

    def systemStart(self):
        logIn = input("로그인 하시겠습니까? y/n : ")
        if not((logIn == 'Y') or (logIn == 'y')):
            return

        if len(self.tUserList) == 0:
            self.tUser = trainUser.Passenger()
            self.tUser.getIDPW()
            self.tUserList.append(self.tUser)
            print("Log-in 되었습니다.")
        else:
            self.tUser = trainUser.Passenger()
            userID, userPW = self.tUser.getIDPW()
            for i in range(len(self.tUserList)):
                if self.tUserList[i].returnIDPW() == (userID, userPW):
                    self.tUser = self.tUserList[i]
                    print("Log-in 되었습니다.")
                    break
                else:
                    self.tUserList.append(self.tUser)

        self.systemMenu()

    def systemMenu(self):
        print('메뉴를 선택하세요')
        print('1. 빠른시간 기차 검색 및 예매')
        print('2. 전체 기차 리스트 출력')
        print('3. 나의 예매 현황 출력 및 예매 취소')
        print('4. 프로그램 종료')
        self.tUserSelection = self.tUser.selectMenuNumber()

        if self.tUserSelection == 1:
            self.reservation()
        elif self.tUserSelection == 2:
            self.tDB.trainDataPrint()
        elif self.tUserSelection == 3:
            cancel = self.tUser.myReservationInfo()
            self.tDB.cancelReservation(cancel)
        elif self.tUserSelection == 4:
            self.systemShutDown()
    
    def systemShutDown(self):
        print("Log-out은 0, 종료는 1을 눌러주십시오")
        command = int(input("명령어 입력 : "))
        if command == 0:
            self.systemStart()
        elif command == 1:
            return
        else:
            self.systemShutDown()

    def reservation(self):
        print("기차 정보를 출력합니다.\n")

        self.tDB.trainDataPrint() # 기존 데이터 출력

        userReservationCloseTimeIndex = self.tDB.findCloseTime(self.tUser.userReservationInfo())#.userReservationCloseTime))
        print("가장 가까운 기차는 다음과 같습니다.")
        print(self.tDB.trainData[userReservationCloseTimeIndex])
        print()
        checkQuestion = input("예매하시겠습니까? y/n : ")

        if (checkQuestion == "Y") or (checkQuestion == "y"):
            tempIndex, tempInfo = self.tDB.reservationComplete(userReservationCloseTimeIndex)
            self.tUser.saveReservation(tempIndex, tempInfo)
            self.systemMenu()
        else:
            self.systemMenu()


if __name__ == "__main__":
    BAROTA = trainSystem()
    BAROTA.systemStart()





