from ClassicAssist.UO.Data import Statics
from Assistant import Engine
from System import Convert
from ClassicAssist.UO import UOMath
from ClassicAssist.UO.Data import Direction
import System
import os
#v.2
###################### I M P O R T A N T ##################
#This script tries to find a valid target at your location and searches for large nuggets. 
#When a large nugget is found, a rune is marked and placed in the book you previously selected..
############################################################
#please right the correct name from your dress agent with the pole, so it will equipped after marking
fingerJackKey = 'n'   #'n'  if you use a normal one
dressName = 'panning'
colorTrashbag = 1173      #1173 is the original
# this are breaks for people with high pings ;) you can try to loweer them if your ping is fast
moveItemPause = 800
smallPause = 160
middlePause = 600

#you can choose how the script should handle the MiBs. If it is set to 'n', the MiBs 
#will be unpacked and included in the treasure key. If it is 'y' then the bottles are 
#pushed into a bag in the bank. This then requires the serial of the Cyratal and the bag in the bank.
extractMiBs = 'y'   
#the next two lines are only needed when extractMiBs = 'y'
bankCrystal = 0x42a30987
bankBag = 0x46775617

############ From here no more changes necessary ##############

searchRange = 4    
tiles = []
panTile = []
recallPlace = []

if fingerJackKey == 'y':
    panKeyHue = 1992
else:
    panKeyHue = 1991

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
    UseObject(runeBook)
    Pause(smallPause)
    WaitForGump(0x554b87f3, 5000)
    Pause(middlePause)
    if InJournal('time to recharge'):
        Pause(3000)
        travel(runeBook, place, travelSpell)
        Pause(smallPause)
    ReplyGump(0x554b87f3, bookPos)
    Pause(2500)
    if InJournal('location is blocked'):
        return False
    return True

def findPanTarget(tiles, searchRadius):
    checkPole()
    for tile in tiles:
        UseType(0x9d7,0,'backpack')
        WaitForTarget(5000)
        Pause(middlePause)
        TargetXYZ(tile['X'], tile['Y'], tile['Z'], tile['ID'])
        Pause(middlePause)
        if InJournal("Target cannot", "system"): 
            ClearJournal()
            continue
        if InJournal("to be closer", "system"): 
            ClearJournal()
            continue        
        if InJournal("seem to be any", "system"): 
            ClearJournal()
            return False
        Pause(11000) 
        large = checkGoldpan()
        if large == 'large':
            return 'large'
        if InJournal("seem to be any", "system"): 
            panTile = [tile['X'], tile['Y'], tile['Z'], tile['ID']]
            ClearJournal()
            return panTile                
        if InJournal("around until your pan is full", "system") or InJournal("fail to find any nuggets", "system"): 
            panTile = [tile['X'], tile['Y'], tile['Z'], tile['ID']]
            ClearJournal()
            return panTile

def getTiles(searchRadius):
    waterTiles = [ 0x179c, 0x1798, 0x1797, 0x1799, 0x179b, 0x179a, 0xa9, 0xa8, 0xab, 0xaa, 0x17ad]
    #global tiles
    for x in range(Engine.Player.X - searchRadius, Engine.Player.X + searchRadius):
        for y in range(Engine.Player.Y - searchRadius, Engine.Player.Y + searchRadius):
            statics = Statics.GetStatics(Convert.ChangeType(Engine.Player.Map, int), x, y)
            #print((statics))
            try:
                for s in statics:
                    if waterTiles.Contains(s.ID):
                        tiles.append({'X': s.X, 'Y': s.Y, 'Z': s.Z, 'ID': s.ID, 'Distance': UOMath.Distance(Engine.Player.X, Engine.Player.Y, s.X, s.Y)})
            except:
                continue    
    return tiles
    
def checkGoldpan():
    ClearJournal()
    Pause(smallPause)
    if FindType(0x9d7, -1, 'backpack', 0):
        return True
    if FindType(0x9d8, -1, 'backpack', 0):
        UseObject("found")
        Pause(moveItemPause)
        if InJournal('large','system'):
            ClearJournal()    
            return 'large'
        return True
    return False
    
def getGoldpan():
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
    if FindType(0x9b2, -1, 'backpack', colorTrashbag):
        SetAlias('trashbag', 'found')
        trashList = [0x170f, 0x170b, 0x1711, 0x2307]
        for trash in trashList:
            while FindType(trash, -1, 'backpack', -1):
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

def panGold(tile):
    ClearJournal()
    checkPole()
    UseType(0x9d7,0,'backpack')
    WaitForTarget(5000)
    Pause(middlePause)
    #print(tile)
    Pause(500)
    TargetXYZ(int(tile[0]), int(tile[1]), int(tile[2]), int(tile[3]))
    Pause(middlePause)
    if InJournal("Target cannot", "system"): 
        ClearJournal()
        return False
    if InJournal("to be closer", "system"): 
        ClearJournal()
        return False    
    Pause(11000)
    if InJournal("seem to be any", "system"): 
        ClearJournal()
        return False        
    large = checkGoldpan()
    if large == 'large':
        return 'large'
    if InJournal("around until your pan is full", "system") or InJournal("fail to find any nuggets", "system"): 
        ClearJournal()
        panGold(tile)

        
def markRune(runebook, position_text):
        Cast("Mark")
        WaitForTarget(5000)
        Pause(1000)
        if FindType(0x1f14, -1, 'backpack', -1):
            HeadMsg("Marking This rune", "found", 1990)
            Target('found')
            Pause(300)
            UseObject("found")
            WaitForPrompt(2000)
            PromptMsg(position_text)
            Pause(1000)
            MoveItem('found', runebook)
            Pause(1000)
            return True
        else:
            markRune(runebook)

def checkPole():
    if not FindLayer('OneHanded'):
        Dress(dressName)
        while Dressing():
            Pause(500)

def finishSpot():
    trashLoot()
    fillGoldKey()
    clearMiBs(extractMiBs)
    HeadMsg("Spot empty or Large Nuggets found..", 'self', 82)  
    Pause(smallPause)

#Prompt the runebook to search the targets
if not FindAlias('LargeSpotBook'):
    HeadMsg("Please target a empty Runebook for Goldpanning Spots..", 'self', 82)  
    Pause(smallPause)
    PromptMacroAlias("LargeSpotBook")

runebook = GetAlias('LargeSpotBook')


tiles = []
if not checkGoldpan():
    if not getGoldpan():
        Stop()

for r in range(1,6):
    tiles = getTiles(r)
    #print(tiles)
    location = findPanTarget(tiles, r)
    if location is not None:
        break

#print(location)
if location == 'large':
    position_text = "{},{},{},{}".format(tiles[0]['X'], tiles[0]['Y'], tiles[0]['Z'], tiles[0]['ID'])
    markRune(runebook, position_text)
    finishSpot()
    Stop()
    Pause(500)
if location == False:
    finishSpot()
    Stop()
    Pause(500)

if location != 'large' and location != False:
    large = panGold(location)
    #print(large)
    Pause(100)
    if large == 'large':
        markRune(runebook)
        finishSpot()
        Stop()
        Pause(500)
    if large == False:
        finishSpot()
        Stop()
        Pause(500)
