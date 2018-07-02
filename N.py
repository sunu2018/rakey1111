# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE()
#line = LINE()
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

#ki = LINE()
#ki = LINE()
#ki.log("Auth Token : " + str(ki.authToken))
#ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

#kk = LINE()
#kk = LINE()
#kk.log("Auth Token : " + str(kk.authToken))
#kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

#kc = LINE()
#kc = LINE()
#kc.log("Auth Token : " + str(kc.authToken))
#kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

#ke = LINE()
#ke = LINE()
#ke.log("Auth Token : " + str(ke.authToken))
#ke.log("Timeline Token : " + str(ke.tl.channelAccessToken))

#ki1 = LINE("EuMog9y5XK0HpLVD5NQd.1nbyMEq08x6C7rz2+Bti7q.AbZpd2NL+U67ENU7foUKRyx+rbCvL7JfxCSIgFep34E=")
#ki2 = LINE("EuEI1iUJoxtcMCdjAwXa.O9c5p841tRUgzA9d0PcAkG.BmkT3cVrFLnqV5SDsGHtV2R+Bwk4tH7HpLYcJY1FbCk=")
#ki3 = LINE("EuB2nqViXB9yVC6Hv4id.dCZhkZtrJsP18XdGxTjDlq.lfF8ng308Ftvk0pwuhDN9xyhwzsJdtF8Rc5kytYYCd4=")
#ki4 = LINE("EuzzT05VEW5hnfk4S6v3.NONcEvn2cxU/zuRhr3ZHOW.1EusstaqkeTioe+S1j8fscJMoh2+NTFjrt/yDiclAp0=")

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

#ki1MID = ki1.profile.mid
#ki1Profile = ki1.getProfile()
#ki1Settings = ki1.getSettings()

#ki2MID = ki2.profile.mid
#ki2Profile = ki2.getProfile()
#ki2Settings = ki2.getSettings()

#ki3MID = ki3.profile.mid
#ki3Profile = ki3.getProfile()
#ki3Settings = ki3.getSettings()

#ki4MID = ki4.profile.mid
#ki4Profile = ki4.getProfile()
#ki4Settings = ki4.getSettings()


oepoll = OEPoll(ki4)
oepoll = OEPoll(ki3)
oepoll = OEPoll(ki2)
oepoll = OEPoll(ki1)
oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]#,ki1,ki2,ki3,ki4]
#Exc = [ki1,ki2,ki3,ki4]
lineMID = line.getProfile().mid
#ki1MID = ki1.getProfile().mid
#ki2MID = ki2.getProfile().mid
#ki3MID = ki3.getProfile().mid
#ki4MID = ki4.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]#,ki1MID,ki2MID,ki3MID,ki4MID]
Family=["u9ed31efc986199adedb27386c9b1f458",lineMID]#,ki1MID,ki2MID,ki3MID,ki4MID]
admin=['u9ed31efc986199adedb27386c9b1f458',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
settings = {
    "autoAdd": True,
    "autoJoin": False,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": False,
    "autoRead": False,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "kickMention": False,
    "potoMention": True,
    "lang":"JP",
    "Wc": False,
    "Lv": False,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": True,
    "cName":"",
    "cNames":"nunu_kap123",
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message":"บัญชีนี้ได้การป้องกันโดย ꧁🍁✟ℓຫຼี้छゆຸ۞🍁꧂ และ ꧁🌸ℓຫຼี้छՃิ🌸꧂  ระบบได้ทำการบล็อคคุณอัตโนมัติเนื่องจากคุณยังไม่ได้ยืนยันตัวตนกับผู้สร้างบอท\nสามารถยืนตัวตนได้ง่ายโดยการพิมunblockกับPZGruardระบบจะทำการปลดบล็อคท่านโดยอัตโนมัต",
    "comment":"แอดมาทุระกรุณาแจ้งไห้ทราบด้วย ขอบคุณ",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": True,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoAdd": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 
dangerMessage = ["cleanse","group cleansed.","mulai",".winebot",".kickall","mayhem","kick on","makasih :d","!kickall","nuke","บิน",".???","งงไปดิ","บินไปดิ","เซลกากจัง","ครับ","ok","ขอคลิปหน่อยครับ"]

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
 
def myhelp():
    myHelp = " ╭════ บ อ ท ท ด ล อ ง น้ อ ง สุ " + "\n" \
                  "║About" + "\n" + \
                  "║Help1" + "\n" + \
                  "║Help2" + "\n" + \
                  "║Help3" + "\n" + \
                  "║Help4" + "\n" + \
                  "║Help5" + "\n" + \
                  "║Help6" + "\n" + \
                  "║textTospeech" + "\n" + \
                  "║Languange" + "\n" + \
                  "║Me" + "\n" + \
                  "║Mymid" + "\n" + \
                  "║Myname" + "\n" + \
                  "║Mybio" + "\n" + \
                  "║Mypict" + "\n" + \
                  "║Mycover" + "\n" + \
                  "║Myvideo" + "\n" + \
                  "║Mid" + "\n" + \
                  "║Name" + "\n" + \
                  "║Bio" + "\n" + \
                  "║Pict" + "\n" + \
                  "║Cover" + "\n" + \
                  "║Video" + "\n" + \
                  "║Copy" + "\n" + \
                  "║Restore" + "\n" + \
                  "║Mimic on/off" + "\n" + \
                  "║MimicList" + "\n" + \
                  "║MimicAdd" + "\n" + \
                  "║MimicDel" + "\n" + \
                  "║Broadcastvoice" + "\n" + \
                  "║Cbroadcastvoice" + "\n" + \
                  "║Restart" + "\n" + \
                  "║Runtime" + "\n" + \
                  "╰════"
    return myHelp

def listgrup():
    listGrup = "╭════HelpGroup " + "\n" + \
                  "║GroupCreator" + "\n" + \
                  "║GroupId" + "\n" + \
                  "║GroupName" + "\n" + \
                  "║GroupPicture" + "\n" + \
                  "║GroupList" + "\n" + \
                  "║GroupMemberList" + "\n" + \
                  "║GroupInfo" + "\n" + \
                  "║Url" + "\n" + \
                  "║Link on/off" + "\n" + \
                  "║Gurl" + "\n" + \
                  "║Friendlist" + "\n" + \
                  "║Blocklist" + "\n" + \
                  "║Friendlist mid" + "\n" + \
                  "║Invite:gcreator" + "\n" + \
                  "║Spam on/off" + "\n" + \
                  "║Reject inv" + "\n" + \
                  "║Allban" + "\n" + \
                  "║Grouplist" + "\n" + \
                  "║Blist" + "\n" + \
                  "║Mention" + "\n" + \
                  "║Lurking on" + "\n" + \
                  "║Lurking off" + "\n" + \
                  "║Lurking reset" + "\n" + \
                  "║Lurking" + "\n" + \
                  "║Invite" + "\n" + \
                  "║uninstall" + "\n" + \
                  "║Kick" + "\n" + \
                  "║Ban:on" + "\n" + \
                  "║Unban:on" + "\n" + \
                  "╰════"
    return listGrup

def socmedia():
    socMedia = "╭════HelpMedia " + "\n" + \
                  "║Instagram" + "\n" + \
                  "║Fotoig" + "\n" + \
                  "║Youtube" + "\n" + \
                  "║Music" + "\n" + \
                  "║Lyric" + "\n" + \
                  "║ScreenshootWebsite" + "\n" + \
                  "║Film:" + "\n" + \
                  "║Kalender" + "\n" + \
                  "║CheckDate" + "\n" + \
                  "║Textig" + "\n" + \
                  "║Wikipedia" + "\n" + \
                  "║Urban" + "\n" + \
                  "║Anime" + "\n" + \
                  "║Image" + "\n" + \
                  "║Pornhub" + "\n" + \
                  "╰════"
    return socMedia
    
def helpset():
    helpSet = "╭════HelpMySet " + "\n" + \
    "║ᴍʏ sᴇʟғ" + "\n" + \
    "║sᴏᴄᴍᴇᴅɪᴀ" + "\n" + \
    "║ʟɪsᴛ ɢʀᴜᴘ" + "\n" + \
    "║ʟɪsᴛ ᴘʀᴏᴛᴇᴄᴛ" + "\n" + \
    "║ʟɪsᴛ ᴋɪᴄᴋᴇʀ" + "\n" + \
    "║sᴛᴀᴛᴜs" + "\n" + \
    "║ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ" + "\n" + \
    "║ʟɪsᴛ ᴛʀᴀɴsʟᴀᴛᴇ" + "\n" + \
    "╰════"
    return helpSet 

def helpkicker():
    helpKicker = "╭════HelpKicker " + "\n" + \
    "║K1 kick" + "\n" + \
    "║K2 kick" + "\n" + \
    "║K3 kick" + "\n" + \
    "║K1 invite" + "\n" + \
    "║K2 inv" + "\n" + \
    "║K3 vit" + "\n" + \
    "║K1 tag" + "\n" + \
    "║K1gruplist" + "\n" + \
    "║K2listgrup" + "\n" + \
    "║K3listrom" + "\n" + \
    "║Cleanse" + "\n" + \
    "║Scan blacklist" + "\n" + \
    "║cb" + "\n" + \
    "║Nameall:" + "\n" + \
    "║Bioall" + "\n" + \
    "╰════"
    return helpKicker
    
def helpsetting():
    helpSetting = "╭════ป้ อ ง กั น " + "\n" + \
    "║Protect on/off" + "\n" + \
    "║Cancel pro on/off" + "\n" + \
    "║Invit pro on/off" + "\n" + \
    "║Link pro on/off" + "\n" + \
    "║Join pro on/off" + "\n" + \
    "║Proall on/off" + "\n" + \
    "║Autojoin on/off" + "\n" + \
    "║Autoadd on/off" + "\n" + \
    "║Autoleave on/off" + "\n" + \
    "║Autoread on/off" + "\n" + \
    "║Tag on/off" + "\n" + \
    "║Selfbot on/off" + "\n" + \
    "║Tag2 on/off" + "\n" + \
    "║Checksticker on/off" + "\n" + \
    "║Sider on/off" + "\n" + \
    "║Welcomemessage on/off" + "\n" + \
    "║Leavemessage on/off" + "\n" + \
    "╰════"
    return helpSetting
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                line.blockContact(op.param1)
                ki1.blockContact(op.param1)
                ki2.blockContact(op.param1)
                ki3.blockContact(op.param1)
                ki4.blockContact(op.param1)  
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
#        if op.type == 24:
#            if settings["autoLeave"] == True:
#                line.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
                if ".say " in msg.text.lower():
                    spl = re.split(".say ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'help1':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))
                elif text.lower() == 'help2':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'help3':
                    helpKicker = helpkicker()
                    line.sendMessage(to, str(helpKicker))
                elif text.lower() == 'help4':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'help5':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == 'help6':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
#                elif text.lower() == 'texttospeech':
 #                   helpTextToSpeech = helptexttospeech()
 #                   line.sendMessage(to, str(helpTextToSpeech))
  #              elif text.lower() == 'languange':
  #                  helpLanguange = helplanguange()
  #                  line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == 'speed':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")						
                elif text.lower() == 'รีบอท':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "ue92d89cc346863c640b8a7855e14abd7"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[ ꧁🌸ℓຫຼี้छՃิ🌸꧂ ]"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ]"
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[ ꧁🍁✟ℓຫຼี้छゆຸ۞🍁꧂ ]"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔════[ Status ]═════┓"
                        if settings["autoAdd"] == True: ret_ += "\n╠ รับแอดออโต้ ✔"
                        else: ret_ += "\n╠ รับแอดออโต้    ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ เข้าห้องออโต้    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ยกเลิกเชิญกลุ่มเมื่อมีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ยกเลิกเชิญกลุ่ม    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ออกแชทรวม ✔"
                        else: ret_ += "\n╠ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ อ่านออโต้ ✔"
                        else: ret_ += "\n╠ อ่านออโต้   ✘ "				
                        if settings["checkSticker"] == True: ret_ += "\n╠ Sticker ✔"
                        else: ret_ += "\n╠ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ แสดงภาพคนแทค ✘ "						
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ กันเชิญ ✔"
                        else: ret_ += "\n╠ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ กันยกเชิญ ✔"
                        else: ret_ += "\n╠ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ป้องกัน ✔"
                        else: ret_ += "\n╠ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✘ "						
                        ret_ += "\n╚════[ Status ]═════┛"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == 'รับแอดออโต้ on':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "เปิดรับแอดออโต้ แล้ว.")
                elif text.lower() == 'รับแอดออโต้ off':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "ปิดรับแอดออโต้ แล้ว.")
                elif text.lower() == 'เข้าห้องออโต้ on':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "เปิดเข้าห้องออโต้ แล้ว.")
                elif text.lower() == 'เข้าห้องออโต้ off':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "ปิดเข้าห้องออโต้ แล้ว.")
                elif "Gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("Gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,strnum + " สมาชิกในกลุ่มจะปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,"Value is wrong")
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == 'autoleave on':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "Autoleave enabled.")
                elif text.lower() == 'autoleave off':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "Autoleave disabled.")
                elif text.lower() == 'autoread on':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Autoread message enabled.")
                elif text.lower() == 'autoread off':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Autoread message disabled.")
                elif text.lower() == 'sticker on':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Check sticker enabled.")
                elif text.lower() == 'sticker off':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Check sticker disabled.")                
#==============================================================================#
                elif text.lower() == 'me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == 'creator':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "ue92d89cc346863c640b8a7855e14abd7")
                elif text.lower() == 'mymid':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == 'myname':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypict':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideo':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("me "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("name "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("pict "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("video "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("cover "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("copy "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            line.cloneContactProfile(contact)
                            line.sendMessage(msg.to, "😊😊")
                        except:
                            line.sendMessage(msg.to, "😊😊")
                            
                elif text.lower() == 'backup':
                    try:
                        lineProfile.displayName = str(myProfile["displayName"])
                        lineProfile.statusMessage = str(myProfile["statusMessage"])
                        lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                        line.updateProfileAttribute(8, lineProfile.pictureStatus)
                        line.updateProfile(lineProfile)
                        line.sendMessage(msg.to, "Berhasil restore profile")
                    except:
                        line.sendMessage(msg.to, "Gagal restore profile")
						
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")
#==============================================================================#
                elif text.lower() == 'groupcreator':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "Itu Pembuat Groupnya")
                elif text.lower() == 'groupid':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ID GROUP \n" + gid.id)
                elif text.lower() == 'grouppicture':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "Name Group -> \n" + gid.name)
                elif text.lower() == 'url':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "Link Qr Group\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == 'link on':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "Link Qr to open")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to open")
                elif text.lower() == 'link off':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "Link Qr to closed.")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "Link Qr to closed.")
                elif text.lower() == 'groupinfo':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ Group Info ]"
                    ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                    ret_ += "\n╠ ID Group : {}".format(group.id)
                    ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                    ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠ Group Qr : {}".format(gQr)
                    ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))

                elif text.lower() == 'k1gruplist':
                        groups = ki1.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki1.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki1.sendMessage(to, str(ret_))

                elif text.lower() == 'k2listgrup':
                        groups = ki2.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki2.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki2.sendMessage(to, str(ret_))

                elif text.lower() == 'k3listroom':
                        groups = ki3.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki3.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki3.sendMessage(to, str(ret_))
						
                elif text.lower() == 'k4listroom':
                        groups = ki4.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = ki4.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        ki4.sendMessage(to, str(ret_))					
                elif ".invitetocall" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")	
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass	
                elif msg.text.lower() == ".getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".info " in msg.text.lower():
                    spl = re.split(".info ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            line.sendMessage(msg)
                elif "|!" in msg.text:
                    spl = msg.text.split("|!")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id)	
                elif ".denyall" in msg.text.lower():
                    spl = re.split(".denyall",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif ".remove " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".bye " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == ".myid":
                    line.sendText(msg.to,user1)
                elif msg.text.lower().startswith(".mentionall"):
                    data = msg.text[len(".mentionall"):].strip()
                    if data == "":
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "<":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count > mentargs:
                                break
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == ">":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        if mentargs >= 0:
                            strt = len(str(mentargs)) + 2
                        else:
                            strt = len(str(count)) + 2
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count < mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                    elif data[0] == "=":
                        mentargs = int(data[1:].strip())
                        group = line.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members if contact.mid != user1]
                        cb = ""
                        cb2 = ""
                        count = 1
                        akh = int(0)
                        cnt = 0
                        for md in nama:
                            if count != mentargs:
                                count += 1
                                continue
                            akh = akh + len(str(count)) + 2 + 5
                            strt = len(str(count)) + 2
                            cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                            strt = strt + len(str(count+1)) + 2 + 6
                            akh = akh + 1
                            cb2 += str(count)+". @name\n"
                            cnt = cnt + 1
                            if cnt == 50:
                                cb = (cb[:int(len(cb)-1)])
                                cb2 = cb2[:-1]
                                msg.contentType = 0
                                msg.text = cb2
                                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                                try:
                                    line.sendMessage(msg)
                                except:
                                    line.sendText(msg.to,"[[NO MENTION]]")
                                cb = ""
                                cb2 = ""
                                strt = len(str(count)) + 2
                                akh = int(0)
                                cnt = 0
                            count += 1
                        cb = (cb[:int(len(cb)-1)])
                        cb2 = cb2[:-1]
                        msg.contentType = 0
                        msg.text = cb2
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                        try:
                            line.sendMessage(msg)
                        except:
                            line.sendText(msg.to,"[[NO MENTION]]")
                elif ".tx " in msg.text.lower():
                    spl = re.split(".tx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        line.kedapkedip(msg.to,spl[1])
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".join " in msg.text.lower():
                    spl = re.split(".join ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))	
                elif msg.text.lower().startswith(".ctt "):
                    try:
                        text = msg.text.split(" ",1)[1]
                        headers = {
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
                        }
                        data = {
                        "q":text
                        }
                        conv = BeautifulSoup(requests.post("http://lullar-de-2.appspot.com/",headers=headers,data=data).content,"html.parser").find("span",attrs={"style":"font-size:40px"}).text
                        if msg.toType != 0:
                                ki2.sendText(msg.to,"Conversion:\n"+conv)
                        else:
                                ki2.sendText(msg.from_,"Conversion:\n"+conv)
                    except Exception as e:
                        print(e)						
                elif msg.text.lower().startswith("pz:gac "):
                    pnum = re.split("pz:gac ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                ki2.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                ki2.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                ki2.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                ki2.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                ki2.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                ki2.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")

                if msg.text.lower() == ".me":
                    msg.contentType = 13
                    msg.text = None
                    msg.contentMetadata = {'mid': user1}
                    line.sendMessage(msg)
                if msg.text.lower() == ".gift":
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
                if ".gift " in msg.text.lower():
                    red = re.compile(re.escape('.gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)						
#==============================================================================#
                elif text.lower() == 'mention':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//500
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*500 : (a+1)*500]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))          

                elif text.lower() == 'k1 tag':
                    group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members if contact.mid != lineMID]
                    k = len(nama)//500
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*500 : (a+1)*500]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        ki1.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        ki1.sendMessage(to, "จำนวน {} คน".format(str(len(nama))))          

                elif text.lower() == 'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'lurking':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~☆นุนุ☆~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
#==============================================================================#   
                elif "Broadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Bcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getGroupIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Cbroadcastvoice " in msg.text:
                    bctxt = msg.text.replace("Cbcvoice ", "")
                    bc = (".Bdw.. Ini adalah Broadcast.. Salam Owner ARDIAN PURNAMA.. by. RFU boot sekawan")
                    cb = (bctxt + bc)
                    tts = gTTS(cb, lang='id', slow=False)
                    tts.save('tts.mp3')
                    n = line.getAllContactIdsJoined()
                    for manusia in n:
                        line.sendAudio(manusia, 'tts.mp3')

                elif "Wikipedia " in msg.text:
                      try:
                          wiki = msg.text.lower().replace("Wikipedia ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          line.sendMessage(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  line.sendText(msg.to, pesan)
                              except Exception as e:
                                  line.sendMessage(msg.to, str(e))

                elif "Film:" in msg.text:
                    proses = msg.text.split(":")
                    get = msg.text.replace(proses[0] + ":","")
                    getfilm = get.split()
                    title = getfilm[0]
                    tahun = getfilm[1]
                    r = requests.get('http://www.omdbapi.com/?t='+title+'&y='+tahun+'&plot=full&apikey=4bdd1d70')
                    start = time.time()
                    data=r.text
                    data=json.loads(data)
                    hasil = "Informasi \n" +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                    hasil += "\n\n " +str(data["Plot"])
                    hasil += "\n\nDirector : " +str(data["Director"])
                    hasil += "\nActors   : " +str(data["Actors"])
                    hasil += "\nRelease : " +str(data["Released"])
                    hasil += "\nGenre    : " +str(data["Genre"])
                    hasil += "\nRuntime   : " +str(data["Runtime"])
                    path = data["Poster"]
                    line.sendImageWithURL(msg.to, str(path))
                    line.sendMessage(msg.to,hasil)

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    line.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        line.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    line.sendMessage(to, str(ret_))
                
                elif "instagram" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ จำนวน Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            line.sendImageWithURL(to, str(path))
                            line.sendMessage(to, str(ret_))
                        except:
                            line.sendMessage(to, "Pengguna tidak ditemukan")
                elif "fotoig" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1):
                            print(('send foto : ', count))
                            r = x.get(profile, params={'max_id': end_cursor})                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                print((node['display_src']))
                                line.sendImageWithURL(msg.to,node['display_src'])
                elif "image" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "anime" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            line.sendImageWithURL(to, str(path))
                elif "youtube" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html.parser")
                        ret_ = "╔══[ ผลการค้นหา ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ จำนวนที่พบ {} ]".format(len(datas))
                        line.sendMessage(to, str(ret_))

                elif msg.text in ["Cctv on"]:
                    try:
                        del RfuCctv['point'][msg.to]
                        del RfuCctv['sidermem'][msg.to]
                        del RfuCctv['cyduk'][msg.to]
                    except:
                        pass
                    RfuCctv['point'][msg.to] = msg.id
                    RfuCctv['sidermem'][msg.to] = ""
                    RfuCctv['cyduk'][msg.to]=True
                    line.sendMessage(msg.to,"Cctv on Ready")
                elif msg.text in ["Cctv off"]:
                    if msg.to in RfuCctv['point']:
                        RfuCctv['cyduk'][msg.to]=False
                        line.sendText(msg.to, RfuCctv['sidermem'][msg.to])
                    else:
                        line.sendMessage(msg.to, "Cctv Already Off")

                elif text.lower() == 'selfbot off':
                    line.sendMessage(receiver, 'หยุดการทำงานเซลบอทเรียบร้อย')
                    print ("Selfbot Off")
                    exit(1)

                elif text.lower() == 'friendlist':
                    contactlist = line.getAllContactIds()
                    kontak = line.getContacts(contactlist)
                    num=1
                    msgs="🎎List Friend🎎"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n🎎List Friend🎎\n\nTotal Teman : %i" % len(kontak)
                    line.sendMessage(msg.to, msgs)

                elif msg.text in ["Blocklist"]: 
                    blockedlist = line.getBlockedContactIds()
                    kontak = line.getContacts(blockedlist)
                    num=1
                    msgs="═════Daftar Akun Yang di Blocked═════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n════════List Blocked════════\n\nTotal Blocked : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text in ["Friendlist mid"]: 
                    gruplist = line.getAllContactIds()
                    kontak = line.getContacts(gruplist)
                    num=1
                    msgs="═════════List FriendMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                    line.sendMessage(receiver, msgs)

                elif msg.text.lower() == 'gurl':
                	if msg.toType == 2:
                         g = line.getGroup(receiver)
                         line.updateGroup(g)
                         gurl = line.reissueGroupTicket(receiver)
                         line.sendMessage(receiver,"╔══════════════┓\n╠❂line://ti/g/" + gurl + "\n╠\n╠❂Link Groupnya Tanpa Buka Qr\n╚══════════════┛")

                elif msg.text == "Pornhub":
                	line.sendMessage(receiver,">nekopoi.host\n>sexvideobokep.com\n>memek.com\n>pornktube.com\n>faketaxi.com\n>videojorok.com\n>watchmygf.mobi\n>xnxx.com\n>pornhd.com\n>xvideos.com\n>vidz7.com\n>m.xhamster.com\n>xxmovies.pro\n>youporn.com\n>pornhub.com\n>youjizz.com\n>thumzilla.com\n>anyporn.com\n>brazzers.com\n>redtube.com\n>youporn.com")

                elif msg.text.lower() == 'invite:gcreator':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Type👉 Invite Pembuat Group Succes")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "Pembuat Group Sudah di dalam")

                elif msg.text in ["/uninstall"]:
                    if msg.toType == 2:
                        ginfo = line.getGroup(receiver)
                        try:
                            line.leaveGroup(receiver)
                            ki1.leaveGroup(receiver)
                            ki2.leaveGroup(receiver)
                            ki3.leaveGroup(receiver)
                            ki4.leaveGroup(receiver)	
                            ki5.leaveGroup(receiver)
                            ki6.leaveGroup(receiver)
                            ki7.leaveGroup(receiver)
                            ki8.leaveGroup(receiver)
                            ki9.leaveGroup(receiver)
                            ki10.leaveGroup(receiver)				
                        except:
                            pass

                elif msg.text in ["Tagimage on","Tag2 on"]:
                        settings['potoMention'] = True
                        line.sendMessage(msg.to,"Respon enabled.")
                
                elif msg.text in ["Tagimage off","Tag2 off"]:
                        settings['potoMention'] = False
                        line.sendMessage(msg.to,"Respon disabled.")

                elif msg.text in ["Respontag on","Tag on","My respon on","Respon:on"]:
                    settings["detectMention"] = True
                    line.sendMessage(msg.to,"AutoRespon enabled.")
                
                elif msg.text in ["Respontag off","Tag off","My respon off","Respon:off"]:
                    settings["detectMention"] = False
                    line.sendMessage(msg.to,"Autorespon disabled.")

                elif msg.text.lower().startswith("textig "):
                    sep = msg.text.split(" ")
                    textnya = msg.text.replace(sep[0] + " ","")
                    urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                    line.sendImageWithURL(msg.to, urlnya)

                elif "kedip " in msg.text:
                    txt = msg.text.replace("kedip ", "")
                    t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                    t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                    line.sendMessage(msg.to, t1 + txt + t2)						
                elif msg.text in ["K1 Siri"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki1.getGroup(msg.to)
                        if ki1MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki1.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki1.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
										
                elif msg.text in ["K2 Siri"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki2.getGroup(msg.to)
                        if ki2MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki2.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki2.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["K3 Siri"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki3.getGroup(msg.to)
                        if ki3MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki3.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki3.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                elif msg.text in ["K4 Siri"]:
                    if msg.toType == 2:
                        print("Kick Siri")
                        x = ki4.getGroup(msg.to)
                        if ki4MID in [i.mid for i in x.members]:
                            sirilist = [i.mid for i in x.members if any(word in i.displayName for word in ["Doctor.A","Eliza","Parry","Rakko","しりちゃん"]) or i.displayName.isdigit()]
                            if sirilist == []:
                                ki4.sendText(msg.to,"ไม่พบสิริอยู่ในกลุ่ม.")
                            for target in sirilist:
                                try:
                                    ki4.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass									
                elif msg.text in ["Inviteuser"]:
                        settings["winvite"] = True
                        line.sendMessage(msg.to,"send a contact to invite user")                            
                elif msg.text.lower() == ".invitecancel":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            line.cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == ".invitecancel2":
                    if msg.toType == 2:
                        group = line.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            random.choice(Exc).cancelGroupInvitation(msg.to,[i])
                elif msg.text.lower() == "on":
                    line.sendText(msg.to,(str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" days, ")[1].split(":")[0]+" ชั่วโมง " if "days" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[0]+" วัน "+str(datetime.datetime.now() - start_runtime)[:-7].split(" day, ")[1].split(":")[0]+" ชั่วโมง " if "day" in str(datetime.datetime.now() - start_runtime) else str(datetime.datetime.now() - start_runtime)[:-7].split(":")[0]+" ชั่วโมง ")+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[1]+" นาที "+str(datetime.datetime.now() - start_runtime)[:-7].split(":")[2]+" วินาที")
#=============COMMAND KICKER===========================#
                elif msg.text in ["cb"]:
                    settings["blacklist"] = {}
                    line.sendMessage(msg.to,"ทำการลบัญชีดำทั้งหมดเรียร้อย")
                    print ("Clear Ban")

                elif text.lower() == 'มาหำ':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        group.preventedJoinByTicket = False
                        line.updateGroup(group)
                        invsend = 0
                        ticket = line.reissueGroupTicket(to)
                        ki1.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki2.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki3.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)
                        ki4.acceptGroupInvitationByTicket(to,format(str(ticket)))
                        time.sleep(0.01)                 
                        group.preventedJoinByTicket = True
                        line.updateGroup(group)
                        print ("Kicker Join")

                elif 'kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               random.choice(Rfu).kickoutFromGroup(msg.to,[target])      
                               print ("Rfu kick User")
                           except:
                               random.choice(Rfu).sendMessage(msg.to,"Limit kaka 😫")

                elif 'kill' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.kickoutFromGroup(msg.to,[target])             
                               print ("Sb Kick User")
                           except:
                               line.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'k1 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki1.kickoutFromGroup(msg.to,[target])           
                               print ("K1 Kick User")
                           except:
                               ki1.sendMessage(msg.to,"Limit kaka 😫")                               

                elif 'k2 kik' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki2.kickoutFromGroup(msg.to,[target])
                               print ("K2 kick user")
                           except:
                               ki2.sendMessage(msg.to,"Limit kaka 😫")                              

                elif 'k3 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki3.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               ki3.sendMessage(msg.to,"Limit kaka 😫")                              

                elif 'k4 kick' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki4.kickoutFromGroup(msg.to,[target])
                               print ("K3 kick user")
                           except:
                               ki4.sendMessage(msg.to,"Limit kaka 😫")                              
                               
                elif 'invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               line.inviteIntoGroup(msg.to,[target])
                               line.sendMessage(receiver, "Type👉 Invite Succes")
                           except:
                               line.sendMessage(msg.to,"Type👉 Limit Invite")

                elif 'k1 invite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki1.inviteIntoGroup(msg.to,[target])
                               ki1.sendMessage(receiver, "Type👉 Invite Succes")
                               print ("R1 invite User")
                           except:
                               ki1.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k2 inv' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki2.inviteIntoGroup(msg.to,[target])
                               ki2.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R2 invite User")
                           except:
                               ki2.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k3 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki3.inviteIntoGroup(msg.to,[target])
                               ki3.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R3 invite User")
                           except:
                               ki3.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif 'k4 getinvite' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki4.inviteIntoGroup(msg.to,[target])
                               ki4.sendMessage(receiver, "Type👉 Invite Succes")
                               ("R4 invite User")
                           except:
                               ki4.sendMessage(msg.to,"Type👉 Limit Invite")                               

                elif "Cleanse" in msg.text:
                	if msg.toType == 2:
                         _name = msg.text.replace("Cleanse","")
                         gs = line.getGroup(receiver)
                         line.sendMessage(receiver,"Just some casual cleansing ô")
                         targets = []
                         for g in gs.members:
                             if _name in g.displayName:
                                 targets.append(g.mid)
                         if targets == []:
                             line.sendMessage(receiver,"Not found.")
                         else:
                             for target in targets:
                             	if not target in Rfu:
                                     try:
                                         klist=[line,ki1,ki2,ki3,ki4]
                                         kicker=random.choice(klist)
                                         kicker.kickoutFromGroup(receiver,[target])
                                         print((receiver,[g.mid]))
                                     except:
                                         line.sendMessage(receiver,"Group cleanse")
                                         print ("Cleanse Group")

                elif msg.text in ["Scan blacklist"]:
                	if msg.toType == 2:
                         group = line.getGroup(receiver)
                         gMembMids = [contact.mid for contact in group.members]
                         matched_list = []
                         for tag in settings["blacklist"]:
                             matched_list+=[str for str in gMembMids if str == tag]
                         if matched_list == []:
                             line.sendMessage(receiver,"Nots in Blacklist")
                         else:
                             for jj in matched_list:
                                 try:
                                     klist=[line,ki1,ki2,ki3,ki4]
                                     kicker=random.choice(klist)
                                     kicker.kickoutFromGroup(receiver,[jj])
                                     print((receiver,[jj]))
                                 except:
                                     line.sendMessage(receiver,"sorry bl ke cyduk")
                                     print ("Blacklist di Kick")

                elif text.lower() == "removechat":
                        if msg._from in Family:
                            try:
                                ki1.removeAllMessages(op.param2)
                                ki2.removeAllMessages(op.param2)
                                ki3.removeAllMessages(op.param2)
                                ki4.removeAllMessages(op.param2)                                
                                line.sendMessage(msg.to,"Remove chat Kicker success....")
                            except:
                                pass
                                print ("Remove Chat Kicker")

                elif text.lower() == "หนีหำ":
                    if msg._from in Family:
                        ki1.leaveGroup(msg.to)
                        ki2.leaveGroup(msg.to)
                        ki3.leaveGroup(msg.to)
                        ki4.leaveGroup(msg.to) 
                        print ("Kicker Leave")

                elif text.lower() == "leaveall":
                    if msg._from in Family:
                        gid = line.getGroupIdsJoined()
                        for i in gid:
                            ki1.leaveGroup(i)
                            ki2.leaveGroup(i)
                            ki3.leaveGroup(i)
                            ki4.leaveGroup(i) 
                           # ki5.leaveGroup(i)
                            #ki6.leaveGroup(i)
                           # ki7.leaveGroup(i)
                           # ki8.leaveGroup(i)
                           # ki9.leaveGroup(i) 
                            #ki10.leaveGroup(i) 
                            print ("Kicker Leave All group")

                elif "myname: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.displayName = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Update to " + string)
                        print ("Update Name")

                elif "upbio: " in msg.text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = line.getProfile()
                        profile_A.statusMessage = string
                        line.updateProfile(profile_A)
                        line.sendMessage(msg.to,"Succes Update 👉 " + string)
                        print ("Update Bio Succes")

                elif "nameall: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki1.getProfile()
                        profile_B = ki2.getProfile()
                        profile_C = ki3.getProfile()
                        profile_D = ki4.getProfile()                        
                        profile_A.displayName = string
                        profile_B.displayName = string
                        profile_C.displayName = string
                        profile_D.displayName = string                        
                        ki1.updateProfile(profile_A)
                        ki2.updateProfile(profile_B)
                        ki3.updateProfile(profile_C)
                        ki4.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Name All Kicker to : " + string)
                        print ("Update Name All Kicker")

                elif "bioall: " in text.lower():
                    if msg._from in Family:
                        proses = text.split(": ")
                        string = text.replace(proses[0] + ": ","")
                        profile_A = ki1.getProfile()
                        profile_B = ki2.getProfile()
                        profile_C = ki3.getProfile()
                        profile_D = ki4.getProfile()                        
                        profile_A.statusMessage = string
                        profile_B.statusMessage = string
                        profile_C.statusMessage = string
                        profile_D.statusMessage = string                        
                        ki1.updateProfile(profile_A)
                        ki2.updateProfile(profile_B)
                        ki3.updateProfile(profile_C)
                        ki4.updateProfile(profile_D)                        
                        line.sendMessage(msg.to,"Update Bio All Kicker to : " + string)
                        print ("Update Bio All Kicker")

                elif text.lower() == "รายงาน":
                    if msg._from in Family:
                        profile = ki1.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        ki1.sendMessage(to, text)                                
                        profile = ki2.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        ki2.sendMessage(to, text)                                
                        profile = ki3.getProfile()
                        text = profile.displayName + "\nรายงานตัว"
                        ki3.sendMessage(to, text)
                        profile = ki4.getProfile()                        
                        text = profile.displayName + "\nรายงานตัว"
                        ki4.sendMessage(to, text)                        
                        print ("Kicker Respon")

                elif msg.text in ["Bot?"]:
                    ki1.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰")
                    ki2.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰2")
                    ki3.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰3")
                    ki4.sendMessage(msg.to,"✰ɢʜᴏsᴛ ᴛᴇᴀᴍ✰4")    
                elif msg.text.lower().startswith("bitcoin"):
                   search = msg.text.split("bitcoin")
                   with requests.session() as web:
                       web.headers["User-Agent"] = random.choice(settings["userAgent"])
                       url = "https://xeonwz.herokuapp.com/bitcoin.api"
                       r = web.get(url)
                       data=r.text
                       data=json.loads(data)
                       print(data)
                       hasil = "「 Bitcoin Result 」"
                       hasil += "\nPrice : " +str(data["btc"])                                
                       hasil += "\nExpensive : " +str(data["high"])
                       hasil += "\nCheap : " +str(data["low"])               
                       line.sendMessage(to, str(hasil))
#=============COMMAND PROTECT=========================#
                elif msg.text.lower() == 'protect on':
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกัน   ")

                elif msg.text.lower() == 'protect off':
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกัน   ")

                elif msg.text.lower() == 'cancel pro on':
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'cancel pro off':
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเลิกเชิญ   ")

                elif msg.text.lower() == 'invit pro on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'invit pro off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ   ")

                elif msg.text.lower() == 'link pro on':
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'link pro off':
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันลิ้ง   ")

                elif msg.text.lower() == 'guest pro on':
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'guest pro off':
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันสมาชิก   ")

                elif msg.text.lower() == 'join pro on':
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'join pro off':
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันคนเข้า   ")

                elif msg.text.lower() == 'proall on':
                    if RfuProtect["inviteprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰เปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    if RfuProtect["protect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันยกเลิกเชิญ")
                    else:
                        RfuProtect["protect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันลิ้ง")
                    if RfuProtect["Protectguest"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == True:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = True
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"เปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

                elif msg.text.lower() == 'proall off':
                    if RfuProtect["inviteprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                        else:
                            line.sendMessage(msg.to,"✰ปิดป้องกันทั้งหมด✰")
                    else:
                        RfuProtect["inviteprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเชิญ")
                    if RfuProtect["cancelprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    else:
                        RfuProtect["cancelprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันยกเชิญ")
                    if RfuProtect["protect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    else:
                        RfuProtect["protect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเตะ")
                    if RfuProtect["linkprotect"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    else:
                        RfuProtect["linkprotect"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันเปิดลิ้ง")
                    if RfuProtect["Protectguest"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    else:
                        RfuProtect["Protectguest"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันกลุ่ม")
                    if RfuProtect["Protectjoin"] == False:
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                    else:
                        RfuProtect["Protectjoin"] = False
                        if settings["lang"] == "JP":
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")
                        else:
                            line.sendMessage(msg.to,"ปิดป้องกันบุคคลภายน้อกเข้ากลุ่ม")

#==============FINNISHING PROTECT========================#
                elif msg.text.lower() == 'welcomemessage on':
                        if settings["Wc"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   .")
                        else:
                            settings["Wc"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                elif msg.text.lower() == 'welcomemessage off':
                        if settings["Wc"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")
                        else:
                            settings["Wc"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกเข้ากลุ่ม   ")

                elif msg.text.lower() == 'leavemessage on':
                        if settings["Lv"] == True:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = True
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"เปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                elif msg.text.lower() == 'leavemessage off':
                        if settings["Lv"] == False:
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")
                        else:
                            settings["Lv"] = False
                            if settings["lang"] == "JP":
                                line.sendMessage(to,"ปิดข้อความต้อนรับมีคนสมาชิกออกกลุ่ม   ")

                elif text.lower() == 'ลบรัน':
                    gid = line.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        line.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    line.sendMessage(to, "ลบรันเสร็จแล้วขอรับ")
                    line.sendMessage(to, "ระยะเวลาที่ใช้: %sวินาที" % (elapsed_time))								
								
                elif "Allban" in msg.text:
                  if msg._from in Family:
                      if msg.toType == 2:
                           print ("All Banlist")
                           _name = msg.text.replace("Allban","")
                           gs = line.getGroup(msg.to)
                           line.sendMessage(msg.to,"Banned all")
                           targets = []
                           for g in gs.members:
                               if _name in g.displayName:
                                    targets.append(g.mid)
                           if targets == []:
                                line.sendMessage(msg.to,"Maaf")
                           else:
                               for target in targets:
                                   if not target in Family:
                                       try:
                                           settings["blacklist"][target] = True
                                           f=codecs.open('st2__b.json','w','utf-8')
                                           json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       except:
                                           line.sentMessage(msg.to,"All members has been added ban.")
										   
                elif 'ban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               settings["blacklist"][target] = True
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes added for the blacklist ")
                               print ("Banned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif 'unban' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               del settings["blacklist"][target]
                               f=codecs.open('st2__b.json','w','utf-8')
                               json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                               line.sendMessage(msg.to,"Succes unban from the blacklist. ")
                               print ("Unbanned User")
                           except:
                               line.sendMessage(msg.to,"Contact Not Found")

                elif msg.text in ["เชคดำ"]:
                  if msg._from in Family:
                    if settings["blacklist"] == {}:
                        line.sendMessage(msg.to,"ไม่พบ") 
                    else:
                        line.sendMessage(msg.to,"รายชื่อผู้ติดดำ")
                        mc = "Blacklist User\n"
                        for mi_d in settings["blacklist"]:
                            mc += "[√] " + line.getContact(mi_d).displayName + " \n"
                        line.sendMessage(msg.to, mc + "")

                elif msg.text.lower().startswith("urban "):
                    sep = msg.text.split(" ")
                    judul = msg.text.replace(sep[0] + " ","")
                    url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                    with requests.session() as s:
                        s.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = s.get(url)
                        data = r.text
                        data = json.loads(data)
                        y = "[ Result Urban ]"
                        y += "\nTags: "+ data["tags"][0]
                        y += ","+ data["tags"][1]
                        y += ","+ data["tags"][2]
                        y += ","+ data["tags"][3]
                        y += ","+ data["tags"][4]
                        y += ","+ data["tags"][5]
                        y += ","+ data["tags"][6]
                        y += ","+ data["tags"][7]
                        y += "\n[1]\nAuthor: "+str(data["list"][0]["author"])
                        y += "\nWord: "+str(data["list"][0]["word"])
                        y += "\nLink: "+str(data["list"][0]["permalink"])
                        y += "\nDefinition: "+str(data["list"][0]["definition"])
                        y += "\nExample: "+str(data["list"][0]["example"])
                        line.sendMessage(to, str(y))
            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = "╔══[ Sticker Info ]"
                    ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                    ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                    ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
              
#==============================================================================#
        if op.type == 19:
          if op.param2 in Family:
            pass
          if op.param2 in RfuBot:
          	pass
          else:
            if op.param3 in lineMID:
              if op.param2 not in Family:
                try:
                  G = ki1.getGroup(op.param1)
                  G = ki2.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki2.updateGroup(G)
                  ticket = ki2.reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  line.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in ki1MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki3.getGroup(op.param1)
                  ki2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki3.updateGroup(G)
                  ticket = ki3.reissueGroupTicket(op.param1)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)                  
                  G.preventedJoinByTicket = True
                  ki2.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki2.updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki1.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki2MID:
              if op.param2 not in Family:
                try:
                  G = ki3.getGroup(op.param1)
                  G = ki1.getGroup(op.param1)
                  ki3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki3.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki2.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1)
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in ki3MID:
              if op.param2 not in Family:
                try:
                  G = ki2.getGroup(op.param1)
                  G = ki4.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki1.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki3.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param3 in ki4MID:
              if op.param2 not in Family:
                try:
                  G = ki1.getGroup(op.param1)
                  G = ki3.getGroup(op.param1)
                  ki1.kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  ki1.updateGroup(G)
                  ticket = ki1.reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  ki4.updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(Rfu).getGroup(op.param1) 
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                  G.preventedJoinByTicket = False
                  random.choice(Rfu).updateGroup(G)
                  ticket = random.choice(Rfu).reissueGroupTicket(op.param1)
                  ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                  time.sleep(0.01)
                  G.preventedJoinByTicket = True
                  random.choice(Rfu).updateGroup(G)
                  settings["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(settings["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)                  

        if op.type == 19:
            if lineMID in op.param3:
                settings["blacklist"][op.param2] = True
        if op.type == 22:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)                
        if op.type == 24:
            if settings['leaveRoom'] == True:
                line.leaveRoom(op.param1)
                ki1.leaveRoom(op.param1)
                ki2.leaveRoom(op.param1)
                ki3.leaveRoom(op.param1)
                ki4.leaveRoom(op.param1)                
#==============================================================================#
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in ki1MID:
                        G = ki1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    else:
                        G = ki1.getGroup(op.param1)                                                
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                        settings["blacklist"][op.param2] = True                       

                elif op.param3 in ki1MID:
                    if op.param2 in lineMID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki2MID:
                    if op.param2 in ki1MID:
                        G = ki1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                    else:
                        G = ki1.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki1.updateGroup(G)
                        ticket = ki1.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        G.preventedJoinByTicket = True
                        ki1.updateGroup(G)
                        settings["blacklist"][op.param2] = True

                elif op.param3 in ki3MID:
                    if op.param2 in ki2MID:
                        G = ki2.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki2.updateGroup(G)
                        ticket = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                        settings["blacklist"][op.param2] = True
                elif op.param3 in ki4MID:
                    if op.param2 in ki3MID:
                        G = ki4.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        ticket = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki3.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)
                        random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki4.updateGroup(G)
                        ticket = ki4.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        line.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki1.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki2.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki4.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki4.updateGroup(G)
                        settings["blacklist"][op.param2] = True
            except:
                pass
#==============================================================================#
        if op.type == 17:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
            if RfuProtect["protect"] == True:
                if settings["blacklist"][op.param2] == True:
                    try:
                        line.kickoutFromGroup(op.param1,[op.param2])
                        G = line.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        line.updateGroup(G)
                    except:
                        try:
                            line.kickoutFromGroup(op.param1,[op.param2])
                            G = line.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            line.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["protect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Rfu).inviteIntoGroup(op.param1,[op.param2])

        if op.type == 13:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["inviteprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Family:
                        if op.param2 in Family:
                            pass
                        elif RfuProtect["inviteprotect"] == True:
                            settings ["blacklist"][op.param2] = True
                            random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
                            if op.param2 not in Family:
                                if op.param2 in Family:
                                    pass
                                elif RfuProtect["cancelprotect"] == True:
                                    settings ["blacklist"][op.param2] = True
                                    random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])

        if op.type == 11:
            if op.param2 not in Family:
                if op.param2 in Family:
                    pass
                elif RfuProtect["linkprotect"] == True:
                    settings ["blacklist"][op.param2] = True
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    line.updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if RfuProtect["autoAdd"] == True:
                if (settings["message"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["message"]))
                    ki1.sendMessage(op.param1,str(settings["message"]))
                    ki2.sendMessage(op.param1,str(settings["message"]))
                    ki3.sendMessage(op.param1,str(settings["message"]))
                    ki4.sendMessage(op.param1,str(settings["message"]))                    

        if op.type == 11:
            if RfuProtect["linkprotect"] == True:
                if op.param2 not in Family:
                    G = line.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Rfu).updateGroup(G)
                    random.choice(Rfu).kickoutFromGroup(op.param1,[op.param3])                    

        if op.type == 13:
           if RfuProtect["Protectguest"] == True:
               if op.param2 not in Family:
                  random.choice(Rfu).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
           if RfuProtect["Protectjoin"] == True:
               if op.param2 not in Family:
                   random.choice(Rfu).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 1:
            if sender in Setmain["foto"]:
                path = line.downloadObjectMsg(msg_id)
                del Setmain["foto"][sender]
                line.updateProfilePicture(path)
                line.sendMessage(to,"Foto berhasil dirubah")

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != line.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    line.sendChatChecked(to, msg_id)
                    ki1.sendChatChecked(to, msg_id)
                    ki2.sendChatChecked(to, msg_id)
                    ki3.sendChatChecked(to, msg_id)
                    ki4.sendChatChecked(to, msg_id)					
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        line.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys())!= None:
                         if settings['potoMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.pictureStatus
                             balas = ["http://dl.profile.line-cdn.net/" + cName]
                             ret_ = random.choice(balas)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention["MENTIONEES"]
                             for mention in mentionees:
                                   if mention["M"] in lineMID:
                                          line.sendImageWithURL(to,ret_)
                                          break  
                if msg.contentType == 0 and sender not in lineMID and msg.toType == 2:
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = line.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『 Auto Respon』\n " + cName + "\n『แทคทำไมหรอ?』"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in lineMID:
                                          line.sendMessage(to,ret_)
                                          sendMessageWithMention(to, contact.mid)
                                          break										  
                if msg.text in ["Me","me",".me",".Me","คท","/me"]:
                    line.sendText(msg.to,"😜เชคจัง กลัวบอทหลุดละสิ😂")
                if msg.text in ["sp","speed",".speed","/speed","Sp",".Speed"]:
                    line.sendText(msg.to,"😜แรงครับแรงแล้ว😂")
                if msg.text in ["runtime","Runtime","/uptime","ออน",".uptime"]:
                    line.sendText(msg.to,"จะล็อคเซลนานไปไหน")				
                if msg.text in dangerMessage:
                    random.choice(Rfu).kickoutFromGroup(receiver,[sender])
                    random.choice(Rfu).sendText(msg.to,"ตรวจพบคำสั่งของบอทลบกลุ่ม จำเป็นต้องนำออกเพื่อความปลอดภัยของสมาชิก (｀・ω・´)")										
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 17:
          if settings["Wc"] == True:
            if op.param2 in admin:
                return
            ginfo = line.getGroup(op.param1)
            contact = line.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus			
            line.sendText(op.param1, " ยินดีต้อนรับ. เข้ามาแล้วก็อย่าลืมปิดแจ้งเตือนกันน่ะครับ" + line.getContact(op.param2).displayName + " สู่กลุ่ม " + "👉" + str(ginfo.name) + "👈""\nหรือสนใจลงบอทป้องกันบอทแท็ก ติดต่อได้ที่Line ID : nunu_kap123\nhttp://line.me/ti/p/~nunu_kap123")			
# ----------------- NOTIFED MEMBER OUT GROUP
        if op.type == 15:
          if settings['Lv'] == True:
            if op.param2 in bot1:
                return
            line.sendText(op.param1,"good Bye" + line.getContact(op.param2).displayName + "รีบไปไหนอ่ะ. ไม่เป็นไรไว้เจอกันใหม่น่ะจ๊ะ")
# ----------------- NOTIFED MEMBER JOIN GROUP
        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n🔰" + Name
                            pref=['eh ada','hai kak','hay kamu','nah ada','halo lg ngapain','halo','sini kak','cctv yah kak']
                            line.sendMessage(op.param1, str(random.choice(pref))+' '+Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            try:
                if RfuCctv['cyduk'][op.param1]==True:
                    if op.param1 in RfuCctv['point']:
                        Name = line.getContact(op.param2).displayName
                        if Name in RfuCctv['sidermem'][op.param1]:
                            pass
                        else:
                            RfuCctv['sidermem'][op.param1] += "\n⌬ " + Name + "\n╚════════════════┛"
                            if " " in Name:
                            	nick = Name.split(' ')
                            if len(nick) == 2:
                            	line.sendMessage(op.param1, "Nah " +nick[0])
                            summon(op.param1, [op.param2])
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 55:
            print ("[ 55 ] ตรวจพบข้อความ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
#==============================================================================#
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
