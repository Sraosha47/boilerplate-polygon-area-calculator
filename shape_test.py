def shape_calc_test(rectangle, square):
    #creating objects--------------------------------------
    rect = rectangle(3, 6)
    sq = square(5)
    #endregion---------------------------------------------

    #defining functions------------------------------------
    def init_test(rectangle, square):
        print("rect and sq initialised\n")
        print("rect's height: " + str(rectangle.height))
        print("rect's width: " + str(rectangle.width))
        print((15 + len(str(rectangle.height)))* "-")
        print("sq's height: " + str(square.height))
        print("sq's width: " + str(square.width) + "\n")

    def area_test(rectangle, square):
        print("rect's area: " + str(rectangle.get_area()))
        print("sq's area: " + str(square.get_area()) + "\n")

    def perimeter_test(rectangle, square):
        print("rect's perimeter: " + str(rectangle.get_perimeter()))
        print("sq's perimeter: " + str(square.get_perimeter()) + "\n")

    def diagonal_test(rectangle, square):
        print("rect's diagonal: " + str(rectangle.get_diagonal()))
        print("sq's diagonal: " + str(square.get_diagonal()) + "\n")

    def picture_test(rectangle, square):
        print(rectangle.get_picture())
        print(square.get_picture())

    
    #endregion-------------------------------------------------

    #execution tests-------------------------------------------
    print(rect)
    print(sq)
    init_test(rect, sq)
    area_test(rect, sq)
    perimeter_test(rect, sq)
    diagonal_test(rect, sq)
    picture_test(rect, sq)
    #endregion-------------------------------------------------

