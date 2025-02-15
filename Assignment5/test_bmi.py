import pytest
from bmi_program import calculate_bmi_value, get_bmi_category

def test_normal_bmi():
    weight = 150
    height = 68
    bmi = calculate_bmi_value(weight, height)
    assert round(bmi, 1) == 22.8
    assert get_bmi_category(bmi) == "Normal Weight"

def test_obesity_bmi():
    weight = 220
    height = 65
    bmi = calculate_bmi_value(weight, height)
    assert round(bmi, 1) == 36.6
    assert get_bmi_category(bmi) == "Obesity"

def test_min_valid_weight():
    weight = 10
    height = 60
    bmi = calculate_bmi_value(weight, height)
    assert round(bmi, 1) == 2.0
    assert get_bmi_category(bmi) == "Underweight"

def test_invalid_weight():
    weight = -5
    height = 67
    with pytest.raises(ValueError):
        calculate_bmi_value(weight, height)

def test_invalid_height():
    weight = 140
    height = 180
    with pytest.raises(ValueError):
        calculate_bmi_value(weight, height)

if __name__ == "__main__":
    pytest.main()
