from Assistant import Engine
import re
import clr
import System
clr.AddReference("System.Core")
clr.ImportExtensions(System.Linq)


class Enemy:
    def __init__(self, mobile):
        self._mobile = mobile
        self.is_boss = MaxHits(mobile) > 10000

    def is_low_hp(self):
        return Hits(self._mobile) < (MaxHits(self._mobile) * 0.01)

    def is_full_hp(self):
        return DiffHits(self._mobile) == 0

class Enemies:
    def __init__(self):
        IgnoreObject("self")
        self.refresh()

    def refresh(self, search_distance=1):
        self._mobiles = self._find_enemies(search_distance)

    def are_amount_eq(self, number):
        return self._mobiles.Count() == number

    def are_amount_more(self, number):
        return self._mobiles.Count() > number

    def boss_here(self):
        for mob in self._mobiles:
            if Enemy(mob).is_boss:
                return True
        return False

    def current_target(self):
        if self.are_amount_eq(0):
            return None

        target = self._mobiles.First().Serial
        if target == GetAlias('self'):
            return None
        else:
            return target

    def _find_enemies(self, enemyNotorieties = ['Attackable', 'Enemy', 'Gray', 'Criminal', 'Murderer'], maxDistance = 32, filter = lambda m: m.Distance):
        return Engine.Mobiles.Where(lambda m: m != None
                                    and (enemyNotorieties == None 
                                              or enemyNotorieties.Contains(m.Notoriety.ToString()))
                                    and m.Distance <= maxDistance
                                    and not InIgnoreList(m.Serial)
                                    ).OrderBy(filter)
        Pause(10)
