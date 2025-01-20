from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

videos_path = [
        r"C:\Users\duvan\Desktop\Git\py_object_detection_v2\turnstile1.mp4",
        r"C:\Users\duvan\Desktop\Git\py_object_detection_v2\turnstile2.mp4"
    ]

for video in videos_path:

    cap = cv2.VideoCapture(video)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        
        annotated_frame = results[0].plot()

        cv2.imshow('Detecciones', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()