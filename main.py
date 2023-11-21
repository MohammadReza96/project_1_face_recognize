# from matplotlib import pyplot as plt
# import cv2
# from error_handling import face_not_recognize_error,image_not_exist_error,model_not_recognize_error

# try:
#   #------------------------ import picture file
#   image=cv2.imread('images/my_image.jpeg')    #----- with human face     (test)
#   # image=cv2.imread('images/image_1.png')    #----- without human face  (test)

#   #---- image handel error
#   if  image is None:
#     raise image_not_exist_error.PhotoNotExist('image is not found')

#   #------------------------ conver BGR image to RGB
#   image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#   #------------------------ import model.xml file
#   model=cv2.CascadeClassifier('model/model.xml')

#   #---- model handel error
#   if model.empty():
#     raise model_not_recognize_error.ModelNotExist('model is not existed')

#   #------------------------ finding face in image
#   face=model.detectMultiScale(image)

#   #---- face handel error
#   if len(face)==0:
#     raise face_not_recognize_error.FaceNotRecognize('Face is not found')

#   #------------------------ find image location in picture
#   image_loc_x=face[0][0]
#   image_loc_y=face[0][1]
#   image_loc_a=face[0][2]
#   image_loc_b=face[0][3]

#   #------------------------ create a border around image which is found
#   image=cv2.rectangle(image,(image_loc_x,image_loc_y),(image_loc_x+image_loc_a,image_loc_y+image_loc_b),(255,0,0),3)

#   #------------------------ show image with the border around the detected face
#   plt.imshow(image)
#   plt.show()

# except Exception as error:
#   print(error)


# import os
# from matplotlib import pyplot as plt
# import cv2
# from error_handling import face_not_recognize_error, image_not_exist_error, model_not_recognize_error

# try:
#     # ------------------------ import picture file
#     image_path = os.path.join('images', 'my_image.jpeg')  # ----- with human face     (test)
#     # image_path = os.path.join('images', 'image_1.png')  # ----- without human face  (test)

#     # ---- image handle error
#     with open(image_path, 'rb') as image_file:
#         image = cv2.imread(image_file.name)

#     if image is None:
#         raise image_not_exist_error.PhotoNotExist('Image is not found')

#     # ------------------------ convert BGR image to RGB
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # ------------------------ import model.xml file
#     model_path = os.path.join('model', 'model.xml')

#     with open(model_path, 'rb') as model_file:
#         model = cv2.CascadeClassifier(model_file.name)

#     if model.empty():
#         raise model_not_recognize_error.ModelNotExist('Model does not exist')

#     # ------------------------ finding face in image
#     face = model.detectMultiScale(image)

#     # ---- face handle error
#     if len(face) == 0:
#         raise face_not_recognize_error.FaceNotRecognize('Face is not found')

#     # ------------------------ find image location in picture
#     face_x, face_y, face_width, face_height = face[0]

#     # ------------------------ create a border around image which is found
#     image = cv2.rectangle(image, (face_x, face_y), (face_x + face_width, face_y + face_height), (255, 0, 0), 3)

#     # ------------------------ show image with the border around the detected face
#     plt.imshow(image)
#     plt.show()

# except Exception as error:
#     print(error)


import cv2
from matplotlib import pyplot as plt
from error_handling import face_not_recognize_error, image_not_exist_error, model_not_recognize_error

# Import picture file
try:
    with open('images/my_image.jpeg', 'rb') as image_file:
        image = cv2.imread(image_file.name)

    # Image handle error
    if image is None:
        raise image_not_exist_error.PhotoNotExist('Image is not found')

    # Convert BGR image to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Import model.xml file
    model = cv2.CascadeClassifier('model/model.xml')

    # Model handle error
    if model.empty():
        raise model_not_recognize_error.ModelNotExist('Model is not existed')

    # Finding face in image
    faces = model.detectMultiScale(image)

    # Face handle error
    if len(faces) == 0:
        raise face_not_recognize_error.FaceNotRecognize('Face is not found')

    # Find image location in picture
    x, y, a, b = faces[0]

    # Create a border around the detected face
    image = cv2.rectangle(image, (x, y), (x + a, y + b), (255, 0, 0), 3)

    # Show image with the border around the detected face
    plt.imshow(image)
    plt.show()

except Exception as error:
    print(error)
