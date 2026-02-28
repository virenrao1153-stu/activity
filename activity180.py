import cv2

image = cv2.imread("input.jpg")
output = image.copy()

h, w = image.shape[:2]

start_point = (0, h // 2)
end_point = (w, h // 2)

cv2.arrowedLine(output, start_point, end_point, (0, 0, 255), 3, tipLength=0.05)
cv2.arrowedLine(output, end_point, start_point, (0, 0, 255), 3, tipLength=0.05)

text = f"Width: {w} pixels"
cv2.putText(output, text, (w // 4, (h // 2) - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Annotated Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()