import os
import subprocess

from src.setting.Command import Command


class SwitchWifi:
    def switchWIFI(object):
        print(">> Enter switch WIFI")
        count = 0
        wifiFlag = subprocess.check_output(Command().checkWifi,
                                           stderr=subprocess.STDOUT,
                                           shell=True).strip().decode('UTF-8')

        try:
            if (wifiFlag.find("0") == 0):
                print("Start WIFI enable")
                mSwitch = subprocess.check_output(Command().viewInfo,
                                                  stderr=subprocess.STDOUT,
                                                  shell=True).strip().decode('UTF-8')

                print(">> mSwitch: ", mSwitch)
                os.system(Command().wifiSettingView)

                if (mSwitch.find("android.widget.Switch") == -1):
                    while True:
                        os.system(Command().tabCommand)
                        mSwitch = subprocess.check_output(Command().viewInfo,
                                                          stderr=subprocess.STDOUT,
                                                          shell=True).strip().decode('UTF-8')

                        if (mSwitch.find("android.widget.Switch") != -1):
                            os.system(Command().enterCommand)
                            break
                        else:
                            count = count + 1

                        if (count > 20):
                            print("No search WIFI UI")
                            break
                else:
                    if (mSwitch.find("android.widget.Switch") != -1):
                        os.system(Command().enterCommand)
            else:
                print("Already WIFI enable")

            os.system(Command().homeCmd)
        except Exception:
            mSwitch = None

    def offWifi(self):
        print(">> Enter Off Wifi")
        count = 0
        wifiFlag = subprocess.check_output(Command().checkWifi,
                                           stderr=subprocess.STDOUT,
                                           shell=True).strip().decode('UTF-8')
        print("WifiFlage:", wifiFlag)
        if (wifiFlag.find("0") != 0):
            os.system(Command().wifiSettingView)
            mSwitch = subprocess.check_output(Command().viewInfo,
                                              stderr=subprocess.STDOUT,
                                              shell=True).strip().decode('UTF-8')

            print(">> [offWifi] mSwitch: ", mSwitch)
            if (mSwitch.find("android.widget.Switch") == -1):
                while True:
                    os.system(Command().tabCommand)
                    mSwitch = subprocess.check_output(Command().viewInfo,
                                                      stderr=subprocess.STDOUT,
                                                      shell=True).strip().decode('UTF-8')

                    if (mSwitch.find("android.widget.Switch") != -1):
                        os.system(Command().enterCommand)
                        break
                    else:
                        count = count + 1

                    if (count > 30):
                        print("No Search UI")
                        break
            else:
                if (mSwitch.find("android.widget.Switch") != -1):
                    os.system(Command().enterCommand)

            os.system(Command().disableWifiCmd)
            os.system(Command().homeCmd)
        else:
            print("Already WIFI Off")

    def TestWifi(self):
        mSwitch = subprocess.check_output(Command().viewInfo,
                                          stderr=subprocess.STDOUT,
                                          shell=True).strip().decode('UTF-8')

        if (mSwitch.find("android.widget.Switch") != -1):
            print("enter btn")
            os.system(Command().enterCommand)
        else:
            print("fail")
