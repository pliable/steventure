class Player:
  def __init__(self):
    self.health = 100
    self.armor = 0
    self.has_shield = False
    self.weapons = set()

  def damage(self, type):
    pass

  def heal(self, type):
    pass

  def get_shield(self, type):
    pass

  def get_weapon(self, type):
    pass
