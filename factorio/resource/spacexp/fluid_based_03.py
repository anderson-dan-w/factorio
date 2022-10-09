from factorio.resource import resource_01 as R
from factorio.resource.spacexp import fluids_02 as F
from factorio.resource.spacexp import resource_02 as SR

class Plastic(R.ChemicalResource):
  seconds_per_batch = 1 
  num_per_batch = 2
  recipe = {
    R.Coal: 1,
    F.Petroleum: 20,
  }

class Sulfur(R.ChemicalResource):
  seconds_per_batch = 1
  num_per_batch = 2
  recipe = {
    R.Water: 30,
    F.Petroleum: 30,
  }

class RedCircuit(R.AssemblerResource):
  seconds_per_batch = 6
  num_per_batch = 1
  recipe = {
    R.CopperCable: 4,
    SR.GreenCircuit: 2,
    Plastic: 2,
  }

class GreenMotor(R.AssemblerResource):
  seconds_per_batch = 10
  num_per_batch = 1
  recipe = {
    SR.GreenCircuit: 4,
    F.Lube: 40,
    R.Steel: 2,
    SR.BlueMotor: 2,
  }
