import configparser

config = configparser.RawConfigParser()
# config.read("D:\\Credence Class Notes\\CredenceBatches\\Credence_Automation_Jan
# 24\\nopcom_Pytest\\Configuration\\config.ini")

config.read("C:\\Users\\SHREE\\PycharmProjects\\Nopcom_python\\Configuration\\config.ini")


class Readconfig:
    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password
