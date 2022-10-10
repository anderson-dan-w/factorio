from factorio.resource.resource_01 import *
from factorio.resource.spacexp.fluids_02 import *
from factorio.resource.spacexp.resource_02 import *

class Plastic(ChemicalResource):
  seconds_per_batch = 1 
  num_per_batch = 2
  recipe = {
    Coal: 1,
    Petroleum: 20,
  }

class Sulfur(ChemicalResource):
  seconds_per_batch = 1
  num_per_batch = 2
  recipe = {
    Water: 30,
    Petroleum: 30,
  }

class RedCircuit(AssemblerResource):
  seconds_per_batch = 6
  num_per_batch = 1
  recipe = {
    CopperCable: 4,
    GreenCircuit: 2,
    Plastic: 2,
  }

class GreenMotor(AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 1
  recipe = {
    GreenCircuit: 4,
    Lube: 40,
    Steel: 2,
    BlueMotor: 2,
  }
