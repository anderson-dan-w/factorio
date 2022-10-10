# TODO(dan): imports...

class BlueSplitter(AssemblerResource):
  seconds_per_batch = 2
  num_per_batch = 1
  recipe = {
      Gear: 10,
      RedCircuit: 10,
      RedSplitter: 1,
      Lube: 80,
  }
