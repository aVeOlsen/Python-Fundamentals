import socket
import time


ports=[20,21,22,23,25,53,69,80,137,139,106,443,445,465,585]
for i in ports:
    s=socket.socket()   
    s.settimeout(5)
    result = s.connect_ex(('206.189.49.197', i))
    if(result==0):
            print("Port {} is open".format(i))
            time.sleep(1)
            s.close()
            assert result==0
    else:
            print("Port {} is closed".format(i))
            s.close()









