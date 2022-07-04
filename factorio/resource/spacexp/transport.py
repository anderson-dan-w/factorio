from factorio.resource.resource import *
from factorio.resource.spacexp.resource import *

##################################################
# Transport
class YellowBelt(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 2
  recipe = {
    SingleCylinder: 1,
    IronPlate: 1,
  }

class YellowUnderground(AssemblerResource):
  seconds_per_batch = 1
  num_per_batch = 2
  recipe = {
    IronPlate: 10,
    YellowBelt: 5,
  }

class YellowSplitter(AssemblerResource):
  seconds_per_batch = 1
  num_per_batch = 1
  recipe = {
    IronPlate: 8,
    YellowBelt: 4,
    SingleCylinder: 4,
  }

class RedBelt(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    Gear: 5,
    YellowBelt: 1,
  }

class RedUnderground(AssemblerResource):
  seconds_per_batch = 2
  num_per_batch = 1
  recipe = {
    Gear: 40,
    YellowUnderground: 2,
  }

class RedSplitter(AssemblerResource):
  seconds_per_batch = 2
  num_per_batch = 1
  recipe = {
      Gear: 10,
      GreenCircuit: 10,
      YellowSplitter: 1,
  }
