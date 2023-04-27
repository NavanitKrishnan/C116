import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "Sun",
            (40,300),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (90,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Venus",
            (160,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Earth",
            (250,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mars",
            (350,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Jupiter",
            (450,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Saturn",
            (750,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Uranus",
            (900,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Neptune",
            (1100,200),
            cv2.FONT_ITALIC,
            0.5,
            (255,255,255)
)


print(img)

cv2.imshow("Solar System",img)

cv2.waitKey(0)

