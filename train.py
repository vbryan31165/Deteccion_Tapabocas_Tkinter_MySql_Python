import cv2
import os
import numpy as np

dataPath = "C:/Users/RYZEN/OneDrive/Documents/python/Tkinter_MySQL/Dataset_faces"
dir_list = os.listdir(dataPath)
print("Lista de archivos", dir_list)

labels = []
facesData = []
label = 0

for name_dir in dir_list:
    dir_path = dataPath + "/" + name_dir

    for file_name in os.listdir(dir_path):
        image_path = dir_path + "/" + file_name
        print(image_path)
        image = cv2.imread(image_path, 0)
        # cv2.imshow("imagen",image)
        # cv2.waitKey(10)
        facesData.append(image)
        labels.append(label)
    label += 1

print("etiqueta 0:", np.count_nonzero(np.array(labels) == 0))
print("etiqueta 1:", np.count_nonzero(np.array(labels) == 1))


# LBPH FaceReconognizer

face_mask = cv2.face.LBPHFaceRecognizer_create()

# entrenamiento

print("entrenando...")
face_mask.train(facesData, np.array(labels))

# almacenando modelo

face_mask.write("face_mask_model.xml")
print("Modelo almacenado")
