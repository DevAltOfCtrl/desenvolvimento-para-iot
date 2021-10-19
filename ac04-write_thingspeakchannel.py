import urllib.request
import threading
import psutil


def UsoCPU():
    cur_uso_cpu = psutil.cpu_percent()
    return cur_uso_cpu


def usoRAM():
    ram = psutil.virtual_memory().percent
    return ram


def thingspeak_post():
    threading.Timer(60, thingspeak_post).start()
    cpu = UsoCPU()
    ram = usoRAM()
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = 'QIFF3RFAYVKZXT16'
    HEADER = '&field1={}&field2={}'.format(cpu, ram)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)


if __name__ == '__main__':
    thingspeak_post()
