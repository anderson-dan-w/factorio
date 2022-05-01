from collections import defaultdict


class Resource:
  def __init__(self, name, seconds_per_batch, num_per_batch, recipe=None):
    self.name = name
    self.seconds_per_batch = seconds_per_batch
    self.num_per_batch = num_per_batch
    self.recipe = recipe
    self._num_per_second = self.num_per_batch / self.seconds_per_batch

  def __str__(self):
    return self.name

  def __repr__(self):
    return f"{self.name}({self.seconds_per_batch}s, #{self.num_per_batch})"

  def full_recipe(self, nps_desired=1):
    full = defaultdict(float, {self: nps_desired})
    batches_per_sec = nps_desired / self.num_per_batch
    if self.recipe:
      for resource, count in self.recipe.items():
        sub_full = resource.full_recipe()
        for sub_resource, sub_count in sub_full.items():
          # TODO(dan): ...why doesn't sub_count get used???
          full[sub_resource] += (count * batches_per_sec)
    return full


# TODO(dan): resource-types: Minable, Furnace, Assembler - so "preferred maker" speed can work
COAL = Resource("Coal", 2, 1)
IRON_ORE = Resource("Iron Ore", 2, 1)
COPPER_ORE = Resource("Copper Ore", 2, 1)
STONE = Resource("Stone", 2, 1)

IRON_PLATE = Resource("Iron Plate", 3.2, 1, {IRON_ORE: 1})
COPPER_PLATE = Resource("Copper Plate", 3.2, 1, {COPPER_ORE: 1})

COPPER_CABLE = Resource("Copper Cable", 0.5, 2, {COPPER_PLATE: 1})
STEEL = Resource("Steel", 16, 1, {IRON_PLATE: 5})
