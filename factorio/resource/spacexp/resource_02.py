from factorio.resource import resource_01 as R

class Sand(R.AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 2
  recipe = {R.Stone: 1}

class Glass(R.AssemblerResource):
  seconds_per_batch = 4
  num_per_batch = 1
  recipe = {Sand: 4}

class StoneTablet(R.AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 4
  recipe = {R.StoneBrick: 1}

class StoneFurnace(R.AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {R.Stone: 5}

class SingleCylinder(R.AssemblerResource):
  seconds_per_batch = 0.6
  num_per_batch = 1
  recipe = {
    R.Gear: 1,
    R.IronPlate: 1,
  }

class MultiCylinder(R.AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 1
  recipe = {
    SingleCylinder: 2,
    R.Gear: 2,
    R.Steel: 2,
  }

class GreenCircuit(R.AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    StoneTablet: 1,
    R.CopperCable: 3,
  }

class BlueMotor(R.AssemblerResource):
  seconds_per_batch = 0.8
  num_per_batch = 1
  recipe = {
    R.CopperCable: 6,
    R.Gear: 1,
    R.IronPlate: 1,
  }

class Concrete(R.AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 10
  recipe = {
    R.IronStick: 2,
    Sand: 10,
    R.StoneBrick: 5,
    R.Water: 100,
  }
