from collections import defaultdict

from factorio.maker import maker as M

class AbstractResource:
  recipe = None

  @classmethod
  def name(cls):
    return cls.__name__

  @classmethod
  def _num_per_second(cls):
    return cls.num_per_batch / cls.seconds_per_batch

  @property
  def MAKER(self):
    raise NotImplementedError(f"{self.name()} needs a maker!")

  def __str__(self):
    return self.name()

  def __repr__(self):
    return f"{self.name()}({self.seconds_per_batch}s, #{self.num_per_batch})"

  @classmethod
  def _makers_needed(cls, nps_desired):
    return nps_desired / (cls._num_per_second() * cls.MAKER.DEFAULT_SPEED)

  @classmethod
  def _num_sub_items_needed(cls, item, nps_desired):
    return cls.recipe[item] * nps_desired / cls.num_per_batch

  @classmethod
  def itemized_recipe(cls, nps_desired=1, indent=""):
    makers_needed = cls._makers_needed(nps_desired)
    print(f"{indent}{cls.name()} : {makers_needed:.03} {cls.MAKER.name}")
    if not cls.recipe:
      return
    for item in cls.recipe:
      num_sub_items = cls._num_sub_items_needed(item, nps_desired)
      item.itemized_recipe(num_sub_items, indent=indent+"    ")

  @classmethod
  def _combined_recipe(cls, nps_desired=1):
    makers_needed = cls._makers_needed(nps_desired)
    basics = defaultdict(int)
    if not cls.recipe or issubclass(cls.MAKER, M.AbstractFurnace):
      basics[cls] = makers_needed
    if cls.recipe:
      for item in cls.recipe:
        num_sub_items = cls._num_sub_items_needed(item, nps_desired)
        sub_basics = item._combined_recipe(num_sub_items)
        for sub_item, sub_count in sub_basics.items():
          basics[sub_item] += sub_count
    return basics

  @classmethod
  def combined_recipe(cls, nps_desired=1):
    basics = cls._combined_recipe(nps_desired)
    for basic_item, basic_count in sorted(basics.items(), key=lambda kv: kv[0].name()):
      print(f"{basic_item.name()} : {basic_count} {basic_item.MAKER.name}")

##################################################
class MiningResource(AbstractResource):
  MAKER = M.ElectricDrill

class Coal(MiningResource):
  seconds_per_batch = 2
  num_per_batch = 1

class IronOre(MiningResource):
  seconds_per_batch = 2
  num_per_batch = 1

class CopperOre(MiningResource):
  seconds_per_batch = 2
  num_per_batch = 1

class Stone(MiningResource):
  seconds_per_batch = 2
  num_per_batch = 1

##################################################
class FurnaceResource(AbstractResource):
  MAKER = M.StoneFurnace

class IronPlate(FurnaceResource):
  seconds_per_batch = 3.2
  num_per_batch = 1
  recipe = {IronOre: 1}

class CopperPlate(FurnaceResource):
  seconds_per_batch = 3.2
  num_per_batch = 1
  recipe = {CopperOre: 1}

class StoneBrick(FurnaceResource):
  seconds_per_batch = 3.2
  num_per_batch = 1
  recipe = {Stone: 2}

class Steel(FurnaceResource):
  seconds_per_batch = 16
  num_per_batch = 1
  recipe = {IronPlate: 5}

##################################################
class AssemblerResource(AbstractResource):
  MAKER = M.Assembler2

class Pipe(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {IronPlate: 1}

class Gear(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {IronPlate: 2}

class IronStick(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 2
  recipe = {IronPlate: 1}

class CopperCable(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 2
  recipe = {CopperPlate: 1}
