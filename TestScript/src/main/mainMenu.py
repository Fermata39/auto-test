from Tools.scripts.treesync import raw_input

from src.script.vowifi.VowifiCall import VowifiCall
from src.script.vowifi.VowifiMMS import VowifiMMS
from src.script.vowifi.VowifiRegi import VowifiRegi
from src.setting.AirplaneMode import AirplaneMode
from src.setting.SwitchWifi import SwitchWifi


def viewMenu():
    print("=====================================")
    print("[VOWIFI] [0] Test END")
    print("[VOWIFI] [1] Vowifi Regi ")
    print("[VOWIFI] [2] Vowifi Regi + MMS send ")
    print("[VOWIFI] [3] Vowifi Regi + Call ")
    print("[VOWIFI] [4] HO (W to L)")
    print("[VOWIFI] [5] HO (L to W)")
    print("[VOWIFI] [6] HO (L to W) in Call")
    print("[VOWIFI] [7] HO (L to W) in Call")
    print("[VOWIFI] [8] VOWIFI ALL Case")
    print("=====================================")


def selectMenu():
    while True:
        viewMenu()
        try:
            cmd = str(raw_input("Input Command: "))
            print("cmd: ", cmd)

            if (cmd.find("1") == 0):
                VowifiRegi().vowifiScript()
            elif (cmd.find("2") == 0):
                # print("[2] Vowifi Regi + MMS send 구현 안됨\n")
                VowifiMMS().vowifiScript()
            elif (cmd.find("3") == 0):
                # print("[3] Vowifi Regi + Call 구현 안됨\n")
                VowifiCall().vowifiScript()
            elif (cmd.find("4") == 0):
                print("[4] HO (W to L) 구현 안됨\n")
            elif (cmd.find("5") == 0):
                print("[5] HO (L to W) 구현 안됨\n")
            elif (cmd.find("6") == 0):
                print("[6] HO (L to W) in Call 구현 안됨\n")
            elif (cmd.find("7") == 0):
                print("[7] HO (L to W) in Call 구현 안됨\n")
            elif (cmd.find("8") == 0):
                print("[8] VOWIFI ALL Case 구현 안됨\n")
                VowifiRegi().vowifiScript()
                VowifiMMS().vowifiScript()
                VowifiCall().vowifiScript();
            elif (cmd.find("0") == 0):
                print("[0] Test END\n")
                break;
            else:
                print("입력 규칙을 벗어나셨습니다\n")

        except ValueError:
            print("입력 규칙을 벗어나셨습니다\n")
            pass


if __name__ == '__main__':
    print("enter Main")
    selectMenu()
    # SwitchWifi().TestWifi();
    # AirplaneMode().enableAirplane()
