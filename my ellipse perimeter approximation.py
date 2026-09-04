import math
from matplotlib import pyplot
def calculate_user_ellipse():
    print("ellipser perimeter calculation V2.0")
    try:
        a = float(input("Enter semi-major axis (a): "))
        b = float(input("enter semi-minor axis (b): "))
    except ValueError:
        print("pls enter valid numbers.")
        return
    a, b = abs(a), abs(b)

    if a == 0 and b == 0:
        print("\ncalculated estimation: 0.0\nofficial infinite series sum: 0.0")
        return

    # my formula est. thats IS PROBABLY better than most
    h = ((a - b) / (a + b)) ** 2
    my_estimation = math.pi * (a + b) * ((32 - 15.30997409*h - 4.07183635*h**2) / (32 - 23.3029129*h + 1.21333601*h**2))

    # simulated infinite series
    series_sum = 1.0
    term = 1.0
    for n in range(1, 1000):
        # most liekly accurate enough
        term *= h * ((2 * n - 3) / (2 * n)) ** 2 if n > 1 else (h / 4)
        series_sum += term

        
    real_official = math.pi * (a + b) * series_sum
    diff = abs(my_estimation - real_official)

    print(f"\ncalculated estimation:  {my_estimation:.10f}\nofficial infinite series sum: {real_official:.10f}")
    print(f"absolute diff. :      {diff:.10f}\npercent error:            {(diff / real_official * 100 if real_official else 0):.5f}%")

if __name__ == "__main__":
    calculate_user_ellipse()
