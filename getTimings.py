from getCount import getCount
from model import model
import cv2

def getTimings(cycle_time: int, cap1, cap2, cap3, cap4, time_stamp=0):
    # Check if all captures are opened
    if not (cap1.isOpened() and cap2.isOpened() and cap3.isOpened() and cap4.isOpened()):
        return None
    
    # Get FPS for each video
    fps1 = cap1.get(cv2.CAP_PROP_FPS)
    fps2 = cap2.get(cv2.CAP_PROP_FPS)
    fps3 = cap3.get(cv2.CAP_PROP_FPS)
    fps4 = cap4.get(cv2.CAP_PROP_FPS)
    
    # Calculate frame indices based on timestamp
    frame_index1 = int(time_stamp * fps1)
    frame_index2 = int(time_stamp * fps2)
    frame_index3 = int(time_stamp * fps3)
    frame_index4 = int(time_stamp * fps4)
    
    # Get total frame counts to check if we've reached the end
    total_frames1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames3 = int(cap3.get(cv2.CAP_PROP_FRAME_COUNT))
    total_frames4 = int(cap4.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Check if we've reached the end of any video, if so, loop back to beginning
    if frame_index1 >= total_frames1:
        frame_index1 = frame_index1 % total_frames1
    if frame_index2 >= total_frames2:
        frame_index2 = frame_index2 % total_frames2
    if frame_index3 >= total_frames3:
        frame_index3 = frame_index3 % total_frames3
    if frame_index4 >= total_frames4:
        frame_index4 = frame_index4 % total_frames4

    # Set frame positions
    cap1.set(cv2.CAP_PROP_POS_FRAMES, frame_index1)
    cap2.set(cv2.CAP_PROP_POS_FRAMES, frame_index2)
    cap3.set(cv2.CAP_PROP_POS_FRAMES, frame_index3)
    cap4.set(cv2.CAP_PROP_POS_FRAMES, frame_index4)

    # Read frames
    frame1_captured, frame1 = cap1.read()
    frame2_captured, frame2 = cap2.read()
    frame3_captured, frame3 = cap3.read()
    frame4_captured, frame4 = cap4.read()

    if frame1_captured and frame2_captured and frame3_captured and frame4_captured:
        # Get vehicle counts
        count1 = getCount(model, frame1)
        count2 = getCount(model, frame2)
        count3 = getCount(model, frame3)
        count4 = getCount(model, frame4)

        countSum = count1 + count2 + count3 + count4
        
        # Avoid division by zero
        if countSum == 0:
            # If no vehicles detected, give equal time to all signals
            green_time1 = green_time2 = green_time3 = green_time4 = cycle_time / 4
        else:
            green_time1 = (count1 / countSum) * cycle_time
            green_time2 = (count2 / countSum) * cycle_time
            green_time3 = (count3 / countSum) * cycle_time  
            green_time4 = (count4 / countSum) * cycle_time

        return [green_time1, green_time2, green_time3, green_time4]
    
    return None


if __name__ == "__main__":
    cycle_time = int(input("Enter the cycle time : "))
    cap1 = cv2.VideoCapture("./vidsAndImg/traffic_video.mp4")
    cap2 = cv2.VideoCapture("./vidsAndImg/traffic_video2.mp4")
    cap3 = cv2.VideoCapture("./vidsAndImg/traffic_video3.mp4")
    cap4 = cv2.VideoCapture("./vidsAndImg/traffic_video4.mp4")

    timings = getTimings(cycle_time, cap1, cap2, cap3, cap4)
    print(timings)