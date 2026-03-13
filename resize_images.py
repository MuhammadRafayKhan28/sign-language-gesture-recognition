import os 
import cv2

dataset_path="dataset"
size=(64,64)

for folder in os.listdir(dataset_path):
    folder_path=os.path.join(dataset_path,folder)

    if os.path.isdir(folder_path):
        for img_name in os.listdir(folder_path):
            img_path=os.path.join(folder_path,img_name)

            img=cv2.imread(img_path)

            if img is None:
                continue 
            resized=cv2.resize(img,size)
            cv2.imwrite(img_path,resized)
print("all images resized")
        
   