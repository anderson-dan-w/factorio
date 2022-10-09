from factorio.resource.resource_01 import *
from factorio.resource.spacexp.resource_02 import *

##################################################
# Arms
class CoalInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    IronStick: 2,
    SingleCylinder: 1,
  }

class YellowInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    BlueMotor: 1,
    CoalInserter: 1,
  }

class RedInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    YellowInserter: 1,
    IronStick: 2,
    IronPlate: 2,
  }

class BlueInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    GreenCircuit: 2,
    YellowInserter: 1,
    IronPlate: 2,
  }
