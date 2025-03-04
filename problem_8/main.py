from fastapi import FastAPI, HTTPException
import sqlite3
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('weather.db')
    conn.row_factory = sqlite3.Row
    return conn

# Weather data model
class WeatherData(BaseModel):
    id: int
    city: str
    temperature: float
    humidity: int
    wind_speed: float
    date_recorded: str

# დავამატოთ საწყისი ენდპოინტი
@app.get("/")
async def root():
    return {"message": "Welcome to Weather API"}

@app.get("/weather", response_model=list[WeatherData])
async def get_weather_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM weather_data")
        rows = cursor.fetchall()

        # Convert rows to list of dictionaries
        weather_data = [dict(row) for row in rows]
        return weather_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@app.get("/weather/{city}", response_model=WeatherData)
async def get_city_weather(city: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM weather_data WHERE city = ?", (city,))
        row = cursor.fetchone()

        if row is None:
            raise HTTPException(status_code=404, detail="City not found")

        return dict(row)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)