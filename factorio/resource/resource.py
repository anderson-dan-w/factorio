class Resource:
  def __init__(self, seconds_per_batch, num_per_batch, recipe=None):
    self.seconds_per_batch = seconds_per_batch
    self.num_per_batch = num_per_batch
    self.recipe = recipe

class IronPlate(Resource):
  pass
