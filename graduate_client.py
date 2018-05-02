import requests
import json
import urllib
import urllib2
import time


body_data = "temperature=15&flame=16&gas=17"
headers = {
'Host': '127.0.0.1:8081',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Content-Length': '30',
'Upgrade-Insecure-Requests': '1',
'Origin': 'http://127.0.0.1:8081',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Content-Type': 'application/x-www-form-urlencoded',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': 'http://127.0.0.1:8081/process_post',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': 'Hm_lvt_8e2a116daf0104a78d601f40a45c75b4=1522924145; BD_UPN=12314353'
}

temperature=1
flame=2
gas=3
while True:
    #response = requests.post('http://127.0.0.1:8081/process_post',data=body_data,headers=headers)
    time.sleep(1)
    temperature=temperature+1
    flame=flame+1
    gas=gas+1
    body_data="temperature"+"="+str(temperature)+"&flame"+"="+str(flame)+"&gas"+"="+str(gas)
    response = requests.post('http://127.0.0.1:8081/process_post',data=body_data,headers=headers)
    #print(response.text)

