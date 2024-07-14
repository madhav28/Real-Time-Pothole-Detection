from ultralytics import YOLO
 
model = YOLO("model.pt")
 
model.predict(source="test1.jpg", save=True)