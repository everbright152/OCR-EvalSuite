import cv2


def preprocess_image(image_path: str, output_path: str):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite(output_path, thresh)
    return output_path
    