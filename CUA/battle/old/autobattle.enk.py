import clr
import os
import System
import re
from Assistant import Engine
clr.AddReference('System.Core')
clr.ImportExtensions(System.Linq)


defaultCombatMode = 'cmode'
autoLootMacro = 'xxxxx'
microPause=25
minPause=150

combatModes = [
    {'name': 'cmode', 'attackAbility': 'secondary', 'targetRange': 2,'dress': 'cdress', 'nontargetActions':['Consecrate Weapon', 'Divine Fury', 'Evasion', 'Counter Attack'], 'targetedActions':['Honor', 'Enemy of One']},
    {'name': 'smode', 'attackAbility': 'Lighning Strike', 'targetRange': 2,'dress': 'sdress', 'autoActions':['autoHonor', 'xyz']},
    {'name': 'rmode', 'attackAbility': 'primary', 'targetRange':12,'dress': 'rdress', 'autoActions':['autoHonor', 'xyz']},
    {'name': 'pmode', 'attackAbility': None, 'targetRange': 10,'dress': 'sdress', 'autoActions':['autoHonor', 'xyz']},
    {'name': 'mmode', 'attackAbility': None, 'targetRange': 12,'dress': 'mdress', 'autoActions':['autoHonor', 'xyz']}
]

featuresToggles = {
    'autoHealingMode': 'on',
    'autoEvasionMode': 'on',
    'autoHonorMode': 'on',
    'autoCounterAttackMode': 'on',
    'autoEnemyOfOneMode': 'off',
    'lockChampionMode': 'on',
    'spsMode': 'off',
    'tpsMode': 'off',
    'jewelryMode': 'on',
    'preferredTypeTargeting': 'off'
}

delaysAndTimers = [
    {'name': 'consecrateWeapon', 'delay':9000},
    {'name': 'divineFury', 'delay':18000}
    
]

others = []

def GetConfig(config,field, criteria=None):
    if criteria:
        search = list(filter(lambda i: i[field] == criteria, config))
    else: 
        try:
            search = config[field]
        except:
            search = None
    if search: 
        if type(search) == list:
            return search[0]
        else:
            return search


cmode_config = GetConfig(combatModes, 'name', defaultCombatMode)
##print(getConfig(delaysAndTimers, 'name', 'divineFury'))
##exit()

def setTimer(timername, default_delay):
    if not TimerExists(timername):
        CreateTimer(timername)
        SetTimer(timername, default_delay)
    else: 
        SetTimer(timername, default_delay)

def CreateTimers():
    for timer in delaysAndTimers:
        createTimer(timer['name'], timer['delay'])


#func = getattr(self, method_name)           # find method that located within the class
#func()                                      # execute the method

# attack routine

class Enemy:
    def __init__(self, mobile):
        self._mobile = mobile
        self.is_boss = False
        #self.is_boss = self.getRealHits() > 1000
        #TODO: is_boss: Record self.getRealHits() onto a file to cache

    def is_low_hp(self):
        return Hits(self._mobile) < (MaxHits(self._mobile) * 0.01)

    def is_full_hp(self):
        return DiffHits(self._mobile) == 0
        
    def getRealHits(self):
        print("a")
        #if InJournal("You must wait", "system"):
        #    ClearJournal()
        #    Pause(5000)
        #    self.getRealHits()
        Pause(5000)       
        UseSkill("Animal Lore")
        WaitForTarget(1500)
        Target(self._mobile)
        
        if not GumpExists(0x934529aa):
            return (0, 0)

        res,gump = Engine.Gumps.GetGump(0x934529aa)
        if not res:
            return False
            
        element = gump.Pages[1].GetElementByXY(280,168)
        CloseGump(0x934529aa)

        if element == None:
            return (0, 0)

        matches = re.match('.*>(\d+)/(\d+)<.*', element.Text)

        if matches == None:
            return (0, 0)
            
        hp = int(matches.group(1))
        maxhp = int(matches.group(2))

        return (hp, maxhp)


class Enemies:
    def __init__(self):
        IgnoreObject("self")
        self.refresh()

    def refresh(self, search_distance=1):
        self._mobiles = self._find_enemies()
        if self._mobiles.current_target(): 
            SetAlias("currentTarget", self._mobiles.current_target().Serial)

    def are_amount_eq(self, number):
        return self._mobiles.Count() == number

    def are_amount_more(self, number):
        return self._mobiles.Count() > number

    def current_target(self):
        if self.are_amount_eq(0):
            return None

        target = self._mobiles.First()
        return target

    def _find_enemies(self, enemyNotorieties = ['Attackable', 'Enemy', 'Gray', 'Criminal', 'Murderer'], enemyMaxDistance = 22, orderBy = lambda m: m.Distance):
        return Engine.Mobiles.Where(lambda m: m.Distance < enemyMaxDistance
                                              and m.Serial != Engine.Player.Serial
                                              #and pets with happiness
                                              and (enemyNotorieties == None 
                                                    or enemyNotorieties.Contains(m.Notoriety.ToString())
                                                  )
                                ).OrderBy(orderBy) 



#=======

def activateOrCastAbility(abilityName):
    if abilityName in ['primary', 'secondary']:
        if not ActiveAbility():
            SetAbility(abilityName) 
    else: 
        Cast(abilityName)
        setTimer("castTimer", minCastDelay)

    Pause(minPause)
    

def handleCombatMode(enemy):
    if ability: activateOrCastAbility(ability)
    Pause(microPause)
    SetEnemyenemy.Serial) 
    Pause(microPause)
    Attack(enemy.Serial)
    Pause(minPause)
    
def autoConsecrateWeapon():
	if (Timer("consecrateWeaponTimer") >= 9000 and Timer("castDelayTimer") >= 1200):
		Cast("Consecrate Weapon")
		SetTimer("consecrateWeaponTimer", 0)
		SetTimer("castDelayTimer", 0)

def autoDivineFury():
	if (Timer("divineFuryTimer") >= 18000 and Timer("castDelayTimer") >= 1200):
		Cast("Divine Fury")
		SetTimer("divineFuryTimer", 0)
		SetTimer("castDelayTimer", 0)
            
def procActions(cmode_config):
	for action in cmode_config['autoActions']:
		globals()["auto{}".format(action.replace(' ', ''))]()
		
		
enemies = Enemies()
handleCombatMode(enemies.current_target)
procActions(cmode_config)