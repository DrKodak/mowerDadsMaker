import os
import glob

assetFile = open("AssetList.txt", 'w')

dirs = glob.glob("layers/*")
print(dirs)
for folder in dirs:
    assetFile.write('\n' + folder + '\n')
    for filepath in os.listdir(folder):
        assetFile.write('("' + str(filepath)[:-4] + '", xyz),' + '\n')    

assetFile.close()