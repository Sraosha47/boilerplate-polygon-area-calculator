class Rectangle():
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
      return("Rectangle(width="+ str(self.width) + ", height="+ str(self.height) +")")

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

  def get_picture(self):
      self.picture = ''
      i = 0
      while i < (self.height):
          self.picture += self.width * "*" + "\n"
          i += 1
      return(self.picture)


class Square(Rectangle):
  def __init__(self, side):
      self.width = side
      self.height = side
      super().__init__(self.width, self.height)

