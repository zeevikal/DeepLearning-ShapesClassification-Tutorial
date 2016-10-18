# Shape Generator - Circle, Rectangle & Square
# by: Zeevikal

import numpy
import cairo
import math
import random
from random import randint
import Image

x=0
for image in range(0,2):

    shapeSize = randint(200, 400)
    data = numpy.zeros((shapeSize, shapeSize, 4), dtype=numpy.uint8)
    surface = cairo.ImageSurface.create_for_data(
        data, cairo.FORMAT_ARGB32, shapeSize, shapeSize)
    cr = cairo.Context(surface)
    # cr.scale(random.uniform(0,1),random.uniform(0,1)) #Shape size (0-100%)
    cr.translate(random.uniform(0,100),random.uniform(0,100)) #Shape Positopn
    x+=1

    # fill with solid color
    cr.set_source_rgb(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    cr.paint()

    # draw border shape
    cr.arc(100, 100, 80, 0, 2*math.pi)  # Circle
    # cr.rectangle(20, 150, 20, 150)     # Rectangle
    # cr.rectangle(40, 40, 40, 40)     # Square

    cr.set_line_width(3)
    cr.set_source_rgb(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
    cr.stroke()

    # write output
    print data[38:48, 38:48, 0]
    surface.write_to_png("/home/zeev/PycharmProjects/shapeGenerator/test1/"+"_Circle_"+
                         str(0+int(x))+".png")
    im = Image.open("/home/zeev/PycharmProjects/shapeGenerator/test1/"+"_Circle_"+
                         str(0+int(x))+".png")
    im.save("/home/zeev/PycharmProjects/shapeGenerator/test1/"+"_Circle_"+
                         str(0+int(x))+".jpg")
print "Done"
