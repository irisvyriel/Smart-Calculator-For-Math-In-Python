from math_ocp import * 
import time

class SmartCalculator:

    def user_input():
        
        print("Welcome to My Smart Calculator")
        print("Here are the lists which you chooce")
        print("1. Flat Building" "\n"
              "2. Space Building")
        user_input1 = str(input("What Do you wanna choose?" "\n"
                                "Your Answer = " ))
        if user_input1 == "1":

            print("1. Rectangle" "\n"
                "2. Circle" "\n"
                "3. Triangle" "\n"
                "4. Trapezium" "\n"
                "5. Rhombus" "\n"
                "6. Parallelogram")
            
            if user_input1 == "1":
                rectangle = Shape("rectangle", width=int(input("Width = ")), height=int(input("Height = ")))
                print("Your Rectangle Calculate is = ", rectangle.calculate_area())

            elif user_input1 == "2":
                circle = Shape("circle", radius=float(input("Radius = ")))
                print("Your Circle Calculate is = ", circle.calculate_area())

            elif user_input1 == "3":
                triangle = Shape("triangle", pedestal=int(input("Pedestal = ")), height=int(input("Height = ")))
                print("Your Triangle Calculate is = ", int(triangle.calculate_area()))
            
            elif user_input1 == "4":
                trapezium = Shape("trapezium", pedestal=int(input("Pedestal = ")), base=int(input("Base = ")), height=int(input("Height = ")))
                print("Your Trapezium Calculate is = ", int(trapezium.calculate_area()))
            
            elif user_input1 == "5":
                Rhombus = Shape("Rhombus", diagonal1 = int(input("Diagonal 1 = ")), diagonal2 = int(input("Diagonal 2 = ")))
                print("Your Rhombus Calculate is = ", int(Rhombus.calculate_area()))
            
            elif user_input1 == "6":
                parallelogram = Shape("parallelogram", pedestal = int(input("Pedestal = ")), height = int(input("Height = ")))
                print("Your Parallelogram Calculate is = ", int(parallelogram.calculate_area()))
        
        elif user_input1 == "2":

            print("1. Cube" "\n"
                  "2. Block" "\n"
                  "3. Rectangular Pyramid" "\n"
                  "4. Triangular Prism" "\n"
                  "5. Triangular Pyramid" "\n"
                  "6. Tube" "\n"
                  "7. Cone" "\n"
                  "8. Sphere")
            user_input2 = str(input("Your Answer : "))
            if user_input2 == "1":

                Cube = GeometryArea("cube", lateral1 = int(input("Lateral 1 = ")), lateral2 = int(input("Lateral 2 = ")))
                print("Your Cube Calculate is ", Cube.calculate_area())
            
            elif user_input2 == "2":

                Block = GeometryArea("block", width = int(input("Width = ")), height = int(input("Height = ")))
                print("Your Block Calculate is = ", Block.calculate_area())
            
            elif user_input2 == "3":

                Rectangular_pyramid = GeometryArea("rectangular_pyramid", side_area1 = int(input("Side Area 1 = ")), 
                                               side_area2 = int(input("Side Area 2 = ")), side_area3 = int(input("Side Area 3 = ")),
                                               side_area4 = int(input("Side Area 4 = ")), side_area5 = int(input("Side Area 5 = ")))
                print("Your Rectangular Pyramid Calculate is = ", Rectangular_pyramid.calculate_area())
            
            elif user_input2 == "4":

                Triangular_prism = GeometryArea("triangular_prism", side1 = int(input("Side 1 = ")), 
                                            side2 = int(input("Side 2 = ")), side3 = int(input("Side 3 = ")),
                                            height = int(input("Height = ")))
                print("Your Triangular Prism Calculate is = ", Triangular_prism.calculate_area())
            
            elif user_input2 == "5":

                Triangular_pyramid = GeometryArea("triangular_pyramid", side_area1 = int(input("Side Area 1 = ")), 
                                               side_area2 = int(input("Side Area 2 = ")), side_area3 = int(input("Side Area 3 = ")),
                                               side_area4 = int(input("Side Area 4 = ")))
                print("Your Triangular Pyramid Calculate is = ", Triangular_pyramid.calculate_area())
            
            elif user_input2 == "6":

                Tube = GeometryArea("tube", radius = int(input("Radius = ")), height = int(input("Height = ")))
                print("Your Tube Calculate is = ", Tube.calculate_area())
            
            elif user_input2 == "7":

                Cone = GeometryArea("cone", radius = int(input("Radius = ")), side = int(input("Side = ")))
                print("Your Cone Calculate is = ", Cone.calculate_area())
            
            elif user_input2 == "8":

                Sphere = GeometryArea("sphere", radius1 = int(input("Radius 1 = ")), radius2 = int(input("Radius 2 = ")))
                print("Your Sphere Calculate is = ", Sphere.calculate_area())

SmartCalculator.user_input()
