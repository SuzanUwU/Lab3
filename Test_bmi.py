import Lab2.bmi as bmi

BMI = 19.04


def test_bmi_normal_weight():
    if BMI < 18.5:
        result = "Under weight"


def test_bmi_under_weight():
    if 18.5 <= BMI <= 25.0:
        result = "Normal weight"


def test_bmi_over_weight():
    if BMI > 25.0:
        result = "Over weight"
