import requests
from datetime import datetime
import os

APP_ID = "92070170"
API_KEY = "fef624f642750b63aa4f8c477b44e2bc"
GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 23

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

headers ={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
params = {
    "query": input("What have you done ?"),
    "gender": "male",
}
response = requests.post(url=nutritionix_endpoint,json=params,headers=headers)
data = response.json()
print(data)

headerss = {
    "Authorization": "Basic eWV0dGlnYXJpaTpZZXR0aWdhcmlpMA=="
}

sheety_post_endpoint = "https://api.sheety.co/9ab4ed823b73c2464b495df720a60f18/workoutTracking/workouts"



for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
response_sheety = requests.post(url=sheety_post_endpoint,json=sheet_inputs,headers=headerss)
print(response_sheety.text)

