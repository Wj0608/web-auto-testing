import requests
import json
from config import globalparam

def req_get(path, params, headers):
    full_url = globalparam.URL + path
    try:
        r = requests.get(full_url, params=params, headers=headers)
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
        return r
    except BaseException as e:
        print("请求不能完成:", str(e))

def post_kv(path, data, headers):
    full_url = globalparam.URL + path
    try:
        r = requests.post(full_url, data=data, headers=headers)
            # 转换为python类型的字典格式,json包的响应结果，调用json(),转换成python类型
        StatusCode = r.status_code
            #print(json_r)
        # return json_r
        return r
    except BaseException as e:
        print("请求不能完成:", str(e))

def post_json(path, data, headers):
    full_url = globalparam.URL + path
    try:
        # python类型转化为json类型
        data = json.dumps(data)
        r = requests.post(full_url, data=data, headers=headers)
        return r
    except Exception as e:
        print("请求不能完成:", str(e))

            # req = urllib.request.Request('http://testing-api.intranet.szjys.com/secStrategy/getUserLoginSecStrategy?username=%s'% email)
            # req.add_header('authorization','Basic  YnJvd3Nlcjo=')
            # req.add_header('content-type','application/json')
            # res_data = urllib.request.urlopen(req)
            # res = res_data.read().decode('utf-8')

def json_to_python(responsedata):
    try:
        data = responsedata.json()
        return data
    except Exception as e:
        print("数据解析失败",str(e))

def ResponseCode(responsedata):
    return responsedata.status_code


if __name__ == '__main__':
    url ="/uaa/oauth/token"
    para = {"grant_type":"password","password":"123456","scope":"ui","source":"standard","username":"yangmengying8977@dingtalk.com"}
    header = {'Content-Type':'application/x-www-form-urlencoded', 'authorization':'Basic YnJvd3Nlcjo=',"origin":"https://pre-www.dae.org"}
    response = post_kv(url, para, header)
    print(ResponseCode(response))
    print(json_to_python(response)['mfa_token'])
    mfa_token = json_to_python(response)['mfa_token']

    url1='/uaa/mfa/challenge'
    para1 = {'challenge_type':'otp|oob','mfa_token':mfa_token}
    header1 = {'Content-Type':'application/json',"origin":"https://pre-www.dae.org"}
    response1 = post_json(url1, para1, header1)
    print(json_to_python(response1)['challenge_types'])