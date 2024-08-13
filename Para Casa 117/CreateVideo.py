import os
import cv2

path = "Image/"

Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)

        Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])
height, width, canais = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(0, count-1):
    frame = cv2.imread(Images[i])
    out.write(frame)

print("Concluido")