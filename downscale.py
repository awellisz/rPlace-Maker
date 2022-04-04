import numpy as np
import cv2

# Find the closest color (from the color dictionary) to the input color 
def closest_color(pixel):
    # Unpack the b g r values of the pixel
    pb, pg, pr = pixel
    # Empty dictionary to keep track of weighted color differences
    color_distances = {}
    
    # Loop over all colors in the dictionary
    for color, rgb in colors.items():
        # Unpack the r g b values of the color dictionary value
        cr, cg, cb = rgb
        
        # Calculate weighted color distance
        # Use "redmean" approach from ttps://en.wikipedia.org/wiki/Color_difference
        if 0.5 * (cr + pr) < 128:
            dist = 2*(cr - pr)*(cr - pr) + 4*(cg - pg)*(cg - pg) + 3*(cb - pb)*(cb - pb)
        else:
            dist = 3*(cr - pr)*(cr - pr) + 4*(cg - pg)*(cg - pg) + 3*(cb - pb)*(cb - pb)

        # Add the color and distance to the color dictionary
        color_distances[color] = dist

    # Get the key of the closest color 
    closest_col = min(color_distances, key=color_distances.get)
    # Return as a tuble of the form (b, g, r) 
    return colors[closest_col][::-1]


colors = {
    "BURGUNDY": (109, 0, 26),
    "DARK_RED": (190, 0, 57),
    "RED": (255, 69, 0),
    "ORANGE": (255, 168, 0),
    "YELLOW": (255, 214, 53),
    "PALE_YELLOW": (255, 248, 184),
    "DARK_GREEN": (0, 163, 104),
    "GREEN": (0, 204, 120),
    "LIGHT_GREEN": (126, 237, 86),
    "DARK_TEAL": (0, 117, 111),
    "TEAL": (0, 158, 170),
    "LIGHT_TEAL": (0, 204, 192),
    "DARK_BLUE": (36, 80, 164),
    "BLUE": (54, 144, 234),
    "LIGHT_BLUE": (81, 233, 244),
    "INDIGO": (73, 58, 193),
    "PERIWINKLE": (106, 92, 255),
    "LAVENDER": (148, 179, 255),
    "DARK_PURPLE": (129, 30, 159),
    "PURPLE": (180, 74, 192),
    "PALE_PURPLE": (228, 171, 255),
    "MAGENTA": (222, 16, 127),
    "PINK": (255, 56, 129),
    "LIGHT_PINK": (255, 153, 170),
    "DARK_BROWN": (109, 72, 47),
    "BROWN": (156, 105, 38),
    "BEIGE": (255, 180, 112),
    "BLACK": (0, 0, 0),
    "DARK_GRAY": (81, 82, 82),
    "GRAY": (137, 141, 144),
    "LIGHT_GRAY": (212, 215, 217),
    "WHITE": (255, 255, 255)
    }

if __name__ == "__main__":
    
    img = cv2.imread('phoenix2.png', 1)
    #cv2.imshow('Original', img)

    height, width, _ = img.shape
    new_width = 36
    ratio = new_width / width
    new_height = int(height * ratio)

    res = cv2.resize(img, dsize=(new_width, new_height), interpolation=cv2.INTER_AREA)
    #cv2.imshow('Downscaled', res)
    cv2.imwrite('phoenix_downscaled.png', res)

    rows, cols, _ = res.shape

    for row in range(rows):
        for col in range(cols):
            res[row][col] = closest_color(res[row][col])

    #cv2.imshow('Colored', res)
    cv2.imwrite('phoenix_downscaled_palette.png', res)
            
