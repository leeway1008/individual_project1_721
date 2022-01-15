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
    return {"Kg":kg}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0') 