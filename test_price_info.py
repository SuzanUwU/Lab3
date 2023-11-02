import price_info

print("Test_Price_Info")

price_list = price_info.price_list
quantity_list = price_info.quantity_list


def test_total_cost_shopping():
    expected_result = 46.75
    total_cost = 0
    total_cost = price_info.total_cost_shopping()
    assert (total_cost == expected_result)


def test_cost_of_fruit():
    expected_result = 9.0
    input_fruit = "pear"  # 0.90 per pear
    cost = price_info.cost_of_fruits(input_fruit, 10)  # 10 pears
    assert (cost == expected_result)
