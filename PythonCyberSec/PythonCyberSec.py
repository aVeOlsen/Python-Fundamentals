
import re

f= open('access.log')

#Faar fat i access log og splitter denne med en linje
log_contents = filter(None, f.read().split('\n')) 

for line in (log_contents):
    entries=re.findall(r'"([^"]*)', line) #Bruger et regulaert udtry til at finde et moenster. Kan aendre denne til at lede efter forskellige moenstre
    url=entries[0].split(' ')[1]# bruger moenster fra foer til at forsat at sende data videre
    url_parts=url.split('?')
    
    if(len(url_parts)>1):
        query=url_parts[1] #faar fat i query delen som er delen der kommet efter ? fra sidste linje i for loop
        if(query.find('password')>-1): #og hvis et password saa er fundet saa vil dette blive fundet her
            print("Likely credentials found:")
            print(query)
            print("\n")