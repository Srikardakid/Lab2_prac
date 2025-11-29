import lab2

def test_min_max():
    input = [7,8,9]
    result = lab2.find_min_max(input)
    assert(result == [7,9])
def test_calc_avg():
    input = [1,2,3]
    result = lab2.calc_average(input)
    assert(result == 2)
def test_median():
    input = [4,5,6]
    result = lab2.calc_median_temp(input)
    assert(result == 5)