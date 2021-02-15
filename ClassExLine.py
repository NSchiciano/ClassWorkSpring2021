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


# Output
def give_ans(Y, m, b):
    print("The line you gave is {:.2f}x + {:.2f}, and the y is {:.2f}".format(m, b, Y))


# Main and Calling Main
def main():
    tuple1,tuple2 = get_line()
    print(tuple1)
    print(tuple2)
    calcSlope = calc_slope(tuple1,tuple2)
    print(calcSlope)
    calcIntercept = calc_intercept(tuple1, calcSlope)
    print(calcIntercept)
    point = get_point()
    print(point)
    calcY = calc_point(calcSlope, calcIntercept, point)
    print(calcY)
    give_ans(calcY, calcSlope, calcIntercept)


if __name__ == "__main__":
    main()
