from Assistant import Engine
import datetime

SetAlias('JacksStorageKey', 0x41c3173b) #use OBject Inspector to get the Serial ID
SetAlias('BagOfHolding', 0x425cf6b7) #use OBject Inspector to get the Serial ID
SetAlias('TrashBag', 0x43a3dd96) #use OBject Inspector to get the Serial ID
weightThreshold = .65 #Mine is set to 65%, 

def CheckBagWeights():
    currentWeight = MaxWeight() - DiffWeight()
    threshholdWeight = MaxWeight() * weightThreshold
    if currentWeight >= MaxWeight() or currentWeight >= threshholdWeight:
        msg = "You have reached your weight threshold... moving items!"
        HeadMsg(msg)
        SysMessage(msg, 35)
        if FindObject('JacksStorageKey', -1, "backpack"):
            JacksStorageKey()
            Move_Items_To_Trash()
        else:    
            Move_Items_To_Bag_Of_Holding()
            Move_Items_To_Trash()
        
def JacksStorageKey():
    SysMessage("Activating Three Finger Jack's Gold Pan Storage", 35)
    WaitForContext('JacksStorageKey', 2, 600) 
    WaitForGump(0x6abce12, 600)
    ReplyGump(0x6abce12, 0)

def Move_Items_To_Bag_Of_Holding():
    findPearl = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("White Pearl"))
    findAmber = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Brilliant Amber"))
    findTurquoise = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Turquoise"))
    findCitrine = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Excru Citrine"))
    findEmerald = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Perfect Emerald"))
    findRuby = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Fire Ruby"))
    findSapphire = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Dark Sapphire"))
    findBlackrock = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Crystalline Blackrock"))
    findBlueDiamond = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Blue Diamond"))
    pauseCount = 750 # 750 milliseconds seems to work fine for me. It gives the program time to do what it needs before moving on.
    msg = "Please wait... moving item to storage container!"
    HeadMsg(msg)
    SysMessage(msg, 35)
    if findPearl != None:
          for item in findPearl:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)

    if findAmber != None:
          for item in findAmber:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)

    if findTurquoise != None:
          for item in findTurquoise:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)

    if findCitrine != None:
        for item in findCitrine:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)

    if findEmerald != None:
        for item in findEmerald:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)
        
    if findRuby != None:
        for item in findRuby:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)

    if findSapphire != None:
        for item in findSapphire:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)
        
    if findBlackrock != None:
        for item in findBlackrock:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)
        
    if findBlueDiamond != None:
        for item in findBlueDiamond:
            MoveItem(item.Serial, 'BagOfHolding')
            Pause(pauseCount)
    WaitForContext(0x44b3ec99, 0, 500)
	

def Move_Items_To_Trash():
    findBoots = Engine.Player.Backpack.Container.SelectEntities(lambda i: filter == None or i.Name.Contains("Boots"))
    pauseCount = 750 # 750 milliseconds seems to work fine for me. It gives the program time to do what it needs before moving on.
    msg = "Please wait... moving item to trash container!"
    HeadMsg(msg)
    SysMessage(msg, 35)
    if findBoots != None:
          for item in findBoots:
            MoveItem(item.Serial, 'TrashBag')
            Pause(pauseCount)
    WaitForContext(0x44b3ec99, 0, 500)


UseType(0x9d7)
WaitForTarget(15000)

if Direction () == 'North':
  TargetTileOffsetResource(0, -3, 0)
if Direction () == 'Northeast':
  TargetTileOffsetResource(3, -3, 0)
if Direction () == 'East':
  TargetTileOffsetResource(3, 0, 0)
if Direction () == 'Southeast':
  TargetTileOffsetResource(3, 3, 0)
if Direction () == 'South':
  TargetTileOffsetResource(0, 3, 0)
if Direction () == 'Southwest':
  TargetTileOffsetResource(-3, 3, 0)
if Direction () == 'West':
  TargetTileOffsetResource(-3, 0, 0)
if Direction () == 'Northwest':
  TargetTileOffsetResource(-3, -3, 0)
#endif
Pause (11000)
UseType(0x9d8)
Pause (4000)
CheckBagWeights()