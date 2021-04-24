import requests
import json

#获取token
def getToken(ID,SECRET):

    API = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'.format(ID=ID,SECRET=SECRET)
    getToken = requests.get(API)
    access_token = json.loads(getToken.text)['access_token']
    return access_token

def send(access_token,agentid,personlist,content):

    API = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={ACCESS_TOKEN}'.format(ACCESS_TOKEN=access_token)
    touser = '{touser}'.format(touser='|'.join(personlist))
    toparty = ''
    totag = ''
    content = '{content}'.format(content=content)
    postdata = {
        "touser" : "{touser}".format(touser=touser),
        "toparty" : "{toparty}".format(toparty=toparty),
        "totag" : "{totag}".format(totag=totag),
        "msgtype" : "text",
        "agentid" : agentid,   #dcmtip的应用id
        "text" : {
            "content" : "{content}".format(content=content)
        },
        "safe":0,
        "enable_id_trans": 0,
        "enable_duplicate_check": 0,
        "duplicate_check_interval": 1800
    }
    return requests.post(url=API,json=postdata)

def getDepartmentPerson(access_token,department_id,fetch_child):

    API = 'https://qyapi.weixin.qq.com/cgi-bin/user/simplelist?access_token={ACCESS_TOKEN}&department_id={DEPARTMENT_ID}&fetch_child={FETCH_CHILD}'.format(ACCESS_TOKEN=access_token,DEPARTMENT_ID=department_id,FETCH_CHILD=fetch_child)
    return requests.get(API)

def getUserlist(res_text):

    userlist = {}
    raw_userlist = json.loads(res_text)['userlist']
    for user in raw_userlist:
        userlist[user['name']] = user['userid']
    return userlist