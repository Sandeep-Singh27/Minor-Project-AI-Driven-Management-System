from getTimings import getTimings
import cv2

def setSequence(l:list):
    indexed_l = list(enumerate(l)) 
    sorted_pairs = sorted(indexed_l, key=lambda x: x[1], reverse=True) 
    ranks = [0] * len(l)
    for rank, (idx, _) in enumerate(sorted_pairs, start=1):
        ranks[idx] = rank
    d = {ranks[i]: l[i] for i in range(len(l))}
    return d

if __name__ == "__main__":
    cycle_time = int(input("Enter the cycle time : "))
    cap1 = cv2.VideoCapture("./Looped Videos/Looped video_1.mp4")
    cap2 = cv2.VideoCapture("./Looped Videos/Looped video_2.mp4")
    cap3 = cv2.VideoCapture("./Looped Videos/Looped video_3.mp4")
    cap4 = cv2.VideoCapture("./Looped Videos/Looped video_4.mp4")
    sequence = setSequence(getTimings(cycle_time,cap1,cap2,cap3,cap4))
    #sequence = setSequence([23,90,89,50])
    print(f"sequence:{sequence}")
    