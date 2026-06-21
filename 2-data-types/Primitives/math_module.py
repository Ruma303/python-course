
import math

## Costanti matematiche
print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586
print(math.inf)  # inf
print(math.nan)  # nan

## Funzioni aritmetiche di base
print(math.ceil(2.3))    # 3
print(math.floor(2.7))   # 2
print(math.trunc(-4.7))  # -4
print(math.fabs(-5))     # 5.0
print(math.copysign(-3, 16)) # 3

## Funzioni aritmetiche avanzate
print(math.pow(2, 3))    # 8.0
print(math.sqrt(16))     # 4.0
print(math.exp(2))       # 7.38905609893065
print(math.log(8, 2))    # 3.0
print(math.log10(100))   # 2.0

## Funzioni trigonometriche
angolo_rad = math.radians(30)
print(math.sin(angolo_rad))    # 0.5
print(math.cos(angolo_rad))    # 0.86
print(math.tan(angolo_rad))    # 0.57
print(math.degrees(math.acos(0.5))) # 59.99
print(math.radians(math.cos(0.5)))  # 0.015

## Funzioni speciali
print(math.factorial(5))   # 120
print(math.gcd(12, 15))    # 3
print(math.lcm(12, 15))    # 60
print(math.comb(5, 2))     # 10
print(math.perm(5, 2))     # 20