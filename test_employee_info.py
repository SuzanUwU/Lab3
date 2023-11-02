import employee_info

employee_data = employee_info.employee_data


def test_cal_avg_salary():
    expected_average_salary = 361000 / 6
    result = employee_info.calculate_average_salary()
    assert (expected_average_salary == result)


def test_get_employees_by_dept():
    expected_result = ["John", "Peter"]  # for Sales
    input_department = "Sales"
    result = employee_info.get_employees_by_dept(input_department)
    assert (expected_result == result)


def test_get_employees_by_age_range():
    expected_result = ["Jane", "Mary"]  # for min 20 max 30
    min_age = 20
    max_age = 30
    result = employee_info.get_employees_by_age_range(min_age, max_age)
    assert (expected_result == result)
