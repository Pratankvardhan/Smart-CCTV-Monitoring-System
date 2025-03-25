import cv2
import pygame


pygame.mixer.init()
# pygame.display.set_caption('')
alarm_sound = pygame.mixer.Sound("alarm.mp3")

def noise():
    cap = cv2.VideoCapture(0)
    alarm_playing = False

    while True:
        _, frame1 = cap.read()
        _, frame2 = cap.read()

        diff = cv2.absdiff(frame2, frame1)
        diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        diff = cv2.blur(diff, (5, 5))
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

        contr, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contr) > 0:
            max_cnt = max(contr, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_cnt)
            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame1, "MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            
            # If alarm is not playing, start playing it
            if not alarm_playing:
                alarm_sound.play()
                alarm_playing = True
        else:
            cv2.putText(frame1, "NO-MOTION", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        
        # If alarm is playing and has finished playing, stop it
        if alarm_playing and not pygame.mixer.get_busy():
            alarm_playing = False

        cv2.imshow("esc. to exit", frame1)

        if cv2.waitKey(1) == 27:
            cap.release()
            alarm_sound.stop()
            cv2.destroyAllWindows()
            break
