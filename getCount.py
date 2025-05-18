import cv2
from model import model

def getCount(model,frame):
    resized_frame = cv2.resize(frame,(640,640))
    results = model(resized_frame)
    result = results[0]
    vehicle_count = len(result.boxes)
    return vehicle_count


if __name__ == "__main__":
    cap = cv2.VideoCapture("./vidsAndImg/traffic_video.mp4")
    _,frame = cap.read()
    count = getCount(model,frame)
    print("Count :",count)