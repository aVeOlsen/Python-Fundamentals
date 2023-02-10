import os
import json
#import requests
from pip._vendor import requests

secrets = dict(os.environ) #Dict laver en form for dictionary data struktur i python
json_secrets=json.dumps(secrets)

print(json_secrets)#Forskellen her fra secrets, er at alt er stringyfied, eller ja puttede i " " klammer, frem for ' '
print("\n")
#print(secrets) 

response = requests.get('https://html-css-js.replit.repl.co/')#simulere hvad en bot vil goere, altsaa ville dette vaere en post til mit system, med data, fremfor get som er skrevet

print(response.status_code)

file=open("secret.txt", "a")#Aabne det for append(tilfoejelse) som er derfor "a" staar der
file.write(json_secrets) 

file =open("secret.txt", "r")#r for read

line=file.readline()

print(line) 

#ALt er her et eksempel paa hvordan en bot kunne finde paa at virke, faa fat i data, send data, og vi kan ogsaa gemme data i en fil. Forskelligt hvordan bots er sat op
#Meget basic struktur, men hvad hvis vi vil lave ddos? Ja saa vil vi bare goere det hurtigere, putte url ind ved requests get, og bare koere det igen og igen