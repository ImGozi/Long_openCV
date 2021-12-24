import cv2
import imutils
#đọc ảnh nguyên bản
image_org = cv2.imread("img_2.png")


#Hàm Threshold đưa ảnh về dạng nhị phân 0 hoặc 255
image= cv2.imread("img_2.png",cv2.IMREAD_GRAYSCALE)
#Áp threshold
cv2.threshold(image,180,255,cv2.THRESH_BINARY)
cv2.imshow("Anh đã áp  ",image)
cv2.imshow("Anh nguyen ban ",image_org)
cv2.waitKey()
cv2.destroyAllWindows()
