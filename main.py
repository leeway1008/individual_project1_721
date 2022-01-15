from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is IDS721 22Spring Individual Project 1. Bohan Li"}

@app.get("/lbtokg/{num1}")
async def transferLbtoKg(num1: int):
    kg = format(0.46 * num1, ".2f")
    # kg = num1*2
    return {"kg":kg}

@app.get("/oztog/{num1}")
async def transferOztoG(num1: int):
    g = format(28.35 * num1, ".2f")
    # kg = num1*2
    return {"g":g}
    
@app.get("/gallontol/{num1}")
async def transferGallontoL(num1: int):
    l = format(3.79 * num1, ".2f")
    # kg = num1*2
    return {"l":l}
    
@app.get("/miletokm/{num1}")
async def transferMiletoKm(num1: int):
    km = format(1.6 * num1, ".2f")
    # kg = num1*2
    return {"km":km}
    
@app.get("/yardtom/{num1}")
async def transferYardtoM(num1: int):
    m = format(0.91 * num1, ".2f")
    # kg = num1*2
    return {"m":m}

@app.get("/feettocm/{num1}")
async def transferFeettoCm(num1: int):
    cm = format(30.48 * num1, ".2f")
    # kg = num1*2
    return {"cm":cm}
    
@app.get("/inchtocm/{num1}")
async def transferInchtoCm(num1: int):
    cm = format(2.54 * num1, ".2f")
    # kg = num1*2
    return {"cm":cm}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0') 