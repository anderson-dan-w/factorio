from factorio.resource.spacexp.fluids import *
from factorio.resource.resource import *

class Plastic(AbstractChemicalResource):
  seconds_per_batch = 1 
  num_per_batch = 2
  recipe = {
    Coal: 1,
    Petroleum: 20,
  }

class Sulfur(AbstractChemicalResource):
  seconds_per_batch = 1
  num_per_batch = 2
  recipe = {
    Water: 30,
    Petroleum: 30,
  }
