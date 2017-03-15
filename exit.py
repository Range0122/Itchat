import time

import itchat

def lc():
    print('finish login')
def ec():
    print('exit')

itchat.auto_login(loginCallback=lc, exitCallback=ec)
time.sleep(3)
itchat.logout()