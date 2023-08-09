import requests,json,os

# 推送开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
# sever = os.environ["SERVE"]
sever = "on"
# 填写pushplus的sckey,不开启推送则不用填
# sckey = os.environ["SCKEY"]
sckey = "SCT219134TSgRnarsTJ3v4yvljYHdLFXLL"
# 填入glados账号对应cookie
# COOKIES = os.environ["COOKIES"]
COOKIES = "__stripe_mid=9476cbd5-0c21-4a09-aacd-4fa78fcd80909d5a19; _gid=GA1.2.1350363516.1691398492; Cookie=enabled; Cookie.sig=lbtpENsrE0x6riM8PFTvoh9nepc; koa:sess=eyJ1c2VySWQiOjM0MDUzNiwiX2V4cGlyZSI6MTcxNzQxOTU1NTE4MiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=QDCJSmV0qt8j4wKZNuLzKBvpBdo; _gat_gtag_UA_104464600_2=1; _ga=GA1.1.417899199.1666864336; _ga_CZFVKMNT9J=GS1.1.1691557120.34.1.1691560612.0.0.0&&_gid=GA1.2.145096105.1691462472; koa:sess=eyJ1c2VySWQiOjIzMjY4MiwiX2V4cGlyZSI6MTcxNzQwOTU3NzIzMiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=M21lQ0VRMz7B_qwDSVKnVuLiMz8; _gat_gtag_UA_104464600_2=1; _ga=GA1.1.145063380.1691462472; _ga_CZFVKMNT9J=GS1.1.1691560275.5.1.1691560911.0.0.0"
print(COOKIES)
cookies=COOKIES.split('&&')



def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    origin = "https://glados.rocks"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    payload={
        'token': 'glados.one'
    }
    for cookie in cookies:
        checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent,'content-type':'application/json;charset=UTF-8'},data=json.dumps(payload))
        state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer,'origin':origin,'user-agent':useragent})
    #--------------------------------------------------------------------------------------------------------#
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        email = state.json()['data']['email']
        if 'message' in checkin.text:
            mess = checkin.json()['message']
            if sever == 'on':
                requests.get('http://www.pushplus.plus/send?token=' + sckey + '&title='+mess+'&content='+email+' 剩余'+time+'天')
        else:
            requests.get('http://www.pushplus.plus/send?token=' + sckey + '&content='+email+'更新cookie')
     #--------------------------------------------------------------------------------------------------------#


def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
