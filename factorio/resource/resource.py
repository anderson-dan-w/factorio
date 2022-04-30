class Resource:
  def __init__(self, name, seconds_per_batch, num_per_batch, recipe=None):
    self.seconds_per_batch = seconds_per_batch
    self.num_per_batch = num_per_batch
    self.recipe = recipe
    self.name = name

  def __str__(self):
    return self.name

  def __repr__(self):
    return f"Resource({self.name}, {self.seconds_per_batch}s, #{self.num_per_batch})"

  def full_recipe(self, n=1):
    full = {self: n}
    if self.recipe:
      for resource, count in self.recipe.items():
        sub_full = resource.full_recipe(n)
        for sub_resource, sub_count in sub_full.items():
          if sub_resource in full:
            full[sub_resource] += (sub_count * n)
          else:
            full[sub_resource] = (sub_count * n)
    return full


IRON_ORE = Resource("Iron Ore", 2, 1)
IRON_PLATE = Resource("Iron Plate", 3.2, 1, {IRON_ORE: 1})
