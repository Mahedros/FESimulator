import random

class Character():
	def __init__(self, name, stats, unitClass):
		"""
			Character data
			@param name --> Character's name; should specify game if recurring character
			@param stats --> dict containing character stats (str, skl, spd, usable weapons, etc)
			@param unitClass --> Class of character (Lord, Paladin, General, etc)
		"""
		self.name = name
		self.stats = stats
		self.tmpStats = stats
		self.unitClass = unitClass
		self.currentHP = stats["HP"]

class Weapon():
	def __init__(self, name, stats, weaponType, effects):
		"""
			Data for a weapon
			@param name --> Name of weapon; should specify game if multiple versions exist
			@param stats --> dict containing weapon props (might, weight, hit, crit, range)
			@param weaponType --> Indicates class of weapon (sword, lance, axe, etc)
			@param effects --> Special weapon properties (armorslayer, brave, luna, bonuses, etc)
		"""
		self.name = name
		self.stats = stats
		self.weaponType = weaponType
		self.effects = effects

class Skill():
	"""
		Base class for all skills
		Skills should extend and override checkActivate() and activate()
	"""
	def __init__(self, name):
		self.name = name

	def checkActivate(character):
		return False

	def activate(fight, activator, opponent):
		pass


class Fight():
	def __init___(self, char1, char2, weap1, weap2):
		self.char1 = char1
		self.char2 = char2
		self.weap1 = weap1
		self.weap2 = weap2

class Round():
	def __init__(self, char1, char2, weap1, weap2):
		self.char1 = char1
		self.char2 = char2
		self.weap1 = weap1
		self.weap2 = weap2
		char1.currentHP = char1.stats["HP"]
		char2.currentHP = char2.stats["HP"]

	def process(self):
		winner = None
		while(winner == None):
			winner = Fight(char1, char2, weap1, weap2).run()
			if(winner != None):
				winner = Fight(char2, char1, weap2, weap1).run()
		return winner

