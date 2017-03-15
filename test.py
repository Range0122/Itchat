import itchat
import time

itchat.auto_login(hotReload=True)

name = itchat.search_friends(wechatAccount='TheMessenger13')

n = name[0]['UserName']
print n
if itchat.send_msg(msg='Hi stupid boy~', toUserName=n):
    for i in xrange(0, 50):
        itchat.send_msg(msg='Hi stupid boy~', toUserName=n)
time.sleep(2)

itchat.logout()
