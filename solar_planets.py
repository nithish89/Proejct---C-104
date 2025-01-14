import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1.0,
            (500, 500, 500)
            )

cv2.putText(img,
            "Mercury",
            (120,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255, 255, 255)
            )

cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Earth",
            (288,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Mars",
            (385,255),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Jupiter",
            (580,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Saturn",
            (760,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Uranus",
            (965,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Neptune",
            (1110,290),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)