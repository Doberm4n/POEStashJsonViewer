from __future__ import division
import re
import traceback



class DPSCalc():

    def __init__(self):
        self.patternStringQuality = 'Quality: +'
        self.patternStringPhysical = 'Physical Damage:'
        self.patternStringChaos = 'Chaos Damage:'
        self.patternStringFire = 'Adds\s\d+\s+to\s\d+\s+Fire Damage'
        self.patternStringLightning = 'Adds\s\d+\s+to\s\d+\s+Lightning Damage'
        self.patternStringCold = 'Adds\s\d+\s+to\s\d+\s+Cold Damage'
        self.patternStringAttacksPerSecond = 'Attacks per Second:'
        self.patternStringIncreasedPhysicalDamage = '% increased Physical Damage'
        self.patternStringCorrupted = 'isCorrupted'


    def searchPattern(self, pattern, data):
        pattern = re.compile(pattern)
        self.modifier = filter(pattern.search, data.splitlines())


    def Split(self, isAugmented):
        if isAugmented:
            self.values = self.modifier[0].split('-', 1)
        else:
            self.values = self.modifier[0].split('to', 1)


    def Calc(self, data):
        try:
            self.searchPattern(self.patternStringQuality, data)
            if self.modifier:
                self.valueQuality = int(filter(str.isdigit, str(self.modifier[0])))
            else:
                self.valueQuality = 0
            self.searchPattern(self.patternStringIncreasedPhysicalDamage, data)
            if self.modifier:
                self.valueIncreasedPhysicalDamage = int(filter(str.isdigit, str(self.modifier[0])))
            else:
                self.valueIncreasedPhysicalDamage = 0
            self.searchPattern(self.patternStringAttacksPerSecond, data)
            if self.modifier:
                self.values = self.modifier[0].split(':', 1)
                self.values = self.values[1].split('(', 1)
                self.valueAttacksPerSecond = float(self.values[0])
            else:
                self.valueAttacksPerSecond = 0
            self.searchPattern(self.patternStringCorrupted, data)
            if self.modifier:
                self.valueIsCorrupted = True
            else:
                self.valueIsCorrupted = False
            self.searchPattern(self.patternStringPhysical, data)
            if self.modifier:
                self.Split(True)
                if not self.valueIsCorrupted:
                    temp = ((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2) / (1+1/100*(self.valueIncreasedPhysicalDamage+self.valueQuality))
                    self.valuePhysical = round(temp * (1+1/100*(self.valueIncreasedPhysicalDamage+20)) * self.valueAttacksPerSecond, 1)
                else:
                    self.valuePhysical = round((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2, 1)
            else:
                self.valuePhysical = 0
            self.searchPattern(self.patternStringChaos, data)
            if self.modifier:
                self.Split(True)
                self.valueChaos = round((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2 * self.valueAttacksPerSecond, 1)
            else:
                self.valueChaos = 0
            self.searchPattern(self.patternStringFire, data)
            if self.modifier:
                self.Split(False)
                self.valueFire = round((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2 * self.valueAttacksPerSecond, 1)
            else:
                self.valueFire = 0
            self.searchPattern(self.patternStringLightning, data)
            if self.modifier:
                self.Split(False)
                self.valueLightning = round((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2 * self.valueAttacksPerSecond, 1)
            else:
                self.valueLightning = 0
            self.searchPattern(self.patternStringCold, data)
            if self.modifier:
                self.Split(False)
                self.valueCold = round((int(filter(str.isdigit, str(self.values[0]))) + int(filter(str.isdigit, str(self.values[1])))) / 2 * self.valueAttacksPerSecond, 1)
            else:
                self.valueCold = 0
            self.valueElemental = sum([self.valueFire, self.valueLightning, self.valueCold])
            self.totalDPS = round(sum([self.valuePhysical, self.valueElemental, self.valueChaos]), 1)
            if self.totalDPS > 0:
                return True
            else:
                return False
        except:
            return False



