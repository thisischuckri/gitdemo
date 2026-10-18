from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

print("*****Installation is successful. You can now use the ChatGoogleGenerativeAI class in your code.")

def add_numbers(a, b):
    return a + b

def diverse_numbers(a, b):
    return a / b

@tool
def get_weather(city: str) -> str:
    """
    Get the current weather for a given city.
    """
    # For demonstration purposes, we'll return a mock weather response.
    return f"The current weather in {city} is sunny with a temperature of 25°C."

output = get_weather.invoke("New York")
print(output)  # Output: The current weather in New York is sunny with a temperature of 25°C.   


