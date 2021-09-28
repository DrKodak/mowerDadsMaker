from PIL import Image, ImageDraw, ImageSequence, ImageOps
from os import mkdir

#### THIS FILE SHOULD JUST OUTPUT THE SLICED GIFS

def sliceGifs(layer, base_location, gif_tuple, mowerFrames = 0):
    # Open the image
    file = str(base_location) + str(gif_tuple[0])
    image = Image.open(file)

    frameCount = 0
    fileBasePath = "sliced-gifs/" + str(layer) + "/" + str(gif_tuple[1])
    mkdir(fileBasePath)
    # print("Sliced to: ", fileBasePath) 
    for frame in ImageSequence.Iterator(image):
        frame = frame.copy()
        filePath = fileBasePath + "/frame_" + str(frameCount) + ".png"
        frame.save(filePath, "PNG")
        frameCount += 1
        if mowerFrames == 2:
            if frameCount == 2:
                return

def compileSlicedGifs():
    # Backgrounds
    BGBase      = "layers/1-background/"
    BGJapan     = ("Mount-Fuji.gif",    "Mount-Fuji")
    BGMedieval  = ("Medieval.gif",      "Medieval")
    BGMoon      = ("The-Moon.gif",      "The-Moon")
    BGRace      = ("Talladega.gif",     "Talladega")
    backgrounds = [BGJapan, BGMedieval, BGMoon, BGRace]

    # Head Effects
    HEBase = "layers/2-hateffect/"
    HEFire = ("Hot-Head.gif", "Hot-Head")
    head_effects = [HEFire]

    # Mower Effects
    MEBase   = "layers/11-mower-effects/"
    mower_effects = [("Flames.gif", "Flames"),
                     ("Shine.gif", "Shine")]

    # Diamond Hands
    DHBase      = "layers/14-diamonds/"
    DHDiamonds  = ("DiamondHands.gif", "DiamondHands")

    
    # Mowers
    MOBase   = "layers/10-mower/"
    mowers = [("Black.gif", "Black"),
              ("Blue.gif", "Blue"),
              ("Brown.gif", "Brown"),
              ("Copper.gif", "Copper"),
              ("DarkGreen.gif", "DarkGreen"),
              ("Diamond.gif", "Diamond"),
              ("Golden.gif", "Golden"),
              ("Green.gif", "Green"),
              ("LightBlue.gif", "LightBlue"),
              ("Maroon.gif", "Maroon"),
              ("Orange.gif", "Orange"),
              ("Pink.gif", "Pink"),
              ("Purple.gif", "Purple"),
              ("Red.gif", "Red"),
              ("RedOrange.gif", "RedOrange"),
              ("Seafoam.gif", "Seafoam"),
              ("Silver.gif", "Silver"),
              ("Teal.gif", "Teal"),
              ("White.gif", "White"),
              ("Yellow.gif", "Yellow"),
              ("Rainbow.gif", "Rainbow")]

    # Slice the Backgrounds
    for index in range(len(backgrounds)):
        sliceGifs("backgrounds", BGBase, backgrounds[index])

    # Slice the Head Effects
    for index in range(len(head_effects)):
        sliceGifs("head-effects", HEBase, head_effects[index])

    # Slice the Mowers
    for index in range(len(mowers)):
        sliceGifs("mowers", MOBase, mowers[index], 2)

    # Slice the Mower Effects
    for index in range(len(mower_effects)):
        sliceGifs("mower-effects", MEBase, mower_effects[index])

    # Slice the diamond hands
    sliceGifs("diamond-hands", DHBase, DHDiamonds)