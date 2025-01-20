from ultralytics import YOLO
import cv2
import os

# Importar el modelo YOLO
model = YOLO("yolov8n.pt")

# Leer video
cap = cv2.VideoCapture('turnstile2.mp4')

# Crear una carpeta para guardar cuadros procesados
output_folder = "processed_frames"
os.makedirs(output_folder, exist_ok=True)

frame_count = 0

# Procesar cada cuadro del video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar objetos en el cuadro
    results = model(frame)

    # Anotar los resultados sobre el cuadro
    annotated_frame = results[0].plot()

    # Guardar el cuadro procesado como imagen
    output_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(output_path, annotated_frame)

    frame_count += 1

cap.release()
model.save('folder/my_model_trained.pt')
