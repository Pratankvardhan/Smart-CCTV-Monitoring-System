import cv2
import os

# Create directories if they don't exist
if not os.path.exists('in'):
    os.makedirs('in')
if not os.path.exists('out'):
    os.makedirs('out')

# Load pre-trained person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Initialize video capture
cap = cv2.VideoCapture(0)  # Change 0 to the appropriate camera index if multiple cameras are available

# Initialize variables for counting
count_in = 0
count_out = 0
in_status = False
out_status = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame for faster processing
    frame = cv2.resize(frame, (640, 480))

    # Detect people in the frame
    (rects, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Draw rectangles around detected people
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Check for movement in/out
    if len(rects) > 0:
        if not in_status:
            count_in += 1
            cv2.imwrite(f'in/person_{count_in}.jpg', frame)
            in_status = True
            out_status = False
    else:
        if not out_status:
            count_out += 1
            cv2.imwrite(f'out/person_{count_out}.jpg', frame)
            out_status = True
            in_status = False

    # Display the frame
    cv2.imshow('Frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
