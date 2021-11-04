class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height
  #region methods-------------------
  def get_area(self):
      self.area = self.width * self.height
      return(self.area)

  def get_perimeter(self):
      self.perimeter = 2 * self.width + 2 * self.height
      return(self.perimeter)


class Square(Rectangle):
    pass
