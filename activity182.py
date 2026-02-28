import cv2
import numpy as np

cap = cv2.VideoCapture(0)

r_val = 1.0
g_val = 1.0
b_val = 1.0

print("Controls:")
print("R/r -> Increase/Decrease Red")
print("G/g -> Increase/Decrease Green")
print("B/b -> Increase/Decrease Blue")
print("S -> Save Image")
print("ESC -> Exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    b, g, r = cv2.split(frame)

    r = cv2.multiply(r, r_val)
    g = cv2.multiply(g, g_val)
    b = cv2.multiply(b, b_val)

    merged = cv2.merge([b, g, r])
    merged = np.clip(merged, 0, 255).astype(np.uint8)

    cv2.imshow("Real-Time Color Filter", merged)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('R'):
        r_val += 0.1
    elif key == ord('r'):
        r_val = max(0, r_val - 0.1)

    elif key == ord('G'):
        g_val += 0.1
    elif key == ord('g'):
        g_val = max(0, g_val - 0.1)

    elif key == ord('B'):
        b_val += 0.1
    elif key == ord('b'):
        b_val = max(0, b_val - 0.1)

    elif key == ord('s') or key == ord('S'):
        filename = input("Enter filename to save (with .jpg): ")
        cv2.imwrite(filename, merged)
        print("Image Saved!")

    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()