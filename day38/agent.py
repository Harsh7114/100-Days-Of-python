import  os
from dotenv import  load_dotenv
load_dotenv()
from langchain_groq import  ChatGroq
from pydantic import  BaseModel , Field
from calories_api import get_calories
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

print("Calorie result:")
print(calorie_data)