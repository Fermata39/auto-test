import os
import subprocess

from src.file.WriteLogFile import WriteLogFile
from src.script.vowifi.VowifiRegi import VowifiRegi
from src.setting.AirplaneMode import AirplaneMode
from src.setting.ClearApp import ClearApp
from src.setting.Command import Command
from src.setting.InitialSetting import InitialSetting
from src.setting.LogSetting import LogSetting
from src.setting.SwitchWifi import SwitchWifi


class VowifiMMS(VowifiRegi):
    vMms = VowifiRegi()

    def vowifiScript(vMms):
        print(">> Enter VOWIFI for mms reg main")
        # getPermission()
        InitialSetting().getPermission()
        # enableAirplane()
        AirplaneMode().enableAirplane()
        # clearApp()
        ClearApp().clearApp();
        # xfrmLog()
        LogSetting().xfrmLog()
        # enableLog()
        LogSetting().enableLog()

        # vowifi
        vMms.enableVowifiOption()
        flag = vMms.checkRegiVowifi()

        if (flag == False):
            print(">> NO Regi")
            msg = "VOWIFI Fail-> WIFI DIsconnected"
            WriteLogFile().writeLogFile(False, msg)
        else:
            # pull logger
            LogSetting().get_log()
            # log parsing
            object.vowifi_logOpen()
            vMms.sendMMS()

        print("END Vowifi Regi + MMS send\n")
        # pull logger
        LogSetting().get_log()
        LogSetting().copyLog()
        # Disable Wifi
        SwitchWifi().offWifi()

    def checkSend(object):
        print("check send")
        count = 1
        while True:
            os.system(Command().tabCommand)
            viewInfo = subprocess.check_output(Command().viewInfo,
                                               stderr=subprocess.STDOUT,
                                               shell=True).strip().decode('UTF-8')
            print("viewinfo: ", viewInfo.find("app:id/send_button_text"))
            if (count <= 20 and viewInfo.find("app:id/send_button_text") == 85):
                print("Send MMS")
                os.system(Command().enterCommand)
            elif (count == 20):
                print("Test Fail")
                break
            else:
                count += 1

    def sendMMS(self):
        print("Start MMS")
        os.system(Command().homeCmd)
        os.system(Command().mmsCmd)
        self.checkSend()
