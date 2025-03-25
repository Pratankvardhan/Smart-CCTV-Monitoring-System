import cv2
# import time
from skimage.metrics import structural_similarity
from datetime import datetime
import winsound
import os

def spot_diff(frame1, frame2):
    frame1 = frame1[1]
    frame2 = frame2[1]

    g1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    g2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    g1 = cv2.blur(g1, (2, 2))
    g2 = cv2.blur(g2, (2, 2))

    (score, diff) = structural_similarity(g2, g1, full=True)

    print("Image similarity", score)

    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY_INV)[1]

    contors = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contors = [c for c in contors if cv2.contourArea(c) > 50]

    if len(contors):
        print("Stolen")
        for c in contors:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    else:
        print("Nothing stolen")
        return 0

    cv2.imshow("diff", thresh)
    cv2.imshow("win1", frame1)
    winsound.Beep(1000, 500)  # Beep sound

    try:
        # Create stolen folder if it doesn't exist
        if not os.path.exists('database/stolen'):
            os.makedirs('database/stolen')
        
        file_name = os.path.join('database','stolen', f"{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg")
        cv2.imwrite(file_name, frame1)
        print("Image saved as:", file_name)
    except Exception as e:
        print("Error saving image:", e)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 1
