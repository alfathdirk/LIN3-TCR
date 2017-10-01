# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(token="ElSXrz6DloySYqhYBmn3.5hcU8I/+c6LAXfuIvU1giW.9X6jMxeBVDUNPewnAr7Zcs9QB5gBAtJsNIlcxkYTJ2Y=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="ElxNuZDOEW4iIOHNYJGf.s6yBVqcgAV2mWy3TWaT6xW.Bp750JRo4GjNwrWleSGIZLL0frSBhFdKg/vyCeROS0M=")
ki.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Gunakan dengan bijak keyword dibawah ini!

!Keberuntungan dan ketamvanan/kecantikan Anda Berlaku!


<※ Keyword  Ar-Har ※>

+[Id︎]
+[Mid]
+[Mid 「@」] By Tag
+[Me︎]
+[TL︎:「Text」]
+[Mc 「mid」]
+[K on/off]
+[Summon]
+[PING]
+[About Creator]
+[ngasyi ah]
+[cancel]
+[Arbot]
+[ArBot siapa?]
+[Welcome]
+[Hallo]
+[Ginfo]
+[Gurl]
+[Ini apa?]
+[Say 「text」]
+[Saran keyword]

[~!] Only Creator Bot [!~]

※[Tagall1]
※[Curl]
※[Ourl]
※[url]
※[url:「Group ID」]
※[Invite：「mid」]
※[Usir：「mid」]
※[jointicket]
※[Cancel]
※[Gn 「group name」]
※[Nk 「name」]
※[Usir Catatan]
※[Kill 「@」]
※[Catat 「@」] By Tag
※[Uncatat 「@」] By Tag
※[Catat] Share Contact
※[Uncatat] Share Contact
※[List Catatan]
※[Cek Catatan]
※[Cv ︎invite:「mid」]
※[Cv ︎rename:「name」]
※[Cv ︎gift]
※[Respo︎n]
※[Bot cancel]
※[Title:]



*ada beberapa key yang tidak bisa digunakan, itu dibuat untuk kepuasan tersendiri 😂✌️*


*jika ada sesuatu yang error segera hubungi sang Creator Ar-bot 📲 Ok😂👌*



Di Add ya line si creator
Kasihan, kesepian dia
Ok 😉
Creator : http://line.me/ti/p/~a.r.- """
KAC=[cl,ki]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid

Bots=[mid,Amid]
admin=["u308205dd6abcc4bec5da585db20ab076"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me 😄\nJangan lupa add si Creator juga ya\nhttp://line.me/ti/p/~a.r.-",
    "lang":"JP",
    "comment":"Thanks for add me 😊",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"Ar-Har",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":False,
    "ProtectQr":False,
    "ProtectGuest":False,
    "atjointicket":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

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
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if op.param2 not in admin:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        cl.kickoutFromGroup(op.param1,[op.param3])
                if op.param3 in admin:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param3])

        if op.type == 19:
#----------Fungsi Reinv Admin----------
                if op.param3 in admin:
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#--------------------------------------
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#----------Open Qr Kick Start----------
        if op.type == 10:
            if wait["ProtectQr"] == True:
                if op.param2 not in Bots:
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    cl.updateGroup(G)
#--------------------------------------

#----------Invite User Kick Start----------
        if op.type == 13:
            if wait["ProtectGuest"] == True:
                if op.param2 not in Bots:
                    random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#------------------------------------------

        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                ki.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada siapapun di List Catatan")

               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        ki.sendText(msg.to,"aded")


               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","Key","menu","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif ("Gn " in msg.text):
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Maaf, anda bukan admin.")
            elif ("Cv1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif "Usir " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Usir ","")
                    cl.kickoutFromGroup(msg.to,[midd])
                else:
                    cl.sendText(msg.to,"Sorry, lu bukan admin")
            elif "Cv1 kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Cv1 kick ","")
                    ki.kickoutFromGroup(msg.to,[midd])
            elif "Cv2 kick " in msg.text:
                midd = msg.text.replace("Cv2 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Undang " in msg.text:
                midd = msg.text.replace("Undang ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Cv1 invite " in msg.text:
                midd = msg.text.replace("Cv1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Cv1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tagall1"]:
                if msg.from_ in admin:
       		      group = cl.getGroup(msg.to)
		      mem = [contact.mid for contact in group.members]
		      for mm in mem:
               	          xname = cl.getContact(mm).displayName
	                  xlen = str(len(xname)+1)
                          msg.text = "@"+xname+" "
		          msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		          try:
                              cl.sendMessage(msg)

		          except Exception as error:
                     	      print error
            elif msg.text in ["Cv cancel","Bot cancel"]:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Link Grup Sudah Terbuka")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Maaf, anda bukan admin.")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 ourl","Cv1 link on"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"Sudah terbuka.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.from_ in admin:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                        ki.sendText(msg.to,"Link Grup Sudah Tertutup")
                    else:
                        cl.sendText(msg.to,"Sudah tertutup.")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sorry, lu bukan admin ArBot.")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 curl","Cv1 link off"]:
                if msg.from_ in admin:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"Sudah tertutup.")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"Info Grup Ini:")
                        ki.sendText(msg.to,"[Nama Grup]\n" + str(ginfo.name) + "\n[Id Grup]\n" + msg.to + "\n[Pembuat Grup]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nMembers:" + str(len(ginfo.members)) + "Anggota\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[Nama Grup]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[Pembuat grup]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ada yang error, pak!")
                        ki.sendText(msg.to,"Harap segera hubungi Si Creator!")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Cv1 mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif msg.text in ["Wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Galon"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                if msg.from_ in admin:
                   string = msg.text.replace("Cn ","")
                   if len(string.decode('utf-8')) <= 20:
                       profile = cl.getProfile()
                       profile.displayName = string
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
                if msg.toType == 2:
                   string = msg.text.replace("Cv1 rename ","")
                   if len(string.decode('utf-8')) <= 20:
                       profile_B = ki.getProfile()
                       profile_B.displayName = string
                       ki.updateProfile(profile_B)
                       ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","K on","Contact on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel"]:
                try:
                    strnum = msg.text.replace("Gcancel","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Sett"]:
                if msg.from_ in admin:
                     md = "Admin Setting:\n"
                     if wait["contact"] == True: md+=" Contact : on\n"
                     else: md+=" Contact : off\n"
                     if wait["autoJoin"] == True: md+=" Auto join : on\n"
                     else: md +=" Auto join : off\n"
                     if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                     else: md+= " Group cancel : off\n"
                     if wait["ProtectQr"] == True: md+=" Protect Qr : on\n"
                     else: md+=" Protect Qr : off\n"
                     if wait["ProtectGuest"] == True: md+=" Protect Guest : on\n"
                     else: md+=" Protect Guest : off\n"
                     if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
                     else: md+=" Auto leave : off\n"
                     if wait["timeline"] == True: md+=" Share : on\n"
                     else:md+=" Share : off\n"
                     if wait["autoAdd"] == True: md+=" Auto add : on\n"
                     else:md+=" Auto add : off\n"
                     if wait["commentOn"] == True: md+=" Comment : on\n"
                     else:md+=" Comment : off\n"
                     if wait["atjointicket"] == True: md+=" Auto Join Group by Ticket : on\n"
                     else:md+=" Auto Join Group by Ticket : off\n"
                     cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["ProtectQr on"]:
                if msg.from_ in admin:
                   if wait["ProtectQR"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQr on")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectQR"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"ProtectQr on")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectQr off"]:
                if msg.from_ in admin:
                   if wait["ProtectQR"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect QR Off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectQR"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect QR Off")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectGuest on"]:
                if msg.from_ in admin:
                   if wait["ProtectGuest"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest On")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectGuest"] == True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest On")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["ProtectGuest off"]:
                if msg.from_ in admin:
                   if wait["ProtectGuest"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest Off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["ProtectGuest"] == False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"Protect Guest Off")
                       else:
                           cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if msg.from_ in admin:
                   if wait["autoAdd"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"already on")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["autoAdd"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if msg.from_ in admin:
                   if wait["autoAdd"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"already off")
                       else:
                           cl.sendText(msg.to,"done")
                   else:
                       wait["autoAdd"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                if msg.from_ in admin:
                   wait["message"] = msg.text.replace("Message change: ","")
                   cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                if msg.from_ in admin:
                   wait["message"] = msg.text.replace("Message add: ","")
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"message changed")
                   else:
                       cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if msg.from_ in admin:
                   if wait["lang"] == "JP":
                       cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                   else:
                       cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                if msg.from_ in admin:
                   c = msg.text.replace("Comment:","")
                   if c in [""," ","\n",None]:
                       cl.sendText(msg.to,"message changed")
                   else:
                       wait["comment"] = c
                       cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                if msg.from_ in admin:
                   c = msg.text.replace("Add comment:","")
                   if c in [""," ","\n",None]:
                       cl.sendText(msg.to,"String that can not be changed")
                   else:
                       wait["comment"] = c
                       cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if msg.from_ in admin:
                   if wait["commentOn"] == True:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"already on")
                   else:
                       wait["commentOn"] = True
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if msg.from_ in admin:
                   if wait["commentOn"] == False:
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"already off")
                   else:
                       wait["commentOn"] = False
                       if wait["lang"] == "JP":
                           cl.sendText(msg.to,"done")
                       else:
                           cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Perbarui grup...%")
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Perbarui grup...%")
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if msg.from_ in admin:
                   if wait["clock"] == True:
                       cl.sendText(msg.to,"already on")
                   else:
                       wait["clock"] = True
                       now2 = datetime.now()
                       nowT = datetime.strftime(now2,"(%H:%M)")
                       profile = cl.getProfile()
                       profile.displayName = wait["cName"] + nowT
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
                if msg.from_ in admin:
                   if wait["clock"] == False:
                       cl.sendText(msg.to,"already off")
                   else:
                       wait["clock"] = False
                       cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
                if msg.from_ in admin:
                   n = msg.text.replace("Change clock ","")
                   if len(n.decode("utf-8")) > 13:
                       cl.sendText(msg.to,"changed")
                   else:
                       wait["cName"] = n
                       cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if msg.from_ in admin:
                   if wait["clock"] == True:
                       now2 = datetime.now()
                       nowT = datetime.strftime(now2,"(%H:%M)")
                       profile = cl.getProfile()
                       profile.displayName = wait["cName"] + nowT
                       cl.updateProfile(profile)
                       cl.sendText(msg.to,"Jam Update")
                   else:
                       cl.sendText(msg.to,"Please turn on the name clock")

            elif msg.text == "$set":
                if msg.from_ in admin:
                    cl.sendText(msg.to, "Check sider")
                    ki.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------

#-----------------------------------------------

            elif msg.text in ["All join"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Cv1 join"]:
                if msg.from_ in admin:
                     X = cl.getGroup(msg.to)
                     X.preventJoinByTicket = False
                     cl.updateGroup(X)
                     invsend = 0
                     Ti = cl.reissueGroupTicket(msg.to)
                     ki.acceptGroupInvitationByTicket(msg.to,Ti)
                     G = ki.getGroup(msg.to)
                     G.preventJoinByTicket = True
                     ki.updateGroup(G)
                     Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Cv2 join"]:
                if msg.from_ in admin:
                     X = cl.getGroup(msg.to)
                     X.preventJoinByTicket = False
                     cl.updateGroup(X)
                     invsend = 0
                     Ti = cl.reissueGroupTicket(msg.to)
                     ki.acceptGroupInvitationByTicket(msg.to,Ti)
                     G = cl.getGroup(msg.to)
                     G.preventJoinByTicket = True
                     ki.updateGroup(G)
                     Ticket = cl.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


#-----------------------------------------------

            elif msg.text in ["Bye bot","Bye 69"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 1"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye 2"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Cv1 @bye"]:
                if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass

#-----------------------------------------------
            elif msg.text in ["Summon"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.from_ in admin:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Ratakan" in msg.text:
                if msg.from_ in admin:
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    cl.sendText(msg.to,"Siap!")
                    ki.sendText(msg.to,"Memnyiapkan Proses Perataan.")
                    ki.sendText(msg.to,"Memulai Perataan.")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl,ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Grup sudah rata Bang Ar.")
                                ki.sendText(msg.to,"Siap melaksanakan perintah selanjutnya!")
            elif "Usir " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("Usir ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Succes Bang Ar")
                                    ki.sendText(msg.to,"👌")
            elif "Blacklist @" in msg.text:
                if msg.from_ in admin:
                   print "[Blacklist]ok"
                   _name = msg.text.replace("Blacklist @","")
                   _kicktarget = _name.rstrip(' ')
                   gs = ki2.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _kicktarget == g.displayName:
                           targets.append(g.mid)
                           if targets == []:
                               cl.sendText(msg.to,"Not found")
                           else:
                               for target in targets:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       k3.sendText(msg.to,"Succes Bang Ar")
                                   except:
                                       ki.sendText(msg.to,"Gagal Bang :'(")
            elif "Catat @" in msg.text:
                if msg.from_ in admin:
                    print "[Catat]ok"
                    _name = msg.text.replace("Catat @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Succes Tercatat Bang Ar")
                            except:
                                ki.sendText(msg.to,"Gagal tercatat Bang Ar :(")
                                ki.sendText(msg.to,"Sorry...")
            elif "Uncatat @" in msg.text:
                if msg.from_ in admin:
                    print "[Uncatat]ok"
                    _name = msg.text.replace("Uncatat @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Selamat!")
                                ki.sendText(msg.to,"Success dilepaskan dari catatan.")
                            except:
                                ki.sendText(msg.to,"Succes Bro!")
#-----------------------------------------------
            elif msg.text in ["On Bot"]:
                ki.sendText(msg.to,"On Bos  􀨁􀄻double thumbs up􏿿 􀜁􀅔Har Har�")
#-----------------------------------------------
            elif "Say " in msg.text:
                if msg.from_ in admin:
				bctxt = msg.text.replace("Say ","")
				cl.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["ArHar say hi"]:
                cl.sendText(msg.to,"Hi  􀜁􀅔Har Har􏿿")
#-----------------------------------------------

            elif msg.text in ["ArHar say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["ArHar say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Localhost@Tersakiti Family Room")
                ki.sendText(msg.to,"Jangan nakal ok!")
            elif msg.text in ["AKU","Aku","aku","Aku?","aku?"]:
                ki.sendText(msg.to,"Iya sayang")
                ki.sendText(msg.to,"Kamu doank")
                ki.sendText(msg.to,"Muacchh..♡♡♡")
            elif msg.text in ["Ban","ban","BAN","Banned"]:
                cl.sendText(msg.to,"Mau nge Ban?")
                ki.sendText(msg.to,"Bikin bot sendiri!")
                ki.sendText(msg.to,"Dasar Ndeso!")
            elif msg.text in ["Saran Keyword"]:
                cl.sendText(msg.to,"Mau kirim saran keyword?")
                ki.sendText(msg.to,"Kirim langsung aja ke Bang Ar(Si Creator) \nDengan mengisi format dibawah👇")
                ki.sendText(msg.to,"Saran keyword:\n\nQ:...[diisi]\nA:...[diisi]\nA:...[boleh diisi jika jawaban A ada lanjutannya]\nJumlah jawaban A:...[diisi]\n\n\nKirim langsung ke Bang Ar, tunggu beberapa hari dan saranmu akan masuk ke list keyword\n\n\nIsilah saranmu dengan sekreatif mungkin, tetapi yang wajar.")
            elif msg.text in ["Unicodes"]:
                cl.sendText(msg.to,"Harap berhati-hati")
                ki.sendText(msg.to,"4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.4.0.4.er.")

#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
            elif msg.text in ["...","..",".","Hh","hhh","hh","hhhhh"]:
                ki.sendText(msg.to,"Galau? Minum baygon aja :v")
            elif msg.text in [":v"]:
                ki.sendText(msg.to,"Ketawa bang?")
            elif msg.text in ["Laper","laper","Laver","laver"]:
                ki.sendText(msg.to,"Makan bang")
            elif msg.text in ["Hallo","hallo","Halo","halo"]:
                ki.sendText(msg.to,"Ya, ada yang bisa Ar-Bot bantu?")
            elif msg.text in ["Error","error","Eror","eror","Errno"]:
                ki.sendText(msg.to,"Ada yang error?")
                ki.sendText(msg.to,"Hubungi si Creator Ar-Har aja\nhttp://line.me/ti/p/~a.r.-")
            elif msg.text in ["Hmm","hmm","Hm","hm"]:
                cl.sendText(msg.to,"Ada Apa?")
                ki.sendText(msg.to,"Ada Apa Dengan Kamu?")
            elif msg.text in ["Ini apa?","Itu apa?","ini apa?","itu apa?"]:
                cl.sendText(msg.to,"Ini ArHar.👦")
                ki.sendText(msg.to,"Ini Ibu ArHar.👩")
                cl.sendText(msg.to,"Ini Bapak ArHar.👨")
            elif msg.text in ["Ar Har siapa?","ArHar siapa?","ar har siapa?","arhar siapa?","Itu siapa?","itu siapa?","Itu saha"]:
                ki.sendText(msg.to,"Aku ArBot kak, panggil aja ArBot :v\nAku dibuat oleh Bang Ar\nhttp://line.me/ti/p/~-a.r.i")
            elif msg.text in ["ngasyi ah?","ngasyi ah","Ngasyi ah","Ngasyi ah?"]:
                ki.sendText(msg.to,"Bang, kalo ngomong jangan disingkat-singkat")
                ki.sendText(msg.to,"Pakai Bahasa Indonesia yang wajar aja bang, lebih mudah dimengerti orang lain")
            elif msg.text in ["sepi","Sepi"]:
                ki.sendText(msg.to,"Karena gk rame")
            elif msg.text in ["Anjing","anjing","njing","Anjeng","anjeng","njeng","Njir","njir","Njeng"]:
                ki.sendText(msg.to,"Kalem Euy")
                ki.sendText(msg.to,"Kalem, jangan ngegas :v")
            elif msg.text in ["About Creator","About creator","about creator"]:
                ki.sendText(msg.to,"About Creator:\nCreator ArHar itu si Bang Ar\nhttp://line.me/ti/p/~a.r.- \n\n Fakta tentang creator:\n-Masih Single\n-Wajah tamvan\n-Tubuh atletik + tinggi\n-Hobby baca buku bekas(bukan bekas dijilat)\n-Suka ngelawak tapi Garing\n-Sangat anti kekerasan")

#-----------------------------------------------

            elif msg.text in ["ArHar","arhar"]:
                ki.sendText(msg.to,"Hadir✋􀜁􀅔Har Har�")
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Loading...")
                elapsed_time = time.time() - start
                ki.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            elif msg.text in ["Catat"]:
                if msg.from_ in admin:
                     wait["wblacklist"] = True
                     cl.sendText(msg.to,"send contact")
                     ki.sendText(msg.to,"send contact")
            elif msg.text in ["Uncatat"]:
                if msg.from_ in admin:
                     wait["dblacklist"] = True
                     cl.sendText(msg.to,"send contact")
                     ki.sendText(msg.to,"send contact")
            elif msg.text in ["List Catatan"]:
                if msg.toType == 2:
                  if wait["blacklist"] == {}:
                      cl.sendText(msg.to,"nothing")
                      ki.sendText(msg.to,"Tak ada siapapun bos.")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    ki.sendText(msg.to,mc)
            elif msg.text in ["Cek Catatan"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kick catatan"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        ki.sendText(msg.to,"Tak ada siapapun bos.")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                        ki.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist harus di usir!")
                    ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    cl.sendText(msg.to,"Betul")
                    cl.sendText(msg.to,"Betul")
                    cl.sendText(msg.to,"Betul")
            elif msg.text in ["Bersihkan"]:
                if msg.from_ in admin:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "Acak:" in msg.text:
                if msg.from_ in admin:
                    strnum = msg.text.replace("Acak:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumchat" in msg.text:
                try:
                    albumtags = msg.text.replace("albumchat","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakechat" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakechat","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
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

def autolike():
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ArHar\nCreator 👇.\n\nhttp://line.me/ti/p/~a.r.-")
            ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by ArQyu\nCreator 👇.\n\nhttp://line.me/ti/p/~a.r.-")
            print "Like"
          except:
            pass
        else:
            print "Already Liked"
     time.sleep(100)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

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
