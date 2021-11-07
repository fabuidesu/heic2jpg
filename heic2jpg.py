'''
fabui - HEIC to JPG converter.
Simple Python script which converts every '.heic' pictures into '.jpg' pictures in the script's directory.
Last edited: 7th November 2021
'''


from PIL import Image
import glob, os, pyheif

print("HEIC to JPEG converter - by fabui !\n")
if os.getcwd != os.path.dirname(__file__):
    os.chdir(os.path.dirname(__file__))

for file in glob.glob("*.heic"):
    print("Converting file " + str(file) + " ...")
    heic = pyheif.read(file)
    im = Image.frombytes(heic.mode, heic.size, heic.data, "raw", heic.mode, heic.stride)
    im.convert("RGB")
    im.save(os.path.splitext(file)[0]+".jpg", "JPEG")

print("\nDone!\n")