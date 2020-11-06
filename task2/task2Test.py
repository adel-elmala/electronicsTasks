from PIL import Image, ImageDraw


def mapCoordinates(left,down):
    """
        Maps the coordinates from cm to Pixels fitted to the Floor image, 
        coordinates are measured from top left corner

    """
    # image width  = 299 pixels 
    # image height  = 730 pixels

    # floor height // till H-hallway = (4465.7) cm 
    
    # floor width = (2509.9) cm 
    # floor height = (4465.7) + 2347.6 = (6814.8) cm 

    # White padding : 250 cm left , 250 cm down

    # (without padding)
    # for width = Each cm eq. to ~ 8.5 pixels  
    # for height = Each cm eq. to ~ 9.5 pixels  

    #(with pading from left and top)
    # for width  = 9.5 pixels per cm   
    # for height =  10 pixels per cm

    x = round(left / 9.5)
    y = round(down / 10) 
    return (x,y)

def drawSqaure(img,coordinates,saveTo):
    with Image.open(img) as im:
        draw = ImageDraw.Draw(im)
        #AT 1176 cm left / 3423.7 should be at net lab
        #(138,360)
        # draw.point((133,266),fill=128)
        p1 = coordinates
        p2 = (coordinates[0] + 10 , coordinates[1] + 10)
        draw.rectangle([p1,p2],outline=128,fill=128,width=10)
        im.save(saveTo, "PNG")  



img = "departmentFloorMap.jpg"
saved = "modified.png"

# down Hallway starts at (1426,3054)
coords = mapCoordinates(1426+311.4,1634.4+3054)
drawSqaure(img,coords,saved)