# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from io import StringIO
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,sys
import re,string,os
import os.path,sys,urllib,shutil,subprocess


cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

cl 
print u"login success"
reload(sys)
sys.setdefaultencoding('utf-8')
i = 0
c_text = """❂•••••••••••••AUTO LIKE BY•••••••••••••❂
                  https://line.me/R/ti/p/%40iya4481p
『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』"""

KAC = [cl]
mid = cl.getProfile().mid

Bots = [mid]
admin=["u54c7ad9784e86419f42e87f2aa39e1ec"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"❂••••••••••••••••••••••••••❂ https://line.me/R/ti/p/%40iya4481p『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』",
    "lang":"JP",
    "comment":"❂••••••••••••••••••••••••••❂ https://line.me/R/ti/p/%40iya4481p『⊰์◉⊱ᎢᎬᎪᎷ ᏴᏞᎪᏟᏦ ❂Ғ ᏀᎪᎷᎬᎡ⊰์◉⊱』",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
	"pnharfbot":{},
    "pname":{},
    "pro_name":{},
	"posts":True,
	}
	
wait2 = {
	'readMember':{},
	'readPoint':{},
	'ROM':{},
	'setTime':{}
    }
	
setTime = {}
setTime = wait2["setTime"]

res = {
    'num':{},
    'us':{},
    'au':{},
}


def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
	
def autolike(op):
    try:
		for posts in cl.activity(1)["result"]["posts"]:
			if wait["posts"] == True:
				if posts["postInfo"]["liked"] is False:
					cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
					print u"liked" + str(i)
					i += 1
    except Exception as e:
            print e
            
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u54c7ad9784e86419f42e87f2aa39e1ec":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
            elif msg.text in ["愛のプレゼント","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
#---------------------Fungsi Tag All Start---------------#
            elif msg.text in ["tagall","tag all","Crot","แท็ก"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#--------------------Fungsi Tag All Finish--------------------#
            elif "Crot" in msg.text:
                group = cl.getGroup(msg.to)
                k = len(group.members)//100
                for j in xrange(k+1):
                    msg = Message(to=msg.to)
                    txt = u''
                    s=0
                    d=[]
                    for i in group.members[j*100 : (j+1)*100]:
                        d.append({"S":str(s), "E" :str(s+8), "M":i.mid})
                        s += 9
                        txt += u'@Krampus\n'
                    msg.text = txt
                    msg.contentMetadata = {u'MENTION':json.dumps({"MENTIONEES":d})}
                    cl.sendMessage(msg) 
#-------------------------------------------------------------------#
#-----------------------------------------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
	for posts in cl.activity(1)["result"]["posts"]:
		if wait["posts"] == True:
			if posts["postInfo"]["liked"] is False:
				cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1002)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],c_text)
				print u"liked" + str(i)
				i += 1
