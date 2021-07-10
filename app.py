from program import Program
from db import Person
from util import Util

OEH = Person()
OEH.data_setter("오은하", 15, "여성")

DB_PEOPLE = []
DB_PEOPLE.append(OEH)

def startApp() :
    print("🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶")
    print("1. View People")
    print("2. Add People")
    print("3. Delete People")
    print("4. Exit Program")
    print("🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶🐶")

    an = Util.custom_input()

    if an == False :
        print("[SYSTEM] 잘못된 입력 입니다.")
        startApp()
    else:
            if an ==1: 
                Program.view_people(DB_PEOPLE)
                startApp()
            elif an == 2:
                result = Program.create_people(DB_PEOPLE)

                if result is True:
                    print("[SYSTEM] 새로운 사람이 추가 되었습니다.")
                    startApp()
                else:
                    print("[SYSTEM]  사람 추가에 실패했습니다. 다시시도 해주세요.")
                    startApp()
            elif an == 3:
                result = Program.delete_people(DB_PEOPLE)
                if result is True:
                    print("[SYSTEM] 사람이 삭제 되었습니다.")
                    startApp()
                else:
                    print("[SYSTEM]  사람 삭제에 실패했습니다. 다시시도 해주세요.")
                    startApp()
            elif an == 4:
                print("프로그램 종료할래!")
            else:
                print("[SYSTEM] 잘못 된 입력 입니다.")
                startApp()


startApp()