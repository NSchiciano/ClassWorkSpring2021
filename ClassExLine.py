# user inputs
def get_line():
    points1 = input("Give First Set of Points x,y: ")
    tuple1 = tuple(map(int,points1.split(',')))
    points2 = input("Give Second Set of Points x,y: ")
    tuple2 = tuple(map(int,points2.split(',')))
    return(tuple1,tuple2)


def  get_point():
    line2 = 0


# Calculations
def calc_slope(tuple1, tuple2):
    slope = (tuple1[1]-tuple2[1]) / (tuple1[0]-tuple2[0])
    return(slope)


def calc_intercept(tuple, slope):
    intercept =  tuple[1]-tuple[0]*slope
    return intercept


def calc_point():
    line4 = 0


# Output
def give_ans():
    line5 = 0


# Main and Calling Main
def main():
    tuple1,tuple2 = get_line()
    print(tuple1)
    print(tuple2)
    calcSlope = calc_slope(tuple1,tuple2)
    print(calcSlope)
    calcIntercept = calc_intercept(tuple1, calcSlope)
    print(calcIntercept)
    get_point()
    calc_point()
    give_ans()


if __name__ == "__main__":
    main()
