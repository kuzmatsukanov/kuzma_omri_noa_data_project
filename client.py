import requests
import cv2


if __name__ == '__main__':
    user_image_path = 'samples/sample_dress.jpg'
    user_image = cv2.imread(user_image_path)
    response = requests.get("http://127.0.0.1:5000/get_recommendation?", params={'user_image': user_image})
    # TODO to parse the response
