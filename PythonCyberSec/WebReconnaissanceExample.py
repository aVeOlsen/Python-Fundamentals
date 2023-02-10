import hashlib
import json

from pip._vendor import requests 
from pip._vendor.requests.exceptions import Timeout

domain ='aveo93-001-site1.ftempurl.com'
uuid=hashlib.md5(domain.encode('utf-8')).hexdigest()

try:
    response=requests.get('https://'+domain, timeout=2)
    if(response.status_code == 200):
        uses_ssl=True
    else:
        uses_ssl=False
except:
    print('Request timed out at https connection')
    uses_ssl=False
try:
    result = requests.get('http://'+domain)
    status_code=result.status_code
except:
    print('No connection')

uses_http = (result.status_code==200)
if(uses_http==False & uses_ssl==False):
    print('No connection')

uses_css = (result.text.find('<link rel="stylesheet')>-1)
uses_js=(result.text.find('<script language="JavaScript')>-1)

profile={'uuid':uuid, 'name':domain, 'uses_http':uses_http, 'uses_ssl':uses_ssl, 'uses_css':uses_css, 'uses_js':uses_js}
print(json.dumps(profile))
 






#print(profile)
#print('Http: ')
#print(uses_http)
#print('\nCss: ')
#print(uses_css) 
#print('\nJavascript: ')
#print(uses_js)

#if(ssl_result==200):# fejl kode
#    print('ssl succes')
#    uses_ssl=True
#else:
#    print('no ssl')
#    uses_ssl=False