from app import power

def test_power():
  assert power(4, 3) == 64, "err, 4 ** 3 = 64"
  assert power(3, 4) == 81, "err, 3 ** 4 = 81"
  print("sucess")
if __name__ == "__main__":
  test_power()
