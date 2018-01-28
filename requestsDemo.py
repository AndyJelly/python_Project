import requests
import json
from requests import exceptions


URL = 'https://api.github.com'

def build_url(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent =4)

def request_method():
    resp = requests.get(build_url('user/emails'),auth=('AndyJelly','hgdamtl1314'))
    print (better_print(resp.text))
    print (resp.request.headers)
    print (resp.url)
    print (resp.status_code)


def request_params():
    resp = requests.get(build_url('users'),params= {'since':10})
    print (better_print(resp.text))
    print (resp.request.headers)
    print (resp.url)
    print (resp.status_code)

def timeout_request():
    try:
        resp = requests.get(build_url('user/emails'),timeout =10)
        resp.raise_for_status()
    except exceptions.Timeout as e:
        pass
        #print(e.message)
    except exceptions.HTTPError as e:
        pass
        #print (e.message)

    else:
        print(better_print(resp.text))
        print (resp.request.headers)
        print (resp.url)
        print (resp.status_code)

def hard_request():
    from requests import Request,Session
    #创建session对象
    s= Session()
    #创建Request对象
    headers = {'User-Agent':'faked by hgd'}
    req = Request('GET',build_url('user/emails'),auth=('AndyJelly','hgdamtl1314'),headers = headers)
    #准备发送数据
    prepped = req.prepare()
    print(prepped.body)
    print(prepped.headers)

    #正式发送
    resp = s.send(prepped,timeout=10)
    print (resp.request.headers)
    print (resp.url)
    print (resp.status_code)
    print (better_print(resp.text))
    print (resp.elapsed)


def download_pic():
    url = 'http://www.666img.com/images/1463625.jpg'
    resp = requests.get(url,stream = True)
    with open('demo.jpg','wb') as fd:
        for chunk in resp.iter_content(1024):
            fd.write(chunk)

    print (resp.status_code)

def download_pic_impoved():
    url = 'http://www.666img.com/images/1463625.jpg'
    #关闭流
    from contextlib import closing
    #存储流数据
    with closing(requests.get(url,stream = True)) as resp:
        with open('demo1.jpg','wb') as fd:
            #每128个字节写入一次
            for chunk in resp.iter_content(128):
                fd.write(chunk)

#事件钩子，相当于回调函数
def event_hooks_callback(response,*args,**kwargs):
    print (response.headers)

def event_hooks():
    requests.get('https://www.baidu.com/',hooks = dict(response=event_hooks_callback))

def print_url(resp,*args,**kwargs):
    print(resp.url)

def record_hook(resp, *args, **kwargs):
    resp.hook_called = True
    return resp


if __name__ == '__main__':
    hooks = {'response' : [print_url,record_hook]}
    #hooks = {'response' : print_url}
    resp = requests.get('http://httpbin.org', hooks=hooks)
    print (resp)
    print (resp.hook_called)

    #event_hooks()
