# user inputs
def get_line():
    points1 = input("Give First Set of Points x,y: ")
    tuple1 = tuple(map(int,points1.split(',')))
    points2 = input("Give Second Set of Points x,y: ")
    tuple2 = tuple(map(int,points2.split(',')))
    return(tuple1,tuple2)


def  get_point():
    point3 = float(input("Give x desired on the line: "))
    return point3


def get_points():
    points4 = input("Test if Points are on your line x,y: ")
    tuple1 = tuple(map(int,points4.split(',')))
    return(tuple1)


# Calculations
def calc_slope(tuple1, tuple2):
    slope = (tuple1[1]-tuple2[1]) / (tuple1[0]-tuple2[0])
    return(slope)


def calc_intercept(tuple, slope):
    intercept =  tuple[1]-tuple[0]*slope
    return intercept


def calc_point(slope, intercept, point):
    y = slope*point + intercept
    return y


def check_points(m, b, points):
    y = m*points[0] + b
    if y == points[1]:
        return True
    else:
        return False


# Output
def give_ans(Y, m, b):
    print("The line you gave is {:.2f}x + {:.2f}, and the y is {:.2f}".format(m, b, Y))


def give_TofF(TorF):
    print("Those points are on the line if true below")
    print(TorF)


# Main and Calling Main
def main():
    tuple1,tuple2 = get_line()
    calcSlope = calc_slope(tuple1,tuple2)
    calcIntercept = calc_intercept(tuple1, calcSlope)
    point = get_point()
    calcY = calc_point(calcSlope, calcIntercept, point)
    give_ans(calcY, calcSlope, calcIntercept)
    possible_points = get_points()
    TorF = check_points(calcSlope, calcIntercept, possible_points)
    give_TofF(TorF)


if __name__ == "__main__":
    main()
