import cv2
import imutils
# #đọc ảnh nguyên bản
# image_org = cv2.imread("img_2.png")
# cv2.imshow("Anh nguyen ban ",image_org)
#
# # HÀM CONVERT HỆ MÀU
# # image_cvt =cv2.cvtColor(image_org,cv2.COLOR_BGR2HSV)
# # cv2.imshow("Anh đổi hệ màu ",image_cvt)
# #
# # image_cvt1 =cv2.cvtColor(image_org,cv2.COLOR_BGR2LUV)
# # cv2.imshow("Anh đổi hệ màu 1 ",image_cvt1)
#
# #đọc ảnh xám
# image = cv2.imread("img_2.png",cv2.IMREAD_GRAYSCALE)
#
# #Hàm resize
# # image_rs=cv2.resize(image,dsize=(100,200))
# image_rs=cv2.resize(image,dsize=None,fx=2,fy=1)
#
# # #lưu ảnh
# # cv2.imwrite("anh_xam.png",image)
#
# #Hàm xoay ảnh
# image_rotate= imutils.rotate(image,70)
#
# # show ảnh
# cv2.imshow("Anh",image)
# cv2.imshow("Anh rs",image_rotate)
# cv2.waitKey()
# cv2.destroyAllWindows()




#Khai báo camera ID ,or nếu video thì dẫn link video cùng thư mục với main
camera_id = 0
# Mở camera
cap = cv2.VideoCapture(camera_id )
 # Đọc ảnh từ camera
while True :
    #Đọc ảnh
    ret ,frame =cap.read()
    # Đọc ảnh xám
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV )
    #Hiện ảnh
    cv2.imshow('Camera ',gray)
    #Kiểm tra nếu bấm Q thì thoát
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
#GIẢI PHÓNG CAMERA
cap.release()
cv2.destroyAllWindows()



