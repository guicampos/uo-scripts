from datetime import datetime, timedelta

SetQuietMode(True)

# ACSVC - python 
def configure():
    # characterName is the only MANDATORY thing to change:
    characterName = "Enkil Velland"  #Place here your Character Name including spaces. This is the heart of the voice command feature.
    # Logging. Pay atention to your Jounal when using the logger.
    logLevel = 5  # Defines a level of system messages. No messages = "0, Errors = "1, Warnings = "2, Info =3, Trace = "4, all messages = "5.

    # All toggles settings.  Change at will. 
    autoHealingMode = "on" # When "on", heal yourself using this macro system. If on, *You must disable your UOSteam self healing option (configure it to friends only)*
    autoDivineFury = "on"
    autoConsecrateWeapon = "on"
    autoEvasionMode = "on"  #Toggles autoEvasionMode feature. It will be enabled for all combat modes. "on" or "off"
    autoHonorMode = "on"  #Toggles autoHonorMode feature. "on" or "off".
    autoCounterAttackMode = "on"  #Toggles autoCounterAttackMode feature. "on" or "off".
    autoEnemyOfOneMode = "off"   #Toggles autoEnemyOfOneMode feature. "on" or "off".
    lockChampionMode = "off" # When "on", lock target on a champion boss whenever 2 titles away from it. "on" or "off"
    spsMode = "off"  # Toggles the auto Shield of Spikes on or off. "on" or "off". Still under testing.
    tpsMode = "off"  # Toggles the auto Triple Slash on or off. "on" or "off". Still under testing.
    autoLooter = "on"  # Enable or disable the jewelry looter feature. "on" or "off"
    preferredTypeTargeting = "off" # under development. When "on", allows to create a list of preferred mob types to lock. Read the help at the end of the file.

    # Combat related configuration. Remember: Excute the voice command ".reload" after any change.
    combatMode = "cmode"  #Your default Combat mode. Can be cmode or smode. More modes to come.
    cmodeSpecial = "secondary"  #Any ability or spell that affects in area. Recomended values: "primary","secondary" (for whirlwind weapons),"Momentum Strike", etc.
    smodeSpecial = "Lightning Strike"  #Any ability or spell that allows emphasize damage and to use on SMODE. Recomended values: "primary","secondary","Lightning Strike",<any fight spell> .

    # Timers and delay limits. Avoid changing.
    championMsgDelay = 10000  # Time between champion found warning.    
    healingDelay = 4000 # Check your [mystats for your perfect delay. 4000 is 4000 seconds
    healthLimit = 250 # The lowest health we should start healing
    divineFuryDelay = 19000  #How often Divine Fury will be toggled. Should be 18-21 seconds.
    consecrateWeaponDelay = 8000  #consecrate weapon delay timer. Adjust based on your Karma.
    autoEvasionDelay = 24000 # How often Evasion will be toggled. According to uo guide, delay should be 23-26 seconds.
    autoHonorDelay = 600 # How often Honor will be toggled. The script will honor only mobs with full HP
    autoHonorListCleanupDelay = 180000# How often the list of already honored creatures must be cleaned. 3 minutes is fine.
    autoEnemyOfOneDelay = 120000  # How often Enemy of One will be cast
    autoCounterAttackDelay = 10000 # How often Counter attack will be toggled.
    cmodeSpecialDelay = 1000  #how often script will use cmodeSpecial. This should be equal to your swing speed. check on [mystats ingame command.
    smodeSpecialDelay = 1000  #how often script will use smodeSpecial. This should be equal to your swing speed. check on [mystats ingame command.
    tpsModeDelay = 1300 # How often tps or sps will be used.
    spsModeDelay = 1300 # How often tps or sps will be used.
    actionsDelay = 300  #No need to change, unless your connection is slow it might be 1000
    castDelay = 1300  # Based on your cast speed and recovery value in milliseconds
    targetDelay = 1500
    resyncDelay = 8000

    # Other settings. Change at will.
    championMsgText = "↓†Champion†↓"  # A message to display over a champion when it appears.
    minSkillforLoot = 8 # How much of a skill a jewelry must have in order to be looted
    lootCorpseDistance = "2"  #Max Distance to loot a corpse.
    lootCorpseDelay = "600"  #Delay to retry looting.
    maxWeight = "550"  #What a weight limit to stop claiming corpses. UNSUSED. Still thinking a better implementation
    maxItemsCount = "130"  #What an items count to stop claiming corpses. UNSUSED. Still thinking a better implementation
    overweightWarningDelay = "20000"  #Time between overweight warning. UNSUSED. Still thinking a better implementation
    
    for name in dir():
        if not name.startswith('__'):
            myvalue = eval(name)
            print("set " + name + " to " + str(myvalue))
            setConf(name, myvalue)
    
    createAliases()
    createTimers()
    createLists()


def main():
    while not Dead("self"):
        if not ListExists("status") or InList("status", "setup") or InList("status", ""):
            SysMessage("Advanced Combat System with Voice Commands V 2.2 - BETA", 1990)
    
            configure()
            
            setConf("status", "execute")
    
        elif ListExists("status") and InList("status", "execute"):
            characterName = getConf("characterName") 
            logLevel = getConf("logLevel") 
            autoHealingMode = getConf("autoHealingMode") 
            autoDivineFury = getConf("autoDivineFury")
            autoConsecrateWeapon = getConf("autoConsecrateWeapon")
            autoEvasionMode = getConf("autoEvasionMode") 
            autoHonorMode = getConf("autoHonorMode") 
            autoCounterAttackMode = getConf("autoCounterAttackMode") 
            autoEnemyOfOneMode = getConf("autoEnemyOfOneMode") 
            lockChampionMode = getConf("lockChampionMode") 
            spsMode = getConf("spsMode") 
            tpsMode = getConf("tpsMode") 
            autoLooter = getConf("autoLooter") 
            preferredTypeTargeting = getConf("preferredTypeTargeting") 
            combatMode = getConf("combatMode") 
            cmodeSpecial = getConf("cmodeSpecial") 
            smodeSpecial = getConf("smodeSpecial") 
            championMsgDelay = getConf("championMsgDelay") 
            healingDelay = getConf("healingDelay") 
            healthLimit = getConf("healthLimit") 
            divineFuryDelay = getConf("divineFuryDelay") 
            consecrateWeaponDelay = getConf("consecrateWeaponDelay") 
            autoEvasionDelay = getConf("autoEvasionDelay") 
            autoHonorDelay = getConf("autoHonorDelay") 
            autoHonorListCleanupDelay = getConf("autoHonorListCleanupDelay") 
            autoEnemyOfOneDelay = getConf("autoEnemyOfOneDelay") 
            autoCounterAttackDelay = getConf("autoCounterAttackDelay") 
            cmodeSpecialDelay = getConf("cmodeSpecialDelay") 
            smodeSpecialDelay = getConf("smodeSpecialDelay") 
            tpsModeDelay = getConf("tpsModeDelay") 
            spsModeDelay = getConf("spsModeDelay") 
            actionsDelay = getConf("actionsDelay") 
            targetDelay = getConf("targetDelay")
            castDelay = getConf("castDelay") 
            resyncDelay = getConf("resyncDelay") 
            championMsgText = getConf("championMsgText") 
            minSkillforLoot = getConf("minSkillforLoot") 
            lootCorpseDistance = getConf("lootCorpseDistance") 
            lootCorpseDelay = getConf("lootCorpseDelay") 
            maxWeight = getConf("maxWeight") 
            maxItemsCount = getConf("maxItemsCount") 
            overweightWarningDelay = getConf("overweightWarningDelay") 
            # Lists
            SkillList1 = GetList("SkillList1")
            SkillList2 = GetList("SkillList2")
    
            # Constants
            spsGumpID = 0x4239a64f
            tpsGumpID = 0x7ec42f38
    
    
            # A greet.
            log("System Executing", 0)
            
            # reseting timers and status
            ClearIgnoreList()
            SetTimer("loopTime", 0)
    
            # ==============================
            # ======= MAIN LOOP ========
            # ==============================
            while not Dead("self"):
                Pause(600)
                SetTimer("loopTime", 0)

                if Dead("self"):
                    HeadMsg("-=|Dead men tell no tales. Nor play macros|=-", "self", 1990)
                    Stop()

                if InJournal(".halt", characterName):
                    HeadMsg("Ok. Halt.", "self", 1990)
                    ClearJournal()
                    Stop()
    
                if InJournal(".reload", characterName):
                    RemoveList("status")
                    ClearJournal()
                    break
                
                # Proc autoDivineFury
                # Healing here, so you can use UO Steam to heal your friends
                if autoHealingMode == "on" and ((Poisoned("self") or Hits("self") <= healthLimit) and Timer("healingDelayTimer") >= healingDelay):
                    log("BandageSelf (autoHealingMode is on)", 3)
                    BandageSelf()
                    SetTimer("healingDelayTimer", 0)
    
   
                # START ACQUIRING TARGET
                # Our target will be always the closest from us
                GetEnemy(["murderer", "enemy", "gray", "criminal"], "any", "closest")
                SetAlias("finalEnemy","enemy")
                finalEnemy = GetAlias("FinalEnemy")
    
    
                if finalEnemy:
                    if autoHonorMode == "on" and (InRange(finalEnemy, 6) and Timer("autoHonorTimer") >= autoHonorDelay and not InList("autoHonorList", finalEnemy) and DiffHits(finalEnemy)  == 0):
                       log("Executing autoHonorMode (ON)", 2)
                       InvokeVirtue("honor")
                       WaitForTarget(targetDelay)
                       Target(finalEnemy, False, False) 
                       PushList("autoHonorList", finalEnemy)
                       SetTimer("autoHonorTimer", 0)
    
                    if combatMode == "cmode":
                        if cmodeSpecial == "primary" or cmodeSpecial == "secondary":
                            if Timer("cmodeSpecialTimer") >= cmodeSpecialDelay:
                                # print("Timer(\"cmodeSpecialTimer\") >= cmodeSpecialDelay = {0} >= {1}".format(Timer("cmodeSpecialTimer"), cmodeSpecialDelay))
                                cmodeSpecialDelay = getConf("cmodeSpecialDelay")
                                log("SetAbility cmodeSpecial ({0})".format(cmodeSpecial), 4)
                                SetTimer("cmodeSpecialTimer", 0)
                                SetAbility(cmodeSpecial, "on")
                        else:
                            if Timer("cmodeSpecialTimer") >= cmodeSpecialDelay:
                                log("cast cmodeSpecial ({0})".format(cmodeSpecial), 4)
                                Cast(cmodeSpecial)
                                SetTimer("cmodeSpecialTimer", 0)
    
                    elif combatMode == "smode":
                        if smodeSpecial == "primary" or smodeSpecial == "secondary":
                            if not ActiveAbility() and Timer("cmodeSpecialTimer") >= smodeSpecialDelay:
                                log("SetAbility smodeSpecial ({0})".format(smodeSpecial), 4)
                                SetAbility(smodeSpecial, "on")
                        else:
                            if Timer("smodeSpecialTimer") >= smodeSpecialDelay:
                                log("cast smodeSpecial ({0})".format(smodeSpecial), 4)
                                Cast(smodeSpecial)
                                SetTimer("smodeSpecialTimer", 0)
                    else:
                        # oops, combatMode should never "else" anything. Assuming the default cmode
                        ClearList("combatMode")
                        PushList("combatMode", "cmode")
    
                    #-----Attack!-----------
                    Attack("finalEnemy")

                    # Auto autoCounterAttackMode
                    if autoCounterAttackMode == "on" and (Timer("autoCounterAttackTimer") >= autoCounterAttackDelay and Timer("castDelayTimer") >= castDelay and Timer("autoEvasionTimer") >= 8300):
                        log("Counter Attack (autoCounterAttackMode is on)", 3)
                        Cast("Counter Attack")
                        SetTimer("autoCounterAttackTimer", 0)
                        SetTimer("castDelayTimer", 0)


                    # Proc autoDivineFury
                    if autoDivineFury == "on" and (Timer("divineFuryTimer") >= divineFuryDelay and Timer("castDelayTimer") >= castDelay):
                        log("Divine Fury (autoDivineFury is on)", 3)
                        Cast("Divine Fury")
                        SetTimer("castDelayTimer", 0)
                        cmodeSpecialDelay = 2250
                        SetTimer("divineFuryTimer", 0)
                        

                    # Proc autoEvasionMode
                    if autoEvasionMode == "on" and (Timer("autoEvasionTimer") >= autoEvasionDelay and Timer("castDelayTimer") >= castDelay):
                        log("Casting Evasion (autoEvasionMode is on)", 3)
                        Cast("evasion") 
                        SetTimer("autoEvasionTimer", 0)
                        SetTimer("castDelayTimer", 0)

                    # Proc autoConsecrateWeapon
                    if autoConsecrateWeapon == "on" and (Timer("consecrateWeaponTimer") >= consecrateWeaponDelay and Timer("castDelayTimer") >= castDelay):
                        log("Casting Consecrate Weapon (autoConsecrateWeapon is on)", 3)
                        Cast("Consecrate Weapon")
                        SetTimer("consecrateWeaponTimer", 0)
                        SetTimer("castDelayTimer", 0)
                        cmodeSpecialDelay = 1250

                    # Proc EnemyOfOne
                    if autoEnemyOfOneMode == "on" and (Timer("autoEnemyOfOneTimer") >= autoEnemyOfOneDelay and Timer("castDelayTimer") >= castDelay): 
                        log("Casting Enemy of One (autoEnemyOfOneMode is on)", 3)
                        Cast("enemy of one")
                        SetTimer("autoEnemyOfOneTimer", 0)
                        SetTimer("castDelayTimer", 0)
                #-------Messages-Handling-----
                # Message service should be the last in loop
                #help
                
                if InJournal(".timers",characterName):
                    ClearJournal()
                    actionsDelayTimer = timedelta(milliseconds=Timer("actionsDelayTimer"))
                    autoCounterAttackTimer = timedelta(milliseconds=Timer("autoCounterAttackTimer"))
                    autoEnemyOfOneTimer = timedelta(milliseconds=Timer("autoEnemyOfOneTimer"))
                    autoEvasionTimer = timedelta(milliseconds=Timer("autoEvasionTimer"))
                    autoHonorListCleanupTimer = timedelta(milliseconds=Timer("autoHonorListCleanupTimer"))
                    autoHonorTimer = timedelta(milliseconds=Timer("autoHonorTimer"))
                    castDelayTimer = timedelta(milliseconds=Timer("castDelayTimer"))
                    championMSGTimer = timedelta(milliseconds=Timer("championMSGTimer"))
                    cmodeSpecialTimer = timedelta(milliseconds=Timer("cmodeSpecialTimer"))
                    consecrateWeaponTimer = timedelta(milliseconds=Timer("consecrateWeaponTimer"))
                    discordanceDelayTimer = timedelta(milliseconds=Timer("discordanceDelayTimer"))
                    loopTime = timedelta(milliseconds=Timer("loopTime"))
                    lootCorpseTimer = timedelta(milliseconds=Timer("lootCorpseTimer"))
                    overweightWarningTimer = timedelta(milliseconds=Timer("overweightWarningTimer"))
                    smodeSpecialTimer = timedelta(milliseconds=Timer("smodeSpecialTimer"))
                    spsModeTimer = timedelta(milliseconds=Timer("spsModeTimer"))
                    tpsModeTimer = timedelta(milliseconds=Timer("tpsModeTimer"))
                    HeadMsg("""
    actionsDelayTimer: {0}
    autoCounterAttackTimer: {1}
    autoEnemyOfOneTimer: {2}
    autoEvasionTimer: {3}
    autoHonorListCleanupTimer: {4}
    autoHonorTimer: {5}
    castDelayTimer: {6}
    championMSGTimer: {7}
    cmodeSpecialTimer: {8}
    consecrateWeaponTimer: {9}
    discordanceDelayTimer: {10}
    loopTime: {11}
    lootCorpseTimer: {12}
    overweightWarningTimer: {13}
    smodeSpecialTimer: {14}
    spsModeTimer: {15}
    tpsModeTimer: {16}                
                    """.format(actionsDelayTimer, autoCounterAttackTimer, autoEnemyOfOneTimer, autoEvasionTimer, autoHonorListCleanupTimer, autoHonorTimer, castDelayTimer, championMSGTimer, cmodeSpecialTimer, consecrateWeaponTimer, discordanceDelayTimer, loopTime, lootCorpseTimer, overweightWarningTimer, smodeSpecialTimer, spsModeTimer, tpsModeTimer) , "self", 0)
                    
                # General Report Mode
                if InJournal(".status", characterName):
                    ClearJournal()
                    HeadMsg("""
    Combat Mode: {0}
    AutoEvasion: {1}
    AutoCounterAttack: {2}
    AutoHonorMode: {3}
    AutoEnemyOfOne: {4}
    AutoTps: {5}
    AutoSps: {6}
    AutoLooter: {7}
    """.format(combatMode, autoEvasionMode, autoCounterAttackMode, autoHonorMode, autoEnemyOfOneMode, tpsMode, spsMode, autoLooter), "self", 0)
    
    
                # Proc autoLooter
                if autoLooter == "on" and FindType(0x2006,2, "ground", -1, 0 ):
                    SetAlias("corpse", "found")
                    #if Timer("lootCorpseTimer") >= lootCorpseDelay:
                    UseObject("corpse")
                    #SetTimer("lootCorpseTimer", 0)
                    IgnoreObject("corpse")
    
    
                    for graphic in GetList("jewelryList"):
                        for i in range(0,5):
                            if FindType(graphic,-1, "corpse", -1, 0):
                                WaitForProperties("found", 2000)
                                for skill1 in SkillList1:
                                    if Property(skill1, "found") >= minSkillforLoot:
                                        SkillList2.pop(skill1)
                                        for skill2 in SkillList2:
                                            if Property(skill2, jewelryFound) >= minSkillforLoot:
                                                SysMessage("Found Jewelry with {0} and {1} > {2}".format(skill1, skill2, minSkillforLoot), 1990)
                                                if not InList("shouldLoot","found"):
                                                    PushList("shouldLoot", "found")
                                                    break
                                        SkillList2.append(skill1)
                                        if InList("shouldLoot","found"):
                                            break
                                IgnoreObject("found")
    
                    # Proc lootList
                    if len(GetList("shouldLoot")) > 0:
                        for item in GetList("shouldLoot"):
                            if Timer("lootCorpseTimer") >= lootCorpseDelay:
                                MoveItem(item, "lootBag")
                                SetTimer("lootCorpseTimer", 0)
                                if FindObject(item, "lootBag"):
                                    Msg("[e yea")
                                    HeadMsg("».«", item, 1990)
                                    PopList("shouldLoot", item)
                                    IgnoreObject(item)
    
    
    
                if Timer("autoHonorListCleanupTimer") >= autoHonorListCleanupDelay:
                    SetTimer("autoHonorListCleanupTimer", 0)
                    ClearList("autoHonorHonoredList")
    
                if InJournal(".ah", characterName):
                    autoHealingMode = setConf("autoHealingMode",  "on") if autoHealingMode == "off" else setConf("autoHealingMode",  "off")
                    HeadMsg("Auto Healing is now {0}".format(autoHealingMode.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".hon", characterName):
                    autoHonorMode = setConf("autoHonorMode",  "on") if autoHonorMode == "off" else setConf("autoHonorMode",  "off")
                    HeadMsg("Auto Honor is now {0}".format(autoHonorMode.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".eva", characterName):
                    autoEvasionMode = setConf("autoEvasionMode",  "on") if autoEvasionMode == "off" else setConf("autoEvasionMode",  "off")
                    HeadMsg("Auto Evasion is now {0}".format(autoEvasionMode.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".ca", characterName):
                    autoCounterAttackMode = setConf("autoCounterAttackMode",  "on") if autoCounterAttackMode == "off" else setConf("autoCounterAttackMode",  "off")
                    HeadMsg("Auto Counter Attack is now {0}".format(autoCounterAttackMode.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".eoo", characterName):
                    autoEnemyOfOneMode = setConf("autoEnemyOfOneMode",  "on") if autoEnemyOfOneMode == "off" else setConf("autoEnemyOfOneMode",  "off")
                    HeadMsg("Auto Enemy of One is now {0}".format(autoEnemyOfOneMode.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".al", characterName):
                    autoLooter = setConf("autoLooter",  "on") if autoLooter == "off" else setConf("autoLooter",  "off")
                    HeadMsg("Auto Looter is now {0}".format(autoLooter.upper()), "self", 1990)
                    ClearJournal()
    
                if InJournal(".gg", characterName): 
                    ClearJournal()
                    while FindType(0xeed, 8, "ground", -1, 1):
                        UseObject("found")
    
                if InJournal(".help", characterName):
                    ClearJournal()
                    SysMessage("""
    Help for Advanced Combat System with Voice Commands.
    Available Commands. All commands starts with ".". 
    -=|Combat Modes|=-
    .cmode - switch to the champion mode
    .smode - switch to the single mode
    .pmode - switch to the pet mode
    -=|Combat Configurations|=-
    .ah  - Toggles Auto Healing
    .eva - Toggles Auto Evasion
    .ca  - Toggles Auto Counter Attack
    .hon - Toggles Auto Honor
    .eoo - Toggles Auto Enemy of One
    .eq1 - Equips your main melee weapons
    .eq2 - Equips your main ranged weapon
    -=|Reports|=-
    .status - shows ON JOUNAL the status for all voice commands features
    .timers - shows ON JOUNAL the time of all timers
    -=|Special attacks|=-
    .sps - toggles the auto Shield of Spikes feature (in development)
    .tps - toggles the Triple Slash feature (in development)
    -=|Auto Looter|=-
    .al - toggles the auto looter feature
    .gg - grabs all in range gold piles.
    -=|SETUP|=-
    .reload - Reset all the setups and start over. *Executed after any changes to settings.*
    .halt - Stop and exit the system
    """, 0)
    
                if InJournal(".eq1", characterName):
                    Dress("melee")
                    ClearJournal()
    
                if InJournal(".eq2", characterName): 
                    Dress("Ranged")
                    ClearJournal()
       
                if InJournal(".help", characterName):
                    ClearJournal()
                    SysMessage("""
    Help for Advanced Combat System with Voice Commands.
    Available Commands. All commands starts with ".". 
    -=|Combat Modes|=-
    .cm - switch to the champion mode
    .sm - switch to the single mode
    -=|Combat Configurations|=-
    .ah  - Toggles Auto Healing
    .eva - Toggles Auto Evasion
    .ca  - Toggles Auto Counter Attack
    .hon - Toggles Auto Honor
    .eoo - Toggles Auto Enemy of One
    .eq1 - Equips your main melee weapons
    .eq2 - Equips your main ranged weapon
    -=|Reports|=-
    .status - shows ON JOUNAL the status for all voice commands features
    .timers - shows ON JOUNAL the time of all timers
    -=|Special attacks|=-
    .sps - toggles the auto Shield of Spikes feature (in development)
    .tps - toggles the Triple Slash feature (in development)
    -=|Auto Looter|=-
    .al - toggles the auto looter feature
    .gg - grabs all in range gold piles.
    -=|SETUP|=-
    .reload - Reset all the setups and start over. *Executed after any changes to settings.*
    .halt - Stop and exit the system
    """, 1990)
    
                if InJournal(".eq1", characterName):
                    Dress("melee")
                    ClearJournal()
    
                if InJournal(".eq2", characterName): 
                    Dress("ranged")
                    ClearJournal()
    
                # set Combat Mode
                if InJournal(".cm", characterName):
                    ClearJournal()
                    combatMode = setConf("combatMode",  "cmode")
                    HeadMsg("SWITCHED TO CHAMPION MODE", "self", 1990)
                elif InJournal(".sm", characterName):
                    ClearJournal()
                    combatMode = setConf("combatMode",  "smode")
                    HeadMsg("SWITCHED TO SINGLE MODE", "self", 1990)



def setConf(configuration_name, configuration_value):
    ClearList(configuration_name) if ListExists(configuration_name) else CreateList(configuration_name)
    PushList(configuration_name, configuration_value)
    return configuration_value
    
def getConf(configuration_name):
    if ListExists(configuration_name) and List(configuration_name) > 0:
        return GetList(configuration_name)[0]

def log(msg, level):
    logLevel = getConf("logLevel")
    if logLevel >= level:
        SysMessage(msg,0)

def createAliases():
    # User defined serials
    if not FindAlias("lootBag"):
        PromptAlias("lootBag")

def createLists():
    CreateList("autoHonorList")
    CreateList("shouldLoot")
    # preferred targets
    #Champion bosses
    CreateList("bossList")
    ClearList("bossList")
    PushList("bossList", 0xAC)  # Riktor
    PushList("bossList", 0xAE)  # Semidar
    PushList("bossList", 0xF9)  # Serado
    PushList("bossList", 0xAD)  # Mephitis
    PushList("bossList", 0x33e) # Priveval Lich
    PushList("bossList", 0xAF)  # Angel Champ
    #missing: Lord Oaks, Neira, Barracoon, Harrower, Serado, Abyssal,  Pirate Davy Jones
    PushList("bossList", 0xcc)  # A horse. Just for fun and testing. Remove at will
    CreateList("jewelryList")
    ClearList("jewelryList")
    PushList("jewelryList", 0x108a)
    PushList("jewelryList", 0x1f09)
    PushList("jewelryList", 0x1086)
    PushList("jewelryList", 0x1f06)
    ClearList("SkillList1")
    PushList("SkillList1", "Animal Taming")
    PushList("SkillList1", "Mace Fighting")
    PushList("SkillList1", "Archery")
    PushList("SkillList1", "Swordsmanship")
    PushList("SkillList1", "Magery")
    PushList("SkillList1", "Spirit Speak")
    PushList("SkillList1", "Necromancy")
    PushList("SkillList1", "Animal Lore")
    PushList("SkillList1", "Anatomy")
    PushList("SkillList1", "Tactics")
    PushList("SkillList1", "Evaluating Intelligence")
    PushList("SkillList1", "Parrying")
    PushList("SkillList1", "Bushido")
    PushList("SkillList1", "Healing")
    PushList("SkillList1", "Focus")
    PushList("SkillList1", "Meditation")
    PushList("SkillList1", "Musicianship")
    CreateList("SkillList2")
    ClearList("SkillList2")
    PushList("SkillList2", "Animal Taming")
    PushList("SkillList2", "Mace Fighting")
    PushList("SkillList2", "Archery")
    PushList("SkillList2", "Swordsmanship")
    PushList("SkillList2", "Magery")
    PushList("SkillList2", "Spirit Speak")
    PushList("SkillList2", "Necromancy")
    PushList("SkillList2", "Animal Lore")
    PushList("SkillList2", "Anatomy")
    PushList("SkillList2", "Tactics")
    PushList("SkillList2", "Evaluating Intelligence")
    PushList("SkillList2", "Parrying")
    PushList("SkillList2", "Bushido")
    PushList("SkillList2", "Healing")
    PushList("SkillList2", "Focus")
    PushList("SkillList2", "Meditation")
    PushList("SkillList2", "Musicianship")

def createTimers():
    CreateTimer("actionsDelayTimer")
    CreateTimer("autoCounterAttackTimer")
    CreateTimer("autoEnemyOfOneTimer")
    CreateTimer("autoEvasionTimer")
    CreateTimer("autoHonorListCleanupTimer")
    CreateTimer("autoHonorTimer")
    CreateTimer("castDelayTimer")
    CreateTimer("championMSGTimer")
    CreateTimer("cmodeSpecialTimer")
    CreateTimer("consecrateWeaponTimer")
    CreateTimer("discordanceDelayTimer")
    CreateTimer("divineFuryTimer")
    CreateTimer("healingDelayTimer")
    CreateTimer("loopTime")
    CreateTimer("lootCorpseTimer")
    CreateTimer("overweightWarningTimer")
    CreateTimer("smodeSpecialTimer")
    CreateTimer("spsModeTimer")
    CreateTimer("tpsModeTimer")
    CreateTimer("resyncTimer")


main()

