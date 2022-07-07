from factorio.resource.resource import *

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

class Petroleum(AbstractOilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.PETROLEUM
  recipe = {
    Water: 50,
    CrudeOil: 100,
  }

class LightOil(AbstractOilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.LIGHT_OIL
  recipe = {
    Water: 50,
    CrudeOil: 100,
  }

class HeavyOil(AbstractOilResource):
  RECIPE = DEFAULT_OIL_RECIPE
  seconds_per_batch = 5
  num_per_batch = RECIPE.HEAVY_OIL
  recipe = {
    Water: 50,
    CrudeOil: 100,
  }

  # TODO(dan): what about heavy->light and light->petroleum chem plants?
