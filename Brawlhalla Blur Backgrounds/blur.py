import cv2
import numpy as np
import os
path="D:\Software\Steam\steamapps\common\Brawlhalla\mapArt\Backgrounds"
path=input("Please provide your brawlhalla game files folder:(eg: C:\Program Files\steam\steamapps\common\Brawlhalla ) ")+"\mapArt\Backgrounds"
while not os.path.isdir(path):
    path=input("that is not a valid folder path, please try again ")+"\mapArt\Backgrounds"
images_path=[]
final_images=[]
file_names=[]
dirpath =os.walk(path)
dirpath=list(dirpath)
for item in dirpath[0][2]:
    images_path.append(dirpath[0][0]+"\\"+item)
    print(str(len(images_path))+" _ "+dirpath[0][0]+item)
    file_names.append(item)
excluded=int(input("type in the index of the file you want to exclude, else type 0: "))
while excluded!=0:
    if excluded<=len(images_path):
        images_path.remove(images_path[excluded-1])
    for i in images_path:
        print(str(images_path.index(i)+1)+" _ "+ i)
    excluded=int(input("type in the index of the file you want to exclude, else type 0: "))
blur_amount=int(input("please specify the amount of blur you want to apply(just a good ol' integer): "))

#f= cv2.imread("D:\Software\Steam\steamapps\common\Brawlhalla\mapArt\Backgrounds\BG_AT.jpg")
#cv2.imshow("sdq",f)
#cv2.waitKey()
for image in images_path:
    f=cv2.imread(image)
    f=cv2.blur(f,(blur_amount,blur_amount))
    final_images.append(f)
export_folder=path+"\\blurred"
if not os.path.isdir(export_folder):
    os.mkdir(export_folder)
inp=input("done, do you want to see a preview? (y/n) ")
if inp=="y":
    cv2.imwrite(export_folder+"\\test.jpg",final_images[0])
    preview=cv2.imread(export_folder+"\\test.jpg")
    cv2.imshow("test",preview)
    cv2.waitKey()
inp=input("do you want to save the files? (y/n) ")
if inp=="y":
    for i in range(0,len(final_images)-1):
        im=final_images[i]
        cv2.imwrite(export_folder+'\\'+file_names[i],im)
    print("saved")
    input("check your the folder here"+export_folder+ "and copy (and replace) the files to mapart/backgrounds to apply the mod...\n enjoyyy!!! <3 ")
