from wand.image import Image
from wand.api import library
# from makeDads import MowerDad
# from makeDads import AttributesList

def savePFP(dadID, pfpFrame):
    pfpFrame.crop(170, 0, 570, 400)
    pfpFrame.save(filename="dads/dadPfPs/MowerDad{}.png".format(dadID))

def compileDad(dadID, mowerDad):

    attributes = mowerDad.getAttributes()

    hoodGoodList = ["Afro",
                   "Bandana",
                   "BaseballCap",
                   "Bowl",
                   "BucketHat",
                   "CrossCut",
                   "CurlyTop",
                   "Einstein",
                   "Emo",
                   "Fauxhawk",
                   "Fez",
                   "FlamingBuffalo",
                   "HardHat-Yellow",
                   "HighTop",
                   "Lockes",
                   "MalePattern",
                   "Monk",
                   "Morpher",
                   "Napoleon",
                   "None",
                   "PartyHat",
                   "Pirate",
                   "RicePaddy",
                   "SlickedBack",
                   "SpaceScientist",
                   "StrawHat",
                   "TheVeryBest",
                   "TopHat",
                   "Ushanka",
                   "Viking"]

    # Get all of the static layers to be used
    dad         = Image(filename = "layers/3-dad/{}.png".format(attributes.Skin))
    shirt       = Image(filename = "layers/4-shirt/{}.png".format(attributes.Shirt))
    legs        = Image(filename = "layers/5-legs/{}.png".format(attributes.Legs))
    hat         = Image(filename = "layers/6-hat/{}.png".format(attributes.Hat))
    face        = Image(filename = "layers/7-face/{}.png".format(attributes.Face))
    hand        = Image(filename = "layers/8-hand/{}.png".format(attributes.Item))
    shoes       = Image(filename = "layers/9-shoes/{}.png".format(attributes.Shoes))
    legsTrim    = Image(filename = "layers/12-legs-trim/{}Trim.png".format(attributes.Legs))
    if(len(attributes.Shirt) >= 5 and attributes.Shirt[:5] == "Hoody" and attributes.Hat in hoodGoodList):
        hood    = Image(filename = "layers/13-hoody-hoods/{}.png".format(attributes.Shirt))
    else:
        hood    = Image(filename = "layers/13-hoody-hoods/None.png")

    dad.composite(shirt)
    dad.composite(hood)
    dad.composite(legs)
    dad.composite(hat)
    dad.composite(face)
    dad.composite(hand)
    dad.composite(shoes)

    with Image() as new_gif:
        with Image() as diamond_gif:
            img_path_base      = "sliced-gifs/backgrounds/{}/frame_".format(attributes.Background)
            eff_path_base      = "sliced-gifs/head-effects/{}/frame_".format(attributes.Effect)
            mow_path_base      = "sliced-gifs/mowers/{}/frame_".format(attributes.Mower)
            mow_eff_path_base  = "sliced-gifs/mower-effects/{}/frame_".format(attributes.MowerEffect)
            diamond_path_base  = "sliced-gifs/diamond-hands/DiamondHands/frame_"

            mow_path1         = mow_path_base  + "0.png"
            mow_path2         = mow_path_base  + "1.png"
            mowImage1         = Image(filename=mow_path1)
            mowImage2         = Image(filename=mow_path2)

            swap = True
            for idx in range(36):
                img_path     = img_path_base  + "{}.png".format(idx)
                eff_path     = eff_path_base  + "{}.png".format(idx)
                effectIdx = idx
                if attributes.MowerEffect == "Flames":
                    effectIdx = effectIdx % 2
                mow_eff_path = mow_eff_path_base + "{}.png".format(effectIdx)
                diamond_path = diamond_path_base + "{}.png".format(idx)

                with Image(filename=img_path) as backFrame:
                    backFrame.composite(Image(filename=eff_path))
                    backFrame.composite(dad)
                    diamond_png_copy = Image(backFrame)
                    diamond_png_copy.composite(Image(filename=diamond_path))
                    if(swap):
                        backFrame.composite(mowImage1)
                        diamond_png_copy.composite(mowImage1)
                        swap = False
                    else:
                        backFrame.composite(mowImage2)
                        diamond_png_copy.composite(mowImage2)
                        swap = True
                    mow_eff = Image(filename=mow_eff_path)
                    backFrame.composite(mow_eff)
                    diamond_png_copy.composite(mow_eff)
                    backFrame.composite(legsTrim)
                    diamond_png_copy.composite(legsTrim)
                    
                    new_gif.sequence.append(backFrame)
                    diamond_gif.sequence.append(diamond_png_copy)
                    
                    if idx == 35:
                        savePFP(dadID, backFrame)
                        savePFP(str(str(dadID) + "D"), diamond_png_copy)

            new_gif.save(filename="dads/dadGifs/MowerDad" + str(dadID) + ".gif")
            diamond_gif.save(filename="dads/diamondDad/MowerDad" + str(dadID) + ".gif")