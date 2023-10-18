from ClassicAssist.UO.Data import Statics
from Assistant import Engine
from System import Convert
from ClassicAssist.UO import UOMath
from ClassicAssist.UO.Data import Direction
import System
import clr
import os

clr.AddReference('System.Core')
clr.ImportExtensions(System.Linq)

###################### I M P O R T A N T ##################
#- The script can only run if all desired runebooks have been read in beforehand with the script 
#  'PanningSearchTarget'. The path to the books must be the same in both scripts.
#- The script expects a Goldpan Storage direct in your backpack.
#- If there is a master key in the backpack, then at the end of a spot everything is included 
#  in the key with [ffp. Without a master key, a treasure key must be in the backpack if the 
#  bottles are to be extracted.
############################################################

#change the path to your folder you like to store the book files. Please use the \\ to separate 
#the folders

# type for recall, best is chiv, the script does check the hands for pole :D
#c = chiv, r = magery
recallType = 'c'     

fingerJackKey = 'n'   #'n'  if you use a normal one
dressName = 'panning'

# this are breaks for people with high pings ;) you can try to loweer them if your ping is fast
moveItemPause = 800
smallPause = 100
middlePause = 400

#ca have no option to pause a script. if the next option is 'y', then you can use the 'PauseMacros'
#script to pause where you are. If you stop 'PauseMacros' it will continue from there.
#(give the pause a few seconds for it to take effect)
possibleToBreak = 'n'   

#i use illys 'CaptchaAlert', i removed the messagebox and if your script contains 
#a different name, please enter it
lookForCaptchas = 'n'   #if set to 'n' then the script doesn't look for afk checks
captaAlertScriptName = 'afk-alert'

#you can choose how the script should handle the MiBs. If it is set to 'n', the MiBs 
#will be unpacked and included in the treasure key. If it is 'y' then the bottles are 
#pushed into a bag in the bank. This then requires the serial of the Cyratal and the bag in the bank.
extractMiBs = 'y'   
#the next two lines are only needed when extractMiBs = 'y'
bankCrystal = 0x42a30987
bankBag = 0x46775617


############ From here no more changes necessary ##############

tiles = []
panTile = []
recallPlace = []
positionList = []
    
backpack = Engine.Items.GetItem(GetAlias('backpack')).Container

allRunebooks = backpack.Where(lambda i: i.ID == 0x22c5)

runebooks = []
for runebook in allRunebooks:
    for prop in runebook.Properties:
        if 'Large Nuggets' in prop.Text:
            runebooks.append((runebook, prop.Text))
            
                       
if not runebooks:
    HeadMsg("No Runebooks to run")
    Stop()
    
runebooks.sort(key=lambda runebook: runebook[1])
    
SetQuietMode(True)
ClearJournal()

if fingerJackKey == 'y':
    panKeyHue = 1992
else:
    panKeyHue = 1991

def checkPole():
    if not FindLayer('OneHanded'):
        Dress(dressName)
        while Dressing():
            Pause(1000)
            
def worldSave():
    if InJournal('The world is saving, please wait.', 'system' ):
        HeadMsg('Pausing for world save','self', 82)
        Pause(250)
        if WaitForJournal('World save complete.',60000, 'system'):
            HeadMsg('Continuing','self',82)
            Pause(250)
        ClearJournal()
    return True

#travelSpell c = chiv, r = magery
def travel(runeBook = None, place = None, travelSpell = 'c'):
    if runeBook is None or place is None:
        return False
    if travelSpell != 'c' and travelSpell != 'r':
        return False
    if travelSpell == 'c':
        bookPos = place * 6 + 1
    if travelSpell == 'r': 
        bookPos = place * 6 - 1
    ClearJournal()
    worldSave()
    UseObject(runeBook)
    Pause(smallPause)
    WaitForGump(0x554b87f3, 5000)
    Pause(middlePause)
    if InJournal('time to recharge'):
        Pause(4500)
        travel(runeBook, place, travelSpell)
        Pause(smallPause)
    ReplyGump(0x554b87f3, bookPos)
    Pause(2500)
    if InJournal('location is blocked'):
        return False
    return True

def panGold(tile):
    checkPole()
    worldSave()
    breaking()
    UseType(0x9d7,0,'backpack')
    WaitForTarget(5000)
    Pause(middlePause)
    TargetXYZ(int(tile[0]), int(tile[1]), int(tile[2]), int(tile[3]))
    Pause(middlePause)
    if InJournal("Target cannot", "system"): 
        ClearJournal()
        Pause(4000)
        return False
    if InJournal("to be closer", "system"): 
        ClearJournal()
        Pause(4000)
        return False    
    if InJournal("seem to be any", "system"): 
        Pause(4000)
        ClearJournal()
        return False        
    Pause(10000)
    checkGoldpan()
    if InJournal("around until your pan is full", "system") or InJournal("fail to find any nuggets", "system"): 
        ClearJournal()
        panGold(tile)

def checkGoldpan():
    Pause(smallPause)
    worldSave()
    if FindType(0x9d7, -1, 'backpack', 0):
        return True
    if FindType(0x9d8, -1, 'backpack', 0):
        UseObject("found")
        Pause(smallPause)
        return True
    return False
    
def getGoldpan():
    worldSave()
    if FindType(0x9d7, -1, 'backpack', panKeyHue):
        SetAlias('goldpan', 'found')
        UseObject('goldpan')
        Pause(middlePause)
        ReplyGump(0x6abce12, 4)
        WaitForGump(0x6abce12, 5000)   
        ReplyGump(0x6abce12, 0)
        if checkGoldpan():
            return True
        else:
            getGoldpan()
    else:
        HeadMsg("**** cant find a goldpan storage found ****", 'self', 82)  
        Pause(smallPause)
        return False

def fillGoldKey():
    worldSave()
    if FindType(0x9d7, -1, 'backpack', panKeyHue):
        WaitForContext('found', 2, 5000)
        WaitForGump(0x6abce12, 5000)
        ReplyGump(0x6abce12, 0)
        return True
    else:
        HeadMsg("**** cant find a goldpan storage found ****", 'self', 82)  
        Pause(smallPause)
        return False

def trashLoot():
    if FindType(0x9b2, -1, 'backpack', 1173):
        SetAlias('trashbag', 'found')
        trashList = [0x170f, 0x170b, 0x1711, 0x2307]
        for trash in trashList:
            while FindType(trash, -1, 'backpack', -1):
                worldSave()
                MoveItem('found', 'trashbag')
                Pause(moveItemPause)
                IgnoreObject('found')
        if FindType(0x176b, -1, 'backpack', -1):
                Msg("[ffp")
                Pause(middlePause)                
        return True
    else:
        HeadMsg("*** cant find a trash bag, please check it ***", 'self', 82)  
        Pause(smallPause)
        return False
    
def clearMiBs(extractMiBs):
    if not FindType(0x99f, -1, 'backpack',0):
        return False
    if extractMiBs == 'y':
        if FindType(0x14ee,-1,'backpack',1861):
            SetAlias('treasureKey', 'found')
            while FindType(0x99f, -1, 'backpack',0):
                worldSave()
                UseObject('found')
                Pause(middlePause)
            if FindType(0x176b, -1, 'backpack', -1):
                Msg("[ffp")
                Pause(middlePause)
            else: 
                WaitForContext('treasureKey', 2, 5000)
                WaitForGump(0x6abce12, 5000)
                ReplyGump(0x6abce12, 0)    
                Pause(smallPause)
            return True
        else:
            HeadMsg("*** cant find a treasure key, please check it ***", 'self', 82)  
            Pause(smallPause)
            return False
    else:        
        worldSave()
        if FindObject(bankCrystal , -1, 'backpack'):
            UseObject(bankCrystal)
            Pause(middlePause)
            while FindType(0x99f, -1, 'backpack',0):
                MoveItem('found', bankBag)
                Pause(moveItemPause)
            return True
        else:
            HeadMsg("*** cant find a bank crystal, please check it ***", 'self', 82)  
            Pause(smallPause)
            return False    

def getLocations(filePath):
    panPos = dict()
    worldSave()
    with open(filePath) as file:
        for line in file:
            worldSave()
            a = line.strip().split(':')
            #print(a)
            panPos[int(a[0])] = [ a[1].split(','),a[2].split(',')]
        return panPos

def checkAlert():
    if not Playing(captaAlertScriptName):
        PlayMacro(captaAlertScriptName)
        Pause(100)   

def breaking():
    while Playing("PauseMacros"):
        Pause(100)   

#Prompt the runebook to search the targets
#if not FindAlias('LargeSpotBook'):
#    HeadMsg("Please target a empty Runebook for Goldpanning Spots..", 'self', 82)  
#    Pause(smallPause)
#    PromptMacroAlias("LargeSpotBook")

for i in runebooks:
    runebook = i[0]
    bookName = i[1]
    HeadMsg("Executing Book {} ({})".format(bookName, hex(runebook.Serial)))

    UseObject(runebook)
    Pause(smallPause)
    WaitForGump(0x554b87f3, 5000)

    res, gump = Engine.Gumps.GetGump(0x554b87f3)

    for page in gump.Pages:
        for element in page.GumpElements:
            if element.Type.ToString() == "croppedtext":
                positionText = element.Text
                #print positionText
                if positionText not in positionList:
                    positionList.append(positionText)
    locations = dict()
    cont=0
    for line in positionList:
        cont=cont+1
        locations[int(cont)] = [ line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]]
    
    for pos in range(1,17):
        #print(type(runebook))
        checkAlert()
        worldSave()
        breaking()
        while not travel(runebook, pos, recallType):
            Pause(smallPause)
        #print(pos)
        Pause(moveItemPause)
        if not checkGoldpan():
            if not getGoldpan():
                Stop()
        tile = [int(locations[pos][0]), int(locations[pos][1]), int(locations[pos][2]), int(locations[pos][3])]
        print('{}({}) - spot: {} @ X{}|Y{}|Z{}|ID{}'.format(bookName,hex(runebook.Serial), pos,int(locations[pos][0]), int(locations[pos][1]), int(locations[pos][2]), int(locations[pos][3])))  
        while panGold(tile):
            Pause(150)
    
        trashLoot()
        fillGoldKey()
        clearMiBs(extractMiBs)

PlayMacro("gohome")

