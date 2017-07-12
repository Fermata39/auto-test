# command
import os
import subprocess

from src.setting.Command import Command


class ClearApp:
    def clearApp(object):
        os.system(Command().homeCmd)
        os.system(Command().recentsAcivityCmd)
        activityInfo = ""
        while True:
            os.system(Command().tabCommand)
            activityInfo = subprocess.check_output(Command().viewInfo,
                                                   stderr=subprocess.STDOUT,
                                                   shell=True).strip().decode('UTF-8')
            print("view info: ", activityInfo)

            if (activityInfo.find("mServedView=DecorView") == 0):
                break
            elif (activityInfo.find("mServedView=AppIcon") == 0 or activityInfo.find("mServedView=FolderIcon") == 0):
                break;
            else:
                os.system("adb shell input keyevent KEYCODE_DEL")
                continue

    def clearView(self):
        print("Enter Clear VIew")
        while True:
            os.system(Command().backCmd)
            windowInfo = subprocess.check_output(Command().activityInfo,
                                                 stderr=subprocess.STDOUT,
                                                 shell=True).strip().decode('UTF-8')

            print("windoinfo :", windowInfo)
            if (windowInfo.find(
                    "mCurrentFocus=Window") == 0):
                break;
            elif (windowInfo.find("mServedView=AppIcon") == 0 or windowInfo.find("mServedView=FolderIcon") == 0):
                break;
            else:
                os.system(Command.backCmd)
                continue
