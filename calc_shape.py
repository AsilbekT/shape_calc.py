# here we are creating the rectangle function we have l and b variables to calculate the area of this shape 
def rectangle():
    l,b =input("Enter rectangle's length and breadth (seperate them with space  no comma): ").split()
    l=int(l)
    b=int(b)
    rect_area = l * b
    print(f"The area of rectangle is {rect_area}.")

# it is the square function we are creating  and we have only s variable which stands for side length and we are squaring it  
def square():
    s = int(input("Enter square's side length: "))
    sqt_area = s * s
    print(f"The area of square is {sqt_area}.")

# this is triangle function we have h and b variables and we have to multiply them all as well as 0.5
def triangle():
    h,b =input("Enter triangle's height and breadth (seperate them with space  no comma): ").split()
    h=int(h)
    b=int(b)
    # calculate area of triangle
    tri_area = 0.5 * b * h
    print(f"The area of triangle is {tri_area}.")

# here we have circle function we only need r variable and we have to multiply 3.14 to squared r
def circle():
    r = int(input("Enter circle's radius length: "))
    # calculate area of circle
    circ_area = 3.14 * r * r
    print(f"The area of circle is {circ_area}.")

# it is paralelogram's turn we have b and h variables as we know the area of this is by multiplying them that is it!
def parallelogram():
    b,h = int(input("Enter parallelogram's base length and height: ")).split()
    b=int(b)
    h=int(h)
    # calculate area of parallelogram
    para_area = b * h
    print(f"The area of parallelogram is {para_area}.")

# here we are creating the function for checking which shape the user wants and we have one empty list
# we append the input to and we can check the type of shape by looping through and we are fine!!!
def what_is_ur_shape():
    shapes=[]
    shape=input('which shape\'s area you wanna find: ' )
    if shape:
        shapes.append(shape)
        for i in shapes:
            if i=='rectangle':
                rectangle()
            elif i=='square':
                square()
            elif i=='triangle':
                triangle()
            elif i=='circle':
                circle()
            elif i=='parallelogram':
                parallelogram()   
            else:
                print('i am sorry we do not have this type of shape here') 
    else:
        print('you didn\' choose anything, enjoy!!!')

what_is_ur_shape()