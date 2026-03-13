import os
import random
import shutil

dataset_path = "dataset"
Training_Path = "dataset/train"
Testing_Path = "dataset/test"

os.makedirs(Training_Path, exist_ok=True)
os.makedirs(Testing_Path, exist_ok=True)

for folder in os.listdir(dataset_path):
    folder_path = os.path.join(dataset_path, folder)
    if os.path.isdir(folder_path) and folder not in ["train", "test"]:
        img = os.listdir(folder_path)
        random.shuffle(img)
        split_IND = int(len(img) * 0.8)
        Train_img = img[:split_IND]
        Test_img = img[split_IND:]
        os.makedirs(os.path.join(Training_Path, folder), exist_ok=True)
        os.makedirs(os.path.join(Testing_Path, folder), exist_ok=True)
        for img in Train_img:
            shutil.move(
                os.path.join(folder_path, img),
                os.path.join(Training_Path, folder, img)
            )
        for img in Test_img:
            shutil.move(
                os.path.join(folder_path, img),
                os.path.join(Testing_Path, folder, img)
            )
print("dataset has been split into train and test")