from scapy.all import*
#et starkt vaerktoej skrevet i python, som har en masse netvaerks analyse vaerktoejer


#spoerget efter en endless stream af packages i mit system, men her siger max 10 her
for pkt in sniff(iface='eth0', count=5):
   print('Packet :'+ str(pkt.summary()) +'\n') #foreach package(pkt=package) in sniff give me a summary an new line