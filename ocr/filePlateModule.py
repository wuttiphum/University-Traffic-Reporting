from roboflow import Roboflow
import supervision as sv
import cv2
import easyocr
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image

# from ocr import findCharacter, ocr

# plateImage = "./pictures/22.jpg"


# API ของRoboflow
def findPlate(plateImage):
    rf = Roboflow(api_key="r5JX8pp1cgBecs7Gf2sD") #เรียกใช้ API
    project = rf.workspace().project("lpr-fuskc") #โปรเจคที่เรียกใช้
    model = project.version(20).model
    result = model.predict(plateImage, confidence=40, overlap=30).json() #ส่ง plateImage ไปให้APIประมวน เเล้วส่งกลับมาเป็นไฟล์json

    # labels = [item["class"] for item in result["predictions"]]

    # detections = sv.Detections.from_roboflow(result)

    # label_annotator = sv.LabelAnnotator()
    # bounding_box_annotator = sv.BoxAnnotator()

    image = cv2.imread(plateImage)

    # # cv2.imshow("test",image)
    # annotated_image = bounding_box_annotator.annotate(
    #     scene=image, detections=detections)
    # annotated_image = label_annotator.annotate(
    #     scene=annotated_image, detections=detections, labels=labels)

    # sv.plot_image(image=image, size=(16, 16))

    # print((result["predictions"][0]))

    x = (result["predictions"][0]['x'])
    y = (result["predictions"][0]['y'])
    w = (result["predictions"][0]['width'])
    h = (result["predictions"][0]['height'])
    return image,x,y,w,h
# sv.plot_image(image=annotated_image, size=(16, 16))



def findNumber(cropped_plate):
    reader = easyocr.Reader(['en','th'],gpu=True)  
    result_text = reader.readtext(cropped_plate,detail=0)
    return result_text

def crop_plate(image,x,y,w,h):
    # image , x , y , w , h = findPlate(filePath)



#display the image
# plt.imshow(image)

#add rectangle
# plt.gca().add_patch(Rectangle((x-w/2,y-h/2),w,h,
#                     edgecolor='red',
#                     facecolor='none',
#                     lw=1))
# print(image)
    cropped_plate = image[int(y - h / 2):int(y + h / 2), int(x - w / 2):int(x + w / 2)]
    # plt.imshow(cropped_plate)
    # plt.show()
    return cropped_plate



# print(result_text)

# gray_image = cv2.cvtColor(cropped_plate,cv2.COLOR_BGR2GRAY)
# ret, thresh4 = cv2.threshold(gray_image, 20, 255, cv2.THRESH_TOZERO)
# ret, thresh4 = cv2.threshold(cropped_plate, 0, 255, cv2.THRESH_BINARY)

# plt.imshow(cropped_plate)
# plt.show()