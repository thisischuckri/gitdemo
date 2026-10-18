from app import add_numbers, diverse_numbers, get_weather
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_diverse_numbers():
    assert diverse_numbers(10, 2) == 5
    assert diverse_numbers(-10, 2) == -5
    assert diverse_numbers(0, 1) == 0

def test_get_weather():
    output = get_weather.invoke("New York")
    assert output == "The current weather in New York is sunny with a temperature of 25°C."