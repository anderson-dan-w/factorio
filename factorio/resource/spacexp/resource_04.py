from factorio.resource.resource_01 import *
from factorio.resource.spacexp.resource_02 import *
from factorio.resource.spacexp.fluid_based_03 import *

class LDS(AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 1
  recipe = {
    Plastic: 10,
    CopperPlate: 10,
    Steel: 10,
    Glass: 10,
  }
