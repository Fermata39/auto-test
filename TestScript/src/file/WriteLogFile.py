class WriteLogFile(object):
    @staticmethod
    def writeLogFile(flag, msg):
        if (flag == True):
            f = open("vowifi_result.log", 'w')
            f.write(msg + '\n')
            f.close()
        else:
            f = open("vowifi_result.log", 'w')
            f.write(msg + '\n')
            f.close()
