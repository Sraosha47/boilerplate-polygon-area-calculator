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

  def get_diagonal(self):
      self.diagonal = (self.width ** 2 + self.height ** 2) ** .5
      return(self.diagonal)

class Square(Rectangle):
    pass
