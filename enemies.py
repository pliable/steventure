class enemy:
  def __init__(self):
    self.health = 100
    self.armor = 0
    self.has_shield = False
    self.weapons = set()
    pass

#define subclasses after here
class asshole(enemy):
  def __init__(self):
    self.instance = enemy.__init__()
    pass

class cunt(enemy):
  def __init__(self):
    self.instance = enemy.__init__()
    pass

class zombie_gary_coleman(enemy):
  def __init__(self):
    self.instance = enemy.__init__()
    pass
