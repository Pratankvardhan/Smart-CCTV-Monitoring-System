import cv2
import os
import pickle
import numpy as np
import warnings
from face_recognition_api import face_locations as detect_face_locations, face_encodings as encode_faces

# Load Face Recogniser classifier
fname = 'classifier.pkl'
if os.path.isfile(fname):
    with open(fname, 'rb') as f:
        (le, clf) = pickle.load(f)
else:
    print('\x1b[0;37;43m' + "Classifier '{}' does not exist".format(fname) + '\x1b[0m')
    quit()

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_names = []
process_this_frame = True

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            detected_face_locations = detect_face_locations(small_frame)
            detected_face_encodings = encode_faces(small_frame, detected_face_locations)

            face_names = []
            predictions = []
            if len(detected_face_encodings) > 0:
                closest_distances = clf.kneighbors(detected_face_encodings, n_neighbors=1)
                is_recognized = [closest_distances[0][i][0] <= 0.5 for i in range(len(detected_face_locations))]

                # predict classes and cull classifications that are not with high confidence
                predictions = [(le.inverse_transform(np.array([int(pred)]))[0].title(), loc) if rec else ("Unknown", loc) for pred, loc, rec in
               zip(clf.predict(detected_face_encodings), detected_face_locations, is_recognized)]


        process_this_frame = not process_this_frame

        # Draw the results on the frame
        for name, (top, right, bottom, left) in predictions:
            # Scale up the face locations to match the original frame size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Show the frame with the results
        cv2.imshow('Real-time Face Recognition', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
