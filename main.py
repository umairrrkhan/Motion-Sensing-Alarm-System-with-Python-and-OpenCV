import cv2
import imutils
import threading 
import winsound

# Initialize webcam
cap = cv2.VideoCapture(0)

# Check if camera opened successfully 
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Load first frame
ret, frame = cap.read()
frame = imutils.resize(frame, width=500)

# Convert to grayscale and blur
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (21, 21), 0)

# Previous frame variable
prev_gray = gray

# For threaded alarm  
alarm_on = False

def sound_alarm(alarm_on):
    while alarm_on:
        print("Alarm!")
        winsound.Beep(2500, 1000)
    alarm_on = False

while True:

    # Read current frame
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=500)

    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0) 

    # Compute absolute difference 
    delta = cv2.absdiff(prev_gray, gray)

    # Threshold
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Count white pixels 
    white_pix = cv2.countNonZero(thresh)

    # Check if pixels exceed threshold
    if white_pix > 1000:
        threading.Thread(target=sound_alarm, args=(alarm_on,)).start()
        alarm_on = True

    # Update previous frame
    prev_gray = gray

    # Display outputs
    cv2.imshow("Frame", frame)
    cv2.imshow("Thresh", thresh)

    # Break on q key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# Release resources
cap.release()
cv2.destroyAllWindows()