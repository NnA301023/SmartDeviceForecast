import uvicorn
from random import randint
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Define CORS settings
origins = ["*"]  # Change this to a list of allowed origins if needed.

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = origins,
    allow_headers = origins,
)

# Define a Pydantic model for input data (modify as per your data structure)
class IoTDataInput(BaseModel):
    current_value: float

# Define the forecasting route
@app.get("/forecast")
async def forecast_iot_data():
    try:
        # Perform the t+1 forecasting based on your model or logic
        # Replace this with your actual forecasting code
        t_plus_1 = randint(1, 100)
        
        return {"status_code" : 200, "message" : "success", "body" : {"forecast": t_plus_1}}
    except Exception as e:
        raise HTTPException(status_code = 500, detail = "Error in forecasting")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)