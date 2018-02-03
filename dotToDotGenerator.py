from PIL import Image, ImageDraw, ImageStat,ImageFilter,ImageOps
import cv2
import numpy as np

# Adaption of answer https://stackoverflow.com/a/10575940/355230
def halftone(img, sample, scale, angle=45):
    ''' Returns a halftone image created from the given input image "img".
        "sample" (in pixels), determines the sample box size from the original
        image. The maximum output dot diameter is given by "sample" * "scale"
        (which is also the number of possible dot sizes). So "sample" == 1 will
        preserve the original image resolution, but "scale" must be > 1 to allow
        variations in dot size.
    '''
    img_grey = img.convert('L')  # Convert to greyscale.
    channel = img_grey.split()[0]  # Get grey pixels.
    channel = channel.rotate(angle, expand=1)
    size = channel.size[0]*scale, channel.size[1]*scale

    bitmap = Image.new('1', size)
    draw = ImageDraw.Draw(bitmap)

    for x in range(0, channel.size[0], sample):
        for y in range(0, channel.size[1], sample):
            box = channel.crop((x, y, x+sample, y+sample))
            mean = ImageStat.Stat(box).mean[0]
            diameter = (mean/255) ** 0.5
            edge = 0.5 * (1-diameter)
            x_pos, y_pos = (x+edge) * scale, (y+edge) * scale
            box_edge = sample * diameter * scale
            draw.ellipse((x_pos, y_pos, x_pos+box_edge, y_pos+box_edge),
                         fill=255)

    bitmap = bitmap.rotate(-angle, expand=1)
    width_half, height_half = bitmap.size
    xx = (width_half - img.size[0]*scale) / 2
    yy = (height_half - img.size[1]*scale) / 2
    bitmap = bitmap.crop((xx, yy, xx + img.size[0]*scale,
                                  yy + img.size[1]*scale))
    return Image.merge('1', [bitmap])

# Sample usage

img = Image.open('cat.jpg')
img = img.filter(ImageFilter.FIND_EDGES)
inverted_image = ImageOps.invert(img)
img = inverted_image.convert('1') 
img.show()
