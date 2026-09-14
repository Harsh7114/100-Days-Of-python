import  os
from dotenv import  load_dotenv
load_dotenv()
from langchain_groq import  ChatGroq
from pydantic import  BaseModel , Field
from calories_api import get_calories
from match_activity import choose_best_activity
from datetime import datetime
from google_sheets import add_workout
class Workout(BaseModel):
    activity: str = Field(
        description="Name of the exercise or activity"
    )

    duration: int = Field(
        description="Duration of the activity in minutes"
    )

    intensity: str | None = Field(
        default=None,
        description="Intensity such as slow, light, moderate, vigorous, or fast if mentioned"
    )
USER_WEIGHT_KG = 70
USER_WEIGHT_LB = USER_WEIGHT_KG * 2.20462
llm = ChatGroq(model="openai/gpt-oss-20b")
structured_llm = llm.with_structured_output(Workout)

user_input = input("Enter your workout: ")
# prompt = f"""
# Extract the workout information from the user's message.
#
# User message:
# {user_input}
#
# Return only:
# - activity
# - duration in minutes
# """
# response = llm.invoke(prompt)

workout = structured_llm.invoke(user_input)

print("Activity:", workout.activity)
print("Duration:", workout.duration)
print("Intensity:", workout.intensity)
calorie_data = get_calories(
    activity=workout.activity,
    weight = USER_WEIGHT_LB,
    duration=workout.duration,
    intensity=workout.intensity
)
# print("Candidates:")
# print(calorie_data)

best_match = choose_best_activity(
    user_activity=workout.activity,
    intensity=workout.intensity,
    candidates=calorie_data
)

if best_match:
    print("Best match:", best_match["name"])
    print("Calories burned:", best_match["total_calories"])
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M")
    add_workout(
        date=date,
        time=time,
        exercise=workout.activity,
        duration=workout.duration,
        calories=best_match["total_calories"]
    )
else:
    print("Could not find a suitable exercise match.")