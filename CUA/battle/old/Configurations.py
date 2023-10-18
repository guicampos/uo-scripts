from configparser import ConfigParser
SetQuietMode(True)

class Configuration:
    config_file = 'configs.cfg'    
    persisConfigurations = ['autoHealingMode' ,'autoDivineFury' ,'autoConsecrateWeaponMode' ,'autoEvasionMode' ,'autoHonorMode' ,'autoCounterAttackMode' ,'autoEnemyOfOneMode' ,'autoLockChampionMode' ,'autoSpsMode' ,'autoTpsMode' ,'autoLooterMode' ,'AutoTypeTargetingMode' ,'combatMode']
    def __init__(self):
        parser = ConfigParser()
        parser.optionxform = str  # case sensitive
        found = parser.read(self.config_file)
        if not found:
            raise ValueError('No config file found!')
        for name in parser.sections():
            self.__dict__.update(parser.items(name))
            for config in parser.items(name):
                print(config)
                if config[0] in persisConfigurations:
                    self.persistConfig(config[0], config[1])
        self.
        self.setupAliases()
        SysMessage("Advanced Combat System with Voice Commands V 2.2 - BETA", 1990)


    def reload(self):
        self.__init__()

    def setPersistConfig(self, configuration_name, configuration_value):
        if configuration_name not in persisConfigurations:
            raise Exception("{} is not a valid configuration to be persisted.".format(configuration_name))
        ClearList(configuration_name) if ListExists(configuration_name) else CreateList(configuration_name)
        PushList(configuration_name, configuration_value)

    def getPersistConfig(self, configuration_name):
        if configuration_name not in persisConfigurations:
            raise Exception("{} cannot be returned because it is not a valid configuration persisted.".format(configuration_name))
        if ListExists(configuration_name) and List(configuration_name) > 0:
            return GetList(configuration_name)[0]

    def setupAliases(self):
        if not FindAlias("lootBag"):
            PromptAlias("lootBag")

    def processConfigurations(self):
        self.actionsList = self.actionsList.split(",")