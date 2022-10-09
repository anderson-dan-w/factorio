from factorio.resource.spacexp.resource_02 import *
from factorio.resource.spacexp.inserters_03 import *
from factorio.resource.spacexp.transport_03 import *

class RedScience(AssemblerResource):
  seconds_per_batch = 5
  num_per_batch = 1
  recipe = {
    Gear: 1,
    CopperPlate: 1,
  }

class GreenScience(AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 2
  recipe = {
    YellowBelt: 2,
    YellowInserter: 1,
  }

class GreyScience(AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 2
  recipe = {
    # ... make intermediates...
  }
