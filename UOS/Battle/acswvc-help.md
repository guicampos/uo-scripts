# Velland's Combat System with Voice Commands V 2.2.14112022 - Steam version

Release Notes for Version 2.2.14112022

## USAGE:
1. Create a new macro on your UO STEAM, paste the script, name it (suggestion: vcswvc ) and save.
2. Review all the default options and features at the start of the script.
   - Put your name on @pushlist 'characterName' variable
   
    **Example: @pushlist 'characterName' 'Velland'**
      
   - Feel free to alter any other configuration value
   - Change only the last value. For exemple, change only 'off' to 'on' in @pushlist 'autoHealingMode' 'off'  <-- Change this only 
3. Create 2 Dress Agents with option 'Move Conflicting Items' marked. Name each of the dress agent as:
     - melee : with your melee weapons
     - ranged: with your favorite bow
4. Assign a hot key for 'vcswvc'.
5. Assign a stop macro button to stop it when you need to  (or use the voice command '.halt')
6. Run and follow the steps.

## Warnings

* I am not responsible for the use you make out of this system.
* I am not responsible for the pauses and features you chose to use.
* You are responsible for reading all comments on the script.
* Having found any bug or problem, please contact me at discord *guicampos#6410*
* **DO NOT USE THIS SYSTEM TO STAY AFK WHILE KILLING MONSTERS OR OTHER PvM ACTIVITIES.**
* **I DO NOT SUPPORT AFK RESOURCE GATHERING.**

## Features

### Passives

**Silent Mode**
Makes the script stop spamming spells and attacks if no enemy ir nearby.

   Comments: Passive and always on.
   
**World Saves Pauses**
Suspends the script temporarily during world save pauses.

   Comments: Passive and always on.

### Active Features   

### Reporting
Shows informations about the system and it's state

      Commands:
         .status: Shows on your journal the status of each feature.
         .timers: Shows on your journal all timers for debuging.

### Logging:
There are 5 levels of Logging. Set it on @pushlist 'logLevel' 'X', where X is:

      No messages = 0, Errors = 1, Warnings = 2, Info =3, Trace = 4, all messages = 5
      **Note**: Run the system on logLevel 5 for a while at the begining.

### Auto Setup:
Initial setup of the system is very simple.
All configurations and values are persistent and durable, meaning that you can close your UO and everything will be the same when you come back.

      Commands:
         .reload - Forces all variables, lists and timers to be reloaded and repopulated. You should execute this after changing any value from the script.
         .halt - Forces the system to stop.

### Targeting:
This system improves targeting for you. It will identify most of the champions.

      Configurations:
         championMsgText: A text to show when a champion is found
         championMsgDelay: A timer to prevent spam the champion found message

### Lock Champion
When 'on', this feature will identified champion bosses to help you targeting it.

      Commands:
         .lc
         
### Auto Healing
Heals yourself using bandages
      
      Voice Command: 
         .ah
         
      Comments: *You must disable your UOSteam self healing option (configure it to friends only)*
      
      Configurations:
         autoHealingMode: 'on' turns on, 'off' turns off
         healingDelay: time between bandages
         healthLimit: min health to start healing

### Combat Modes:
**Champion mode**
Enables a combat mode focused on group battles
      
      Voice Command: 
         .cmode
         
         Comments: starts spamming whirlwind attack
         
         Configurations:
            cmodeSpecial: Ability or spell name, like 'secondary' or 'Momentum Strike'. Always use any powerful group move
            cmodeSpecialRate: How often, in milliseconds, should this special move be cast
            
**Single Mode**
Enables a combat mode oriented on 1x1 (pvm) battles

         Voice Command: 
            .smode
         
         Comments: Starts spamming your primary hability or Lighting Strike
         
         Configurations:
            smodeSpecial: Ability or spell name, like 'primary' or 'Lighting Strike'. Always use any powerful 1x1 move
            smodeSpecialRate: How often, in milliseconds, should this special move be cast

### Auto Divine Fury
      Autocast Divine fury
      
      Voice Command: None. Always on.
      
      Configurations:
         divineFuryDelay: How often, in milliseconds, should Divine Fury be cast
         
### Auto Consecrate Weapon:
      Auto cast Consecrate Weapon
      
      Voice Command: None. Always on.
      Configurations:
         consecrateWeaponDelay: How often, in milliseconds, should consecrate Weapon be cast

### Auto Evasion
      Toggles automatically cast Evasion

      Voice command: 
         .eva
      
      Configurations:
         autoEvasionDelay: How often, in milliseconds, should Evasion be cast

      Notes: Check Evasion delays and durations on the web.
      
### Auto Counter Attack:
      Toggles automatically cast Counter Attack syncronous with Evasion
      
      Voice Command: 
         .ca
      
      Notes: Counter attack will be cast only when Evasion is on delay
      
      Configurations:
         autoCounterAttackDelay: How often, in milliseconds, should Counter Attack be cast. Note that it won't be casted when Evasion is on effect.

### Auto Honor:
      Toggles automatically mark enemies with Honor.
      
      Notes: Make sure that possible targets have line of sight all the time.
      Voice Command: 
         .hon
         
      Configurations:
         autoHonorDelay: How often, in milliseconds, should we honor targets
         autoHonorHonoredListCleanupDelay: How often should we cleanup the honor list.

### Auto Discordance:
      Toggles Auto Discordance.
      
      Notes: Make sure that possible targets have line of sight all the time.
      Voice Command: 
         .ad
         
      Configurations:
         autoDiscordanceMode: if auto discordance is enabled or disabled by default.
         autoDiscordanceDelay: How often should targets be discorded.
         instrumentGraphic: Graphic Hex Code for a musical instrument inside your backpack
         instrumentGraphic: Color Hex Code for a musical instrument inside your backpack

### Auto Enemy of One:
      Toggles automatically cast Enemy of One on a timed basis

      Voice Command: 
         .eoo
         
      Configurations:
         autoEnemyOfOneDelay: How often Enemy of One should be cast

### Auto Looter
Toggles the Jewelry Looter feature.
The auto looter will loot: 
   - Jewelry with howManySkillsforLoot >= minSkillforLoot
   - Peerless quest items.

    Voice Command: 
        .jl
         
    Note: It will open corpses and loot jewelry with more than 'minSkillforLoot' on a selected list of skills.
    
    Configurations:
     minSkillforLoot: Will loot jewelry with at list this amount of skill.
     howManySkillsforLoot: How many wanted skill above or equal 'minSkillforLoot' the jewelry should have in order to be grabbed?
     lootCorpseDistance: Will look from this distance.
     lootCorpseDelay: Delay between loots.

#### Auto Claim
Part of the Auto Looter system.
When 'on', makes every corpse to be claimed at the end of the auto looter system.
      
      Voice Command: 
         .ac


### Gold Grabber
Makes your character grab all gold piles from the ground.

      Voice command: 
         .gg

### Equipment Helper
Helps you to dress a correct set of gear on the correct order

      Voice Commands:
         .eq1: Force equip your main melee weapons (dress agent 'melee')
         .eq2: Force equip your ranged weapon (dress agent 'ranged')

## Other features 
This system has other features that cannot be seen but makes lots of difference.

- Pauseless: This system uses a timed semaphore algorithm that allows using the least pauses possible, making it blazing fast and reliable.
- One Script To Rule Them All: One script that centralize your battle gameplay should change your gaming experience. No more repetitive clicks or casting the same spells everytime.
- Community thinking: Everyone using the same base script so everyone can help each other and implement features to be used by everyone.
- Simplicity: All features are implemented with simple and common uosteam functions. 
- Reliable: Simple to understand and maintain, serving as a real framework to add more features.
- Sampire routine: Implements a well known sampire battle routine, capable of fitting the fighiting styles of swords/parry or swords/bushido builds.

## Known Issues:
- tps not working properlly when failed

## Todo:
- v2.3 - Make a reliable triple slash

