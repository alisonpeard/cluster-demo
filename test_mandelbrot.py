import mandelbrot

def test_generate_data():
    actual_value = mandelbrot.generate_data([0], [0])
    expected_value = [[0]]
    assert actual_value == expected_value

def test_shape():
    actual = mandelbrot.generate_data(range(5), range(3))
    actual_rows = len(actual)
    actual_columns = len(actual[0])
    assert actual_rows == 3
    assert actual_columns == 5

def test_hypot():
    c = mandelbrot.hypot(3, 4)
    assert c == 5
    c = mandelbrot.hypot(5, 12)
    assert c == 13

# ----Notes----
# $ python -m pytest
