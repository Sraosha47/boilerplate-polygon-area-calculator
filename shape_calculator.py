from shape_test import shape_calc_test

#class Rectange-----------------------------------------------------------
class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return("Rectangle(width="+ str(self.width) + ", height="+ str(self.height) +")")

    #region methods------------------------------------------------------
    def get_area(self):
        self.area = self.width * self.height
        return(self.area)

    def get_perimeter(self):
        self.perimeter = 2 * self.width + 2 * self.height
        return(self.perimeter)

    def get_diagonal(self):
        self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return(self.diagonal)

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            self.picture = ''
            i = 0
            while i < (self.height):
                self.picture += self.width * "*" + "\n"
                i += 1
            return(self.picture)
        else:
            return("Too big for picture.")

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_amount_inside(self, shape):
        x = self.width / shape.width
        y = self.height / shape.height
        return(int(x*y))

    #endregion----------------------------------------------------------
#endregion--------------------------------------------------------------

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        super().__init__(self.width, self.height)

    def __str__(self):
        return("Square(side=" + str(self.width) + ")")

    def set_side(self, side):
        self.width = side
        self.height = side

shape_calc_test(Rectangle, Square)