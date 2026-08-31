import math
from matplotlib import pyplot
def calculate_user_ellipse():
    print("ellipser-thing calculation")
    try:
        a = float(input("yo! enter semi-major axis (a): "))
        b = float(input("and enter semi-minor axis (b): "))
    except ValueError:
        print("pls enter valid numbers.")
        return

    # convert to absolute values to handle negative inputs safely
    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("\ncalculated estimation: 0.0\nofficial infinite series sum: 0.0")
        return

    # my formula est. thats shiitake mushrooms (allegedly and supposedly worse or better lets see)
    h = ((a - b) / (a + b)) ** 2
    my_estimation = math.pi * (a + b) * ((32 + 9.5*h + 1.1*h**2) / (32 + 1.54*h - 0.05*h**2))

    # actual infinite series, or rather its very good approximation
    series_sum = 1.0
    term = 1.0
    for n in range(1, 1000):
        # *hopfully* accruate enough
        term *= h * ((2 * n - 3) / (2 * n)) ** 2 if n > 1 else (h / 4)
        series_sum += term

        
    real_official = math.pi * (a + b) * series_sum
    diff = abs(my_estimation - real_official)

    print(f"\ncalculated estimation:  {my_estimation:.10f}\nofficial infinite series sum: {real_official:.10f}")
    print(f"absolute diff. :      {diff:.10f}\npercent error:            {(diff / real_official * 100 if real_official else 0):.5f}%")

if __name__ == "__main__":
    calculate_user_ellipse()
