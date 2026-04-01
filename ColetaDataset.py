import cv2
import os

VIDEO_PATH = "H:\\VideosTeste\\video_teste.mp4"
OUTPUT_DIR = "H:\\Dev\\OlhaBuraco\\dataset_novo\\images\\train"
INTERVALO = 10  #coleta 1 imagem a cada 10 frames

os.makedirs(OUTPUT_DIR, exist_ok=True)

cap = cv2.VideoCapture(VIDEO_PATH)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Total de frames: {total_frames} | FPS: {fps}")

frame_num = 0
salvo = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_num % INTERVALO == 0:
        nome = os.path.join(OUTPUT_DIR, f"frame_{frame_num:05d}.jpg")
        cv2.imwrite(nome, frame)
        salvo += 1
        print(f"Salvo: {nome}")

    frame_num += 1

cap.release()
print(f"\n Total de frames extraídos: {salvo}")