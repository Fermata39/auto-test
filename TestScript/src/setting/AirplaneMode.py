import os
import subprocess

from src.setting.Command import Command


class AirplaneMode:
    def enableAirplane(self):
        print(">> Enter enableAirplane")
        try:
            airplaneInfo = subprocess.check_output(Command().airplaneCheckCmd,
                                                   stderr=subprocess.STDOUT,
                                                   shell=True).strip().decode('UTF-8')
            print(airplaneInfo)
            if (airplaneInfo.find("0") == 0):
                os.system(Command().airplaneEnableCmd)
            else:
                print("Already Airplane")
        except Exception:
            pass

    def disableAirplane(self):
        print(">> Enter disableAirplane")
        os.system(Command().airplaneDisableCmd)