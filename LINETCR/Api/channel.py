# -*- coding: utf-8 -*-
import os, sys, json
path = os.path.join(os.path.dirname(__file__), '../lib/')
sys.path.insert(0, path)
import requests

from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol

from curve import LineService
from curve.ttypes import *
import tempfile

class Channel:
    client = None

    host = "gd2.line.naver.jp"
    http_query_path = "/S4"
    channel_query_path = "/CH4"

    UA = "Line/6.0.0 iPad4,1 9.0.2"
    LA = "DESKTOPMAC 10.10.2-YOSEMITE-x64    MAC 4.5.0"

    authToken = None
    mid = None
    channel_access_token = None
    token = None
    obs_token = None
    refresh_token = None

    def __init__(self, authToken):
        self.authToken = authToken
        self.transport = THttpClient.THttpClient('https://gd2.line.naver.jp:443'+self.http_query_path)
        self.transport.setCustomHeaders({ "User-Agent" : self.UA,
        "X-Line-Application" : self.LA,
        "X-Line-Access": self.authToken
        })
        self.transport.open()
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.client = LineService.Client(self.protocol)
        self.mid = self.client.getProfile().mid
        self.transport.path = self.channel_query_path

    def login(self):
        result = self.client.issueChannelToken("1341209950")

        self.channel_access_token = result.channelAccessToken
        self.token = result.token
        self.obs_token = result.obsToken
        self.refresh_token = result.refreshToken

        print "channelAccessToken:" + result.channelAccessToken
        print "token:" + result.token
        print "obs_token:" + result.obsToken
        print "refreshToken:" + result.refreshToken

    def new_post(self, text):

        header = {
            "Content-Type": "application/json",
            "User-Agent" : self.UA,
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "postInfo" : { "readPermission" : { "type" : "ALL" } },
            "sourceType" : "TIMELINE",
            "contents" : { "text" : text }
        }

        r = requests.post(
            "http://" + self.host + "/mh/api/v24/post/create.json",
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

    def postPhoto(self,text,path):
        header = {
            "Content-Type": "application/json",
            "User-Agent" : self.UA,
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "postInfo" : { "readPermission" : { "type" : "ALL" } },
            "sourceType" : "TIMELINE",
            "contents" : { "text" : text ,"media" :  [{u'objectId': u'F57144CF9ECC4AD2E162E68554D1A8BD1a1ab0t04ff07f6'}]}
        }
        r = requests.post(
            "http://" + self.host + "/mh/api/v24/post/create.json",
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

    def like(self, mid, postid, likeType=1001):

        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "likeType" : likeType,
            "activityExternalId" : postid,
            "actorId" : mid
        }

        r = requests.post(
            "http://" + self.host + "/mh/api/v23/like/create.json?homeId=" + mid,
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

    def comment(self, mid, postid, text):
        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        payload = {
            "commentText" : text,
            "activityExternalId" : postid,
            "actorId" : mid
        }

        r = requests.post(
            "http://" + self.host + "/mh/api/v23/comment/create.json?homeId=" + mid,
            headers = header,
            data = json.dumps(payload)
        )

        return r.json()

    def activity(self, limit=20):

        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        r = requests.get(
            "http://" + self.host + "/tl/mapi/v21/activities?postLimit=" + str(limit),
            headers = header
        )
        return r.json()
    def getAlbum(self, gid):

        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct": self.channel_access_token,

        }

        r = requests.get(
            "http://" + self.host + "/mh/album/v3/albums?type=g&sourceType=TALKROOM&homeId=" + gid,
            headers = header
        )
        return r.json()
    def changeAlbumName(self,gid,name,albumId):
        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct": self.channel_access_token,

        }
        payload = {
            "title": name
        }
        r = requests.put(
            "http://" + self.host + "/mh/album/v3/album/" + albumId + "?homeId=" + gid,
            headers = header,
            data = json.dumps(payload),
        )
        return r.json()
    def deleteAlbum(self,gid,albumId):
        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct": self.channel_access_token,

        }
        r = requests.delete(
            "http://" + self.host + "/mh/album/v3/album/" + albumId + "?homeId=" + gid,
            headers = header,
            )
        return r.json()
    def getNote(self,gid, commentLimit, likeLimit):
        header = {
            "Content-Type" : "application/json",
            "X-Line-Mid" : self.mid,
            "x-lct": self.channel_access_token,

        }
        r = requests.get(
            "http://" + self.host + "/mh/api/v27/post/list.json?homeId=" + gid + "&commentLimit=" + commentLimit + "&sourceType=TALKROOM&likeLimit=" + likeLimit,
            headers = header
        )
        return r.json()

    def postNote(self, gid, text):
        header = {
            "Content-Type": "application/json",
            "User-Agent" : self.UA,
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }
        payload = {"postInfo":{"readPermission":{"homeId":gid}},
                   "sourceType":"GROUPHOME",
                   "contents":{"text":text}
                   }
        r = requests.post(
            "http://" + self.host + "/mh/api/v27/post/create.json",
            headers = header,
            data = json.dumps(payload)
            )
        return r.json()

    def getDetail(self, mid):
        header = {
            "Content-Type": "application/json",
            "User-Agent" : self.UA,
            "X-Line-Mid" : self.mid,
            "x-lct" : self.channel_access_token,
        }

        r = requests.get(
        "http://" + self.host + "/ma/api/v1/userpopup/getDetail.json?userMid=" + mid,
        headers = header
        )
        return r.json()

    def getHome(self,mid):
        header = {
                    "Content-Type": "application/json",
                    "User-Agent" : self.UA,
                    "X-Line-Mid" : self.mid,
                    "x-lct" : self.channel_access_token,
        }

        r = requests.get(
        "http://" + self.host + "/mh/api/v27/post/list.json?homeId=" + mid + "&commentLimit=2&sourceType=LINE_PROFILE_COVER&likeLimit=6",
        headers = header
        )
        return r.json()
    def getCover(self,mid):
        h = self.getHome(mid)
        objId = h["result"]["homeInfo"]["objectId"]
        return "http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + mid + "&oid=" + objId
    def createAlbum(self,gid,name):
        header = {
                    "Content-Type": "application/json",
                    "User-Agent" : self.UA,
                    "X-Line-Mid" : self.mid,
                    "x-lct" : self.channel_access_token,
        }
        payload = {
                "type" : "image",
                "title" : name
        }
        r = requests.post(
            "http://" + self.host + "/mh/album/v3/album?count=1&auto=0&homeId=" + gid,
            headers = header,
            data = json.dumps(payload)
        )
        return r.json()

    def createAlbum2(self,gid,name,path,oid):
        header = {
                    "Content-Type": "application/json",
                    "User-Agent" : self.UA,
                    "X-Line-Mid" : self.mid,
                    "x-lct" : self.channel_access_token,
        }
        payload = {
                "type" : "image",
                "title" : name
        }
        r = requests.post(
            "http://" + self.host + "/mh/album/v3/album?count=1&auto=0&homeId=" + gid,
            headers = header,
            data = json.dumps(payload)
        )
        #albumId = r.json()["result"]["items"][0]["id"]


        #h = {
        #            "Content-Type": "application/x-www-form-urlencoded",
        #            "User-Agent" : self.UA,
        #            "X-Line-Mid" : gid,
        #            "X-Line-Album" : albumId,
        #            "x-lct" : self.channel_access_token,
                    #"x-obs-host" : "obs-jp.line-apps.com:443",

        #}
        #print r.json()
        #files = {
        #    'file': open(path, 'rb'),
        #}
        #p = {
        #    "userid" : gid,
        #    "type" : "image",
        #    "oid" : oid,
        #    "ver" : "1.0"
        #}
        #data = {
        #    'params': json.dumps(p)
        #}
        #r = requests.post(
        #"http://obs-jp.line-apps.com/oa/album/a/object_info.nhn:443",
        #headers = h,
        #data = data,
        #files = files
        #)
        return r.json()
        #cl.createAlbum("cea9d61ba824e937aaf91637991ac934b","ss3ai","kawamuki.png")
