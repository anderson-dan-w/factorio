# TODO(dan): imports...

class GreenInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    Gear: 15,
    GreenCircuit: 15,
    RedCircuit: 1,
    BlueInserter: 1,
  }

class WhiteInserter(AssemblerResource):
  seconds_per_batch = 0.5
  num_per_batch = 1
  recipe = {
    GreenCircuit: 5,
    GreenInserter: 1,
  }
