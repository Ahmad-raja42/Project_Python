# let's craete a function.
def square():
  square_side = input('Enter the side:-')
  square_side = int(square_side)
  area = square_side * square_side
  perimeter = 4 * square_side
  print("Square side:-", square_side)
  print("Square side:-", area)
  print("Square side:-", perimeter)


def rectangle():
  length = input('Enter the length of rectangle:-')
  breath = input('Enter the breath of rectangle:-')
  length = int(length)
  breath = int(breath)
  area = length * breath
  perimeter = 2 * (length + breath)
  print("Rectangle area:-", area)
  print("rectangle perimeter:-", perimeter)


def circle():
  radius = input('Enter the radius of circle:-')
  radius = int(radius)
  area = 3.14 * radius * radius
  perimeter = 2 * 3.14 * radius
  print("Area of cirle:-", area)
  print("Perimeter of circle:-", perimeter)

def mensuration_app(shape):
  if shape == 'square':
    square()
  elif shape == 'rectangle':
    rectangle()
  elif shape == 'circle':
    circle()

mensuration_app('rectangle')