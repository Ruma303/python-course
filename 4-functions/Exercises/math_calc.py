a = 10
b = 5

arithmetic_calc = [
  lambda a: a + 1,
  lambda a: a - 1,
  lambda a: a * 2,
  lambda a: a / 2,
  lambda a: a ** 2,
  lambda a: a % 2 == 0,
]

print("\nArithmetic operations")
for calc in arithmetic_calc:
  print(calc(a))


logic_calc = (
  lambda a, b: a and 1,
  lambda a, b: a or 1,
  lambda a, b: not a,
)

print("\nLogic operations")
for calc in logic_calc:
  print(calc(a, b=None))


comparison_calc = {
  "equal" : lambda a, b: a == b,
  "different" : lambda a, b: a != b,
  "less_or_equal" : lambda a, b: a <= b,
  "greater_or_equal" : lambda a, b: a >= b,
}

print("\nComparison operations")
for op, calc in comparison_calc.items():
  print(f"{op}: {calc(a, b)}")
