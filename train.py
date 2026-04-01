from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8s.pt")

    results = model.train(
        data="H:/Dev/OlhaBuraco/data.yaml",
        epochs=150,
        imgsz=640,
        batch=8,        
        patience=30,    
        name="olha_buraco",
        device=0,       
    )
