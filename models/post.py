from pydantic import BaseModel

class PowerPlant(BaseModel):
    name: str
    type: str
    efficiency: float
    pmin: float
    pmax: float
    cost_per_MWh: float | None = None

class Fuel(BaseModel):
    gas: float
    kerosine: float
    co2: float | None = None
    wind: float

class ProductionPlanRequest(BaseModel):
    load: float
    fuels: dict[str, float]
    powerplants: list[PowerPlant]

class ProductionPlanResponse(BaseModel):
    name: str
    p: float