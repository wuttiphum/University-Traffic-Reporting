import cv2
import pytesseract
from PIL import Image
import os
import numpy as np
def test():
    print("test")

# print(os.system('dir'))
def ocr (file_path):
    # โหลดภาพ
    image = cv2.imread(file_path)
    # os.remove(file_path)
    # image = cv2.imread('C:\\Users\\wutwa\\OneDrive\\Desktop\\Project\\Myproject\\ocr\\plate.png')

    # ครอบตัดส่วนของป้ายทะเบียน (crop)
    # คุณต้องระบุขนาดของส่วนที่คุณต้องการ crop (ความกว้างและความสูง)

    x, y, width, height = 100, 200, 300, 100  # ตัวอย่างขนาดเริ่มต้น 

    # # Crop ภาพ
    # cropped_image = image[y:y+height, x:x+width]
    # แปลงภาพเป็นขาวดำ (Grayscale)
    #  Grayscale the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    enhanced_image = cv2.equalizeHist(gray)
    # cv2.imshow('Gray', gray)

    # Apply filter and find edges
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)
    # cv2.imshow('Edged', edged)

    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Find number plate
    roi = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.015 * perimeter, True)
        if len(approx) == 4:
            roi = approx
            break

    roi = np.array([roi], np.int32)
    points = roi.reshape(4, 2)
    x, y = np.split(points, [-1], axis=1)

    (x1, x2) = (np.min(x), np.max(x))
    (y1, y2) = (np.min(y), np.max(y))

    number_plate = image[y1:y2, x1:x2]

    # cv2.imshow('Number plate', number_plate)



    # ทำ OCR บนป้ายทะเบียน
    license_plate_text = pytesseract.image_to_string(enhanced_image,lang="tha")

    # # แสดงข้อความที่ได้จาก OCR
    print("License Plate:", license_plate_text)

    
    # แสดงภาพป้ายทะเบียน
    # cv2.namedWindow('License Plate',cv2.WINDOW_NORMAL)
    # cv2.imshow('License Plate', image)
    # cv2.namedWindow('Cropped License Plate',cv2.WINDOW_NORMAL)
    # cv2.imshow('Cropped License Plate', number_plate)
    #กำหนดชื่อไฟล์ ที่บันทึกไฟล์
    # ocr/static/ocr/plate_pic/plate.png
    cropped_path = f'{file_path[0:28]}_cropped.png'
    # ocr/static/ocr/plate_pic/pla_cropped.png
    cv2.imwrite(cropped_path,number_plate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # ส่งไปยังหน้าเว็บ
    # /static/ocr/plate_pic/pla_cropped.png'
    return [license_plate_text,cropped_path,file_path]


ocr('ocr/static/ocr/plate_pic/1.png')
