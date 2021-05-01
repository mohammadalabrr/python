class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    def set_width(self, width):
        self.width = width
        return self.width
    def set_height(self, height):
        self.height = height
        return self.height
    def get_area(self):
        area = self.width * self.height
        return area
    def get_perimeter(self):
        perm = (self.width * 2) + (self.height * 2)
        return perm
    def get_diagonal(self):
        diag = (self.width ** 2 + self.height ** 2) ** .5
        return diag
    def get_picture(self):
        line = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        if self.width <= 50:
            pwidth = "*" * self.width
            for n in range(0, self.height):
                line = pwidth + "\n" + line
            return line
        elif self.height <= 50:
            pwidth = "*" * self.width
            for n in range(0, self.height):
                line = pwidth + "\n" + line
            return line

    def get_amount_inside(self, shape):
        self.shape = shape
        if type(self.shape) == Square:
          num_times = self.get_area()/(self.width * self.height)
          return int(num_times)
        else:
          num_times = self.get_area()/(self.width * self.height)
          return int(num_times)
        
            

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        return "Square(side={})".format(self.width)
    def set_side(self, side):
        self.width = side
        self.height = side
        return self.width, self.height
    def set_width(self, side):
        self.width = side
        self.height = side
        return self.width, self.height
    def set_height(self, side):
        self.height = side
        self.width = side
        return self.height, self.width
