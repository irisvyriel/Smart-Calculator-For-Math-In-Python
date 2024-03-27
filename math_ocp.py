from math import *


class ShapeArea:

# Bangun Datar 
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type

        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]

        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

        elif self.shape_type == "triangle":
            self.pedestal = kwargs["pedestal"]
            self.height = kwargs["height"]

        elif self.shape_type == "trapezium":
            self.pedestal = kwargs["pedestal"]
            self.height = kwargs["height"]
            self.base = kwargs["base"]

        elif self.shape_type == "Rhombus":
            self.diagonal1 = kwargs["diagonal1"]
            self.diagonal2 = kwargs["diagonal2"]

        elif self.shape_type == "parallelogram":
            self.height = kwargs["height"]
            self.pedestal = kwargs["pedestal"]

    def calculate_area(self) -> int:
        # Calculate Area
        if self.shape_type == "rectangle":
            return self.width * self.height
        
        elif self.shape_type == "circle":
            return pi * self.radius ** 2
        
        elif self.shape_type == "triangle":
            return self.pedestal * self.height / 2
        
        elif self.shape_type == "trapezium":
            return (self.pedestal + self.base) * self.height / 1/2
        
        elif self.shape_type == "Rhombus":
            return self.diagonal1 * self.diagonal2 / 2
        
        elif self.shape_type == "parallelogram":
            return self.pedestal * self.height 

class ShapeParameter:


    def __init__(self, shape_volume, **kwargs):
        self.shape_volume = shape_volume

        if self.shape_volume == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        
        elif self.shape_volume == "circle":
            self.radius = kwargs["radius"]
        
        elif self.shape_volume == "triangle":
            self.pedestal1 = kwargs["pedestal1"]
            self.pedestal2 = kwargs["pedestal2"]
            self.pedestal3 = kwargs["pedestal3"]
        
        elif self.shape_volume == "trapezium":
            self.pedestal1 = kwargs["pedestal1"]
            self.pedestal2 = kwargs["pedestal2"]
            self.pedestal3 = kwargs["pedestal3"]
            self.pedestal4 = kwargs["pedestal4"]
        
        elif self.shape_volume == "Rhombus":
            self.pedestal1 = kwargs["pedestal1"]
            self.pedestal2 = kwargs["pedestal2"]
            self.pedestal3 = kwargs["pedestal3"]
            self.pedestal4 = kwargs["pedestal4"]
        
        elif self.shape_volume == "parallelogram":
            self.pedestal1 = kwargs["pedestal1"]
            self.pedestal2 = kwargs["pedestal2"]
            self.pedestal3 = kwargs["pedestal3"]
            self.pedestal4 = kwargs["pedestal4"]
    
    def calculate_perimeter(self) -> int:
        # Calculate Perimeter
        if self.shape_volume == "rectangle":
            return (2 * self.height) + (2 * self.width)
        
        elif self.shape_volume == "circle":
            return pi * 2 * self.radius
        
        elif self.shape_volume == "triangle":
            return self.pedestal1 + self.pedestal2 + self.pedestal3
        
        elif self.shape_volume == "trapezium":
            return self.pedestal1 + self.pedestal2 + self.pedestal3 + self.pedestal4
        
        elif self.shape_volume == "Rhombus":
            return self.pedestal1 + self.pedestal2 + self.pedestal3 + self.pedestal4
        
        elif self.shape_volume == "parallelogram":
            return self.pedestal1 + self.pedestal2 + self.pedestal3 + self.pedestal4


class GeometryArea:

# Bangun Ruang
    def __init__(self, geometry_type_area, **kwargs):
        self.geometry_type_area = geometry_type_area

        if self.geometry_type_area == "cube": 
            self.lateral1 = kwargs["lateral1"]
            self.lateral2 = kwargs["lateral2"]

        elif self.geometry_type_area == "block":
            self.width = kwargs["width"]
            self.height = kwargs["height"]

        elif self.geometry_type_area == "rectangular_pyramid":
            self.side_area1 = kwargs["side_area1"]
            self.side_area2 = kwargs["side_area2"]
            self.side_area3 = kwargs["side_area3"]
            self.side_area4 = kwargs["side_area4"]
            self.side_area5 = kwargs["side_area5"]

        elif self.geometry_type_area == "triangular_prism":
            self.side1 = kwargs["side1"]
            self.side2 = kwargs["side2"]
            self.side3 = kwargs["side3"]
            self.height = kwargs["height"]

        elif self.geometry_type_area == "triangular_pyramid":
            self.side_area1 = kwargs["side_area1"]
            self.side_area2 = kwargs["side_area2"]
            self.side_area3 = kwargs["side_area3"]
            self.side_area4 = kwargs["side_area4"]

        elif self.geometry_type_area == "tube":
            self.radius = kwargs["radius"]
            self.height = kwargs["height"]

        elif self.geometry_type_area == "cone":
            self.radius = kwargs["radius"]
            self.side = kwargs["side"]

        elif self.geometry_type_area == "sphere":
            self.radius1 = kwargs["radius1"]
            self.radius2 = kwargs["radius2"]

    def calculate_area(self) -> int:
        # Calculate Area
        if self.geometry_type_area == "cube":
            return 6 * self.lateral1 * self.lateral2
        
        elif self.geometry_type_area == "block":
            return (2 * self.width + self.height) + (2 * self.width + self.height) + (2 * self.width + self.height)
        
        elif self.geometry_type_area == "rectangular_pyramid":
            return self.side_area1 + self.side_area2 + self.side_area3 + self.side_area4 + self.side_area5
        
        elif self.geometry_type_area == "triangular_prism":
            return (self.side1 + self.side2 + self.side3) * self.height
        
        elif self.geometry_type_area == "triangular_pyramid":
            return self.side_area1 + self.side_area2 + self.side_area3 + self.side_area4
        
        elif self.geometry_type_area == "tube":
            return 2 * pi * self.radius * self.height
        
        elif self.geometry_type_area == "cone":
            return pi * self.radius * self.side
        
        elif self.geometry_type_area == "sphere":
            return 4 * pi * self.radius1 * self.radius2

class GeometryVolume:

    def __init__(self, geometry_type_volume, **kwargs):
        self.geometry_type_volume = geometry_type_volume

        if self.geometry_type_volume == "cube":
            self.lateral1 = kwargs["lateral1"]
            self.lateral2 = kwargs["lateral2"]
            self.lateral3 = kwargs["lateral3"]

        elif self.geometry_type_volume == "block":
            self.lenght = kwargs["lenght"]
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        
        elif self.geometry_type_volume == "rectangular_pyramid":
            self.pedestal = kwargs["pedestal"]
            self.height = kwargs["height"]
        
        elif self.geometry_type_volume == "triangular_prism":
            self.pedestal = kwargs["pedestal"]
            self.height = kwargs["height"]
            self.Height = kwargs["Height"]
        
        elif self.geometry_type_volume == "triangular_pyramid":
            self.pedestal = kwargs["pedestal"]
            self.height = kwargs["height"]
            self.Height = kwargs["Height"]
        
        elif self.geometry_type_volume == "tube":
            self.radius1 = kwargs["radius1"]
            self.radius2 = kwargs["radius2"]
            self.height = kwargs["height"]
        
        elif self.geometry_type_volume == "cone":
            self.radius1 = kwargs["radius1"]
            self.radius2 = kwargs["radius2"]
            self.height = kwargs["height"]
        
        elif self.geometry_type_volume == "sphere":
            self.radius1 = kwargs["radius1"]
            self.radius2 = kwargs["radius2"]
            self.radius3 = kwargs["radius3"]
        
    def calculate_volume(self) -> int:
        # Calculate Volume
        if self.geometry_type_volume == "cube":
            return self.lateral1 * self.lateral2 * self.lateral3
        
        elif self.geometry_type_volume == "block":
            return self.lenght * self.width * self.height
        
        elif self.geometry_type_volume == "rectangular_pyramid":
            return (self.pedestal * self.height) / 3
        
        elif self.geometry_type_volume == "triangular_prism":
            return (self.pedestal * self.height * self.Height) / 2
        
        elif self.geometry_type_volume == "triangular_pyramid":
            return (self.pedestal * self.height * self.Height) / 6
        
        elif self.geometry_type_volume == "tube":
            return pi * self.radius1 * self.radius2 * self.height
        
        elif self.geometry_type_volume == "cone":
            return (pi * self.radius1 * self.radius2 * self.height) / 3
        
        elif self.geometry_type_volume == "sphere":
            return (pi * self.radius1 * self.radius2 * self.radius3 * 4) / 3 