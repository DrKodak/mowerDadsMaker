import os
import glob
import hashlib
import json
from compiler import compileSlicedGifs
from compilemagik import compileDad
import attributesList
from random import choices

from time import time

class AttributesList:
    Background = ""
    Effect = ""
    Skin = ""
    Shirt = ""
    Legs = ""
    Shoes = ""
    Hat = ""
    Face = ""
    Item = ""
    Mower = ""
    MowerEffect = ""
    LegsTrim = ""

    def getRandomAsset(self, assetList):
        assets = []
        weights = []
        for total in assetList:
            assets.append(str(total[0]))
            weights.append(total[1])
        asset = choices(assets, weights=weights, cum_weights = None, k=1)[0]
        # print("asset: ", asset)
        return asset

    def randomizeAttributes(self):
        self.Background  = self.getRandomAsset(attributesList.Backgrounds)
        self.Effect      = self.getRandomAsset(attributesList.Effects)
        self.Skin        = self.getRandomAsset(attributesList.Skins)
        self.Shirt       = self.getRandomAsset(attributesList.Shirts)
        self.Legs        = self.getRandomAsset(attributesList.Legs)
        self.Shoes       = self.getRandomAsset(attributesList.Shoes)
        self.Hat         = self.getRandomAsset(attributesList.Hats)
        self.Face        = self.getRandomAsset(attributesList.Faces)
        self.Item        = self.getRandomAsset(attributesList.Items)
        self.Mower       = self.getRandomAsset(attributesList.Mowers)
        self.MowerEffect = self.getRandomAsset(attributesList.MowerEffects)
        
        shineList   = ["Copper", "Silver", "Golden", "Diamond", "Rainbow"]
        if(self.Mower in shineList):
            self.MowerEffect = 'Shine'

    def attributesSha1(self):
        attList = [self.Background, 
                   self.Effect, 
                   self.Skin, 
                   self.Shirt, 
                   self.Legs, 
                   self.Shoes, 
                   self.Hat, 
                   self.Face, 
                   self.Item, 
                   self.Mower, 
                   self.MowerEffect]
        attributeString = "".join(attList)
        # print("string: ", attributeString)
        attributeBytes = attributeString.encode('utf-8')
        hash_func = hashlib.sha1()
        hash_func.update(attributeBytes)
        hashedString = hash_func.hexdigest()
        return hashedString


class MowerDad:
    description = "This dad is hard at work mowing the yard."
    name = "MowerDad X"
    image = "FIGURE THIS OUT LATER"
    edition = 0
    attributes = ""
    metadata = {}

    def __init__(self, edition, attributes):
        self.name = "MowerDad ".format(edition)
        self.edition = edition
        self.attributes = attributes    

    def newDad(self, edition, attributes):
        self.name = "MowerDad ".format(edition)
        self.edition = edition
        self.attributes = attributes

    def setEdition(self, edition):
        self.edition = edition

    def setAttributes(self, attributes):
        self.attributes = attributes

    def getAttributes(self):
        return self.attributes

    def formatMetadata(self):
        attMetadata = {"Background": self.attributes.Background,
                        "Effect": self.attributes.Effect,
                        "Skin": self.attributes.Skin,
                        "Shirt": self.attributes.Shirt,
                        "Legs": self.attributes.Legs,
                        "Shoes": self.attributes.Shoes,
                        "Hat": self.attributes.Hat,
                        "Face": self.attributes.Face,
                        "Item": self.attributes.Item,
                        "Mower": self.attributes.Mower,
                        "MowerEffect": self.attributes.MowerEffect}
        metadata = {
            "description": self.description,
            "external_url": "EXTERNAL_URL",
            "image": "IPFS NEED TO DO",
            "name": "Mower Dad #{}".format(self.edition),
            "attributes": attMetadata, 
        }
        return metadata


def clearDir(path):
    dirs = glob.glob(str(path) + '/*')
    for folder in dirs:
        for filepath in os.listdir(folder):
            os.remove(folder + "/{}".format(filepath))
        os.rmdir(folder)    

def clearAndSlice(clearSliced, clearDads):
    ## Start by removing all of the sliced-gifs layers
    if(clearSliced):
        clearDir('sliced-gifs/backgrounds')
        clearDir('sliced-gifs/diamond-hands')
        clearDir('sliced-gifs/head-effects')
        clearDir('sliced-gifs/mower-effects')
        clearDir('sliced-gifs/mowers')
        ## Now repopulate the slice gif folders by calling the compiler function
        compileSlicedGifs()

    if(clearDads):
        clearDir('dads/')
        os.mkdir('dads/dadGifs')
        os.mkdir('dads/dadPfps')
        os.mkdir('dads/dadMetadata')
        os.mkdir('dads/diamondDad')

def writeMetadataToFile(dadID, metadata):
    jsonData = json.dumps(metadata)
    filename = "{}.json".format(dadID) 
    file = open("dads/dadMetadata/{}".format(filename), 'w')
    file.write(jsonData)
    file.close()

def makeDad(dadID, mowerDad):
    # Get a random set of assets
    # Determine if the random set is found in the whole group to prevent dupes
    compileDadTime = time()

    compileDad(dadID, mowerDad)

    print("---MAKE DAD TIME: %s seconds ---" % (time() - compileDadTime))
    return

def makeAllDads():
    start_time = time()

    clearSliced = False
    clearDads = True
    clearAndSlice(clearSliced, clearDads)
    totalDads = 100
    attList = AttributesList()
    mowerDad = MowerDad(0, attList)

    hashSet = set()
    for dadID in range(totalDads):
        print(dadID)
        
        attHash = ""
        hashInSet = True
        while(hashInSet):
            attList.randomizeAttributes()
            attHash = attList.attributesSha1()
            hashInSet = attHash in hashSet
        hashSet.add(attHash)
        mowerDad.setEdition(dadID)
        mowerDad.setAttributes(attList)
        makeDad(dadID, mowerDad)
        writeMetadataToFile(dadID, mowerDad.formatMetadata())

    print("--- TOTAL TIME: %s seconds ---" % (time() - start_time))


makeAllDads()