from models.post import ProductionPlanRequest, ProductionPlanResponse
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello ENGIE, this is Brian Daza"}

@app.post("/productionplan/", status_code=201)
async def create_plan(plan: ProductionPlanRequest) -> list[ProductionPlanResponse]:
    load = plan.load
    fuels = plan.fuels
    powerplants = plan.powerplants

    # Calculate the cost per MWh for each power plant
    for plant in powerplants:
        if plant.type == 'gasfired':
            plant.cost_per_MWh = fuels['gas(euro/MWh)'] / plant.efficiency
        elif plant.type == 'turbojet':
            plant.cost_per_MWh = fuels['kerosine(euro/MWh)'] / plant.efficiency
        elif plant.type == 'windturbine':
            plant.cost_per_MWh = 0  
            plant.pmax *= fuels['wind(%)'] / 100  
    
    # Sort power plants by cost/MWh, with lowest cost first
    powerplants.sort(key=lambda x: x.cost_per_MWh)

    # Allocate power to meet the load
    response = []
    remaining_load = load

    for plant in powerplants:

        # if you have already met the load just append the remaining plants to list with p:0.0
        if remaining_load <= 0:
            response.append({"name": plant.name, "p": 0.0})
            continue

        # determine the power contribution of the current plant
        pmin = plant.pmin
        pmax = plant.pmax

        # if remaining load is higher than pmin, take the pmax of the plant and substract it from the load
        if remaining_load >= pmin:
            p = min(remaining_load, pmax) # only use the amount of power required
            remaining_load -= p
            response.append({"name": plant.name, "p": p}) # add the plant to the response
        else:
            # If load < pmin, set to 0
            response.append({"name": plant.name, "p": 0.0})

    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)