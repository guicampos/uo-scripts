from System.Collections.Generic import List

# SETTINGS
boh = 0x4046ACB1
lootbag = 0x4045B50D
masterkey = 0x4019B16D
corpse_ID = 0x2006
#backpack = Player.Backpack.Serial
backpack = 0x4046ACAB
#clearignore = 30000000 #Time to clear ignorelist

corpses_filter = Items.Filter()
corpses_filter.IsCorpse = True # optional
corpses_filter.OnGround = True # Questionably optional
corpses_filter.RangeMin = 0 # optional
corpses_filter.RangeMax = 2 # optoinal
corpses_filter.Graphics = List[int]([corpse_ID,]) # optional, use item IDs
corpses_filter.CheckIgnoreObject = True # optioinal, if you use Misc.IgnoreObject(item) the fitler will ignore if true.


loot_list  = [ #loot all colors
0x1EBA, #Tool Kit
0x0DCA, #fish nets
0x099F, #bottles
0x26B4, #scales
0x4077, #dragon blood
0x9E28, #BooksRecipes
#0x0DCF, #all seeds
0x1EA7, #Arcane Gem

#0x2D51, #arcane circle
#0x2D52, #Gift of Renewal
#0x2D53, #Immolating Weapon
#0x2D54, #Attunement
#0x2D55, #Thunderstorm
#0x2D56, #Natures Fury
#0x2D58, #Thunderstorm
#0x2D59, #Reaper Form
#0x2D5A, #Wildfire
#0x2D5B, #Essence of Wind
#0x2D5C, #Dryad Allure
#0x2D5D, #Ethereal Voyage
#0x2D5E, #Word of Death
#0x2D5F, #Gift of Life
#0x2D60, #Arcane Empowerment

#0x14EC  #Maps
0x2831 #Recipes

] #Goes to Lootbag

loot_boh =[ #Goes to BOH bag
0x0EED, #Gold
0x0F3F, #Arrow
0xAE60, #Arrow 
0x0F7E, #Bones
0x0F80, #DaemonBones
0x0E21, #bandage
0x26B7  #Zungi Fungus
]

loot_hue= [ #loot with color filter
# [ID , Hue]
[0x09B1, 0x0043], #GoldPan test
[0x0F8B, 0x0B94], #Moonstone



[0x0F45,0x076C], #Garg Axe
[0x13F6,0x0973], #Garg knife
[0x0E85,0x076C], #Garg pickaxe
[0x0E86,0x076C], #Garg pickaxe

#[0x0DCF,0x0000], #PlainSeeds

[0x1EA7,0x0032], #Gen of navigation

[0x0E36,0x0000], #IT Key - Desintegrated Notes

#[0x5736,0x048f], #Event Seed

#[0x26BC,0x01FC], #Queen Key - Purple
#[0x1439,0x00E8], #Queen Key - Red
#[0x0978,0x0556], #Queen Key - Blue
#[0x422C,0x00FD], #Queen Key - Yellow
#[0x1B12,0x0110], #Queen Key - Green
#[0x0E76,0x03C7], #Queen Key - Gray


#Indiana Jones
[0x14EB, 0x03E9], #Map
[0x0E76, 0x073E] #Bag of Sand

]
 
#loot_names = ['gargoyles','gargoyle'] #lootbag
loot_props = ['Artifact',
#'Rare',
#'Greater Magic',
#'Major Magic',
'of Forensics',
#'Uses Remaining',
'Ingeniously',
'Diabolically',
'Peerless Item',
'Peculiar Seed',
'Quest Item'] #lootbag


# SCRIPT

def findCorpses():
    corpse_list = Items.ApplyFilter(corpses_filter) # returns list of items, manipulate list after this as you wish
    return corpse_list

def lootCorpse(corpse):
    looted = False
    lotting = True
    while lotting:
        if not Player.InRangeItem(corpse,2):
                looted = False
                break
        lotting = False
        Items.WaitForContents(corpse,100)
        for item_to_loot in corpse.Contains:
            shouldLoot = False
            if checkItemByID(item_to_loot, loot_list):
                shouldLoot = True
            elif checkItemByHue(item_to_loot, loot_hue):
                shouldLoot = True
    #        elif checkItemByName(item_to_loot, loot_names):
    #            shouldLoot = True
            elif checkItemByCap(item_to_loot):
                shouldLoot = True
            elif checkItemByProperty(item_to_loot, loot_props):
                shouldLoot = True
            
            if shouldLoot:
                moveitem(item_to_loot, lootbag)
                
            elif checkItemByID(item_to_loot,loot_boh):
                shouldLoot = True
                moveitem(item_to_loot, boh)
               
            lotting = shouldLoot
            looted = looted or shouldLoot
            Misc.Pause(10)
        
    return looted
        
def checkItemByID(item_to_check, valid_ids):
    if item_to_check.ItemID in valid_ids:
        return True
    return False
    
def moveitem(item_to_move, dest_bag):
    Items.Move(item_to_move,dest_bag,-1 )
    Misc.Pause(350)

    
def checkItemByHue(item_to_check, valid_ids):
    if [item_to_check.ItemID,item_to_check.Hue] in valid_ids:
        return True
    return False
    
def checkItemByName(item_to_check, valid_names):
    for name in valid_names:
        if name.lower() in str(item_to_check.Name).lower():
            return True
    return False
    
def checkItemByCap(item_to_check):
    Items.WaitForProps(item_to_check,500)
    word=str(item_to_check.Properties)
    pos=str(item_to_check.Properties).find("bonus")
    if pos !=-1:
        #bonus = int(word[pos+len("bonus")+1:pos+len("bonus")+3].replace("]",""))
        bonus = int(word[pos+6:pos+8].replace("]",""))
        if bonus>8:
                return True
    pos1=str(item_to_check.Properties).find("Reagent Cost")
    if pos1 !=-1:
        #bonus = int(word[pos+len("bonus")+1:pos+len("bonus")+3].replace("]",""))
        lrc = int(word[pos1+13:pos1+15].replace("]",""))
        if lrc>18:
                return True
    return False
     
    
def checkItemByProperty(item_to_check, valid_props):
    Items.WaitForProps(item_to_check,500)
    prop = str(item_to_check.Properties)
    for name in valid_props:
        #for prop in item_to_check.Properties():
            if name.lower() in str(prop).lower():
                return True
    return False
    
def tooMuchWeight():
    Items.WaitForProps(backpack,5000)
    stuff = Items.GetPropStringByIndex(backpack,2)
    word=stuff.split()
    if len(word)>2:
        word=word[1]
        count=int(word.replace("/150",""))
        if (Player.Weight > 540) or count>145  :
            Player.HeadMessage(138, "Burp, Feeling full")
            Misc.Pause(200)
            Misc.WaitForContext(masterkey, 4000)
            Misc.ContextReply(masterkey, 2)  
            Misc.Pause(250)
            #clear Trash
            Misc.WaitForContext(0x4046ACAD, 10000)
            Misc.ContextReply(0x4046ACAD, 1)
            Misc.Pause(250)
        
def main(): # define the function
    crps_list = findCorpses()

    for current_corpse in crps_list:
        if not tooMuchWeight():
            #Items.Message(current_corpse,170,"loot this")
            if Player.InRangeItem(current_corpse,2):
                Items.UseItem(current_corpse)
                ignore = True
            Misc.Pause(250)
            ignore = lootCorpse(current_corpse)
            if not ignore and Player.InRangeItem(current_corpse,2) :
                Misc.IgnoreObject(current_corpse)
            Misc.Pause(50)
# RUN
while True:
    Journal.Clear()
    if Misc.ReadSharedValue("AL") and not Player.IsGhost :
        tooMuchWeight()
        main() #call the function
        Misc.Pause(100)
