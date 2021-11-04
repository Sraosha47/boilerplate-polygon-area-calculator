class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height
  #region methods-------------------
  def get_area(self):
      self.area = self.width * self.height
      return(self.area)



class Square(Rectangle):
    pass
