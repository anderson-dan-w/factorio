from factorio.resource.resource import *

class GreenCircuit(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    IronPlate: 1,
    CopperCable: 3,
  }

class YellowInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    GreenCircuit: 1,
    Gear: 1,
    IronPlate: 1,
  }
