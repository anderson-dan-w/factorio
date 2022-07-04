class MakerNames:
  DRILLS = "drills"
  FURNACES = "furnaces"
  ASSEMBLERS = "assemblers"
  OIL_REFINERY = "oil-refineries"
  CHEMICAL_PLANT = "chem-plants"
  PUMP_JACK = "pump-jack"
  WATER_PUMP = "water-pump"

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

##################################################
class OilRefinery(AbstractMaker):
  name = MakerNames.OIL_REFINERY
  DEFAULT_SPEED = 1  # TODO(dan): confirm

class ChemicalPlant(AbstractMaker):
  name = MakerNames.CHEMICAL_PLANT
  DEFAULT_SPEED = 1  # TODO(dan): confirm

class PumpJack(AbstractMaker):
  name = MakerNames.PUMP_JACK
  DEFAULT_SPEED = 1

class WaterPump(AbstractMaker):
  name = MakerNames.WATER_PUMP
  DEFAULT_SPEED = 1
