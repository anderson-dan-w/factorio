from factorio.resource.resource import *

class Sand(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 2
  recipe = {Stone: 1}

class Glass(AssemblerResource):
  seconds_per_batch = 4
  num_per_batch = 1
  recipe = {Sand: 4}

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

class MultiCylinder(AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 1
  recipe = {
    SingleCylinder: 2,
    Gear: 2,
    Steel: 2,
  }

class GreenCircuit(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    StoneTablet: 1,
    CopperCable: 3,
  }

class BlueMotor(AssemblerResource):
  seconds_per_batch = 0.8
  num_per_batch = 1
  recipe = {
    CopperCable: 6,
    Gear: 1,
    IronPlate: 1,
  }
