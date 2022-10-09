from factorio.resource_01 import resource as R

class OilRefineryRecipe:
  pass

class PetroleumRecipe(OilRefineryRecipe):
  PETROLEUM = 90
  HEAVY_OIL = 0
  LIGHT_OIL = 0

class LightOilRecipe(OilRefineryRecipe):
  PETROLEUM = 30
  HEAVY_OIL = 20
  LIGHT_OIL = 70

class HeavyOilRecipe(OilRefineryRecipe):
  PETROLEUM = 20
  HEAVY_OIL = 70
  LIGHT_OIL = 30

DEFAULT_OIL_RECIPE = LightOilRecipe

class Petroleum(R.OilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.PETROLEUM
  recipe = {
    R.Water: 50,
    R.CrudeOil: 100,
  }

class LightOil(R.OilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.LIGHT_OIL
  recipe = {
    R.Water: 50,
    R.CrudeOil: 100,
  }

class HeavyOil(R.OilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.HEAVY_OIL
  recipe = {
    R.Water: 50,
    R.CrudeOil: 100,
  }

# TODO(dan): what about heavy->light and light->petroleum chem plants?

class Lube(R.ChemicalResource):
  seconds_per_batch = 1
  num_per_batch = 10
  recipe = {
    HeavyOil: 10,
  }
