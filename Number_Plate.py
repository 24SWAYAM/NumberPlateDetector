import cv2

framewidth, frameheight = 640, 480
NumPlateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
minArea = 200
fcolor = (0, 0, 255)

cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)
cap.set(10, 150)

while True:
    ret, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numPlates = NumPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    
    for x, y, w, h in numPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, fcolor, 2)
            imgf = img[y:y + h, x:x + w]
            cv2.imshow("Scanning", imgf)

    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit the loop
        break

cap.release()
cv2.destroyAllWindows()
