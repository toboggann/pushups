import cv2
from mediapipe.python.solutions import pose as mp_pose
from mediapipe.python.solutions import drawing_utils as mp_drawing
from mediapipe.python.solutions import drawing_styles as mp_drawing_styles
import time


print("Welcome to Rep Johnson!")
print("=" * 20)
excercise  =  int(input("Please Select an exercise:\n1. Pushups\n2. Squats\n3. Lunge\n4. Plank\n5. Exit\nAnswer: "))
#print(excercise)

if excercise == 5:
    raise SystemExit

print("Loading Camera: ", end="", flush=False)
for _ in range(10):
    time.sleep(0.2)
    print("█", end="", flush=True)
print(" done!")


count = 0
Position = False
First = True

def Pushups():
    global count, Position, body_list 

    if len(body_list) <= 14:
        return

    # up position (shoulders above elbows) and we were previously down
    if (body_list[12][2] < body_list[14][2] and body_list[11][2] < body_list[13][2]) and Position == True:
        count += 1
        Position = False
        if count == 1:
            print(f"{count} Pushup done!")
        else:
            print(f"{count} Pushups done!")

    # down position (shoulders below elbows) and we were previously up
    if (body_list[12][2] > body_list[14][2] and body_list[11][2] > body_list[13][2]) and Position == False:
        Position = True

def Squat():
    global count, Position, body_list 
    print("Squat")
    pass


def Lunge():
    global count, Position, body_list 
    print("Lunge")
    pass



def Plank():
    global count, Position, body_list 
    print("Plank")
    pass


cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error: problem with webcam")
    exit()


with mp_pose.Pose(
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6) as pose:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("black camera")
      continue
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    body_list = []
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        for id, i in enumerate(results.pose_landmarks.landmark):
            h,w,_ = image.shape
            X,Y = int(i.x*w), int(i.y*h)
            body_list.append([id,X,Y])

        #11 is left shoulder
        #12 is right shoulder
        #print(body_list[12][1], body_list[12][2])
        #print(body_list[11][1], body_list[11][2])
        if excercise == 1:
            if count == 0 and First:
                print("Pushups started! (Press Esc to quit)")
                First = False
            Pushups()
        elif excercise == 2 :
            if count == 0 and First:
                print("Squats started! (Press Esc to quit)")
                First = False
            Squat()
        elif excercise == 3:
            if count == 0 and First:
                print("Lunges started! (Press Esc to quit)")
                First = False
            Lunge()
        elif excercise == 4:
            if count == 0 and First:
                print("Plank started! (Press Esc to quit)")
                First = False
            Plank()


    cv2.imshow('Rep Johnson', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break


       
cap.release()