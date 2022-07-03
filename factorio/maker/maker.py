class MakerNames:
  DRILLS = "drills"
  FURNACES = "furnaces"
  ASSEMBLERS = "assemblers"

##################################################
class AbstractMaker:
  @property
  def name(self):
    raise NotImplementedError("Maker needs a name!")

  @property
  def DEFAULT_SPEED(self):
    raise NotImplementedError(f"{self.name} needs a speed!")

##################################################
class AbstractDrill(AbstractMaker):
  name = MakerNames.DRILLS

class CoalDrill(AbstractDrill):
  DEFAULT_SPEED = 0.5

class ElectricDrill(AbstractDrill):
  DEFAULT_SPEED = 1

##################################################
class AbstractFurnace(AbstractMaker):
  name = MakerNames.FURNACES

class StoneFurnace(AbstractFurnace):
  DEFAULT_SPEED = 1

class SteelFurnace(AbstractFurnace):
  DEFAULT_SPEED = 2 # TODO(dan): confirm this...

class ElectricFurnace(AbstractFurnace):
  DEFAULT_SPEED = 2

##################################################
class AbstractAssembler(AbstractMaker):
  name = MakerNames.ASSEMBLERS

class Assembler1(AbstractAssembler):
  DEFAULT_SPEED = 0.5

class Assembler2(AbstractAssembler):
  DEFAULT_SPEED = 0.75

class Assembler3(AbstractAssembler):
  DEFAULT_SPEED = 1
