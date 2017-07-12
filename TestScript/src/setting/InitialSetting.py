import subprocess

from src.setting.Command import Command


class InitialSetting:
    def getPermission(object):
        print(">> Enter initSetting")
        try:
            output = subprocess.check_output(Command().homeCmd,
                                             stderr=subprocess.STDOUT,
                                             shell=True).strip().decode('UTF-8')
            root = subprocess.check_output(Command().adbRootCmd,
                                           stderr=subprocess.STDOUT,
                                           shell=True).strip().decode('UTF-8')
            remount = subprocess.check_output(Command().adbRemountCmd,
                                              stderr=subprocess.STDOUT,
                                              shell=True).strip().decode('UTF-8')

        except:
            output = None
            root = None
            remount = None
