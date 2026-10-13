from src.kopo_calc import add, subtract

def test_feature_1():
  assert add(10, 5) == 15
  assert subtract(10, 5) == 5
