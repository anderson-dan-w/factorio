from factorio.resource.resource import *

class StoneTablet(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 4
  recipe = {StoneBrick: 1}

class StoneFurnace(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {Stone: 5}

class SingleCylinder(AssemblerResource):
  seconds_per_batch = 0.6
  num_per_batch = 1
  recipe = {
    Gear: 1,
    IronPlate: 1,
  }
