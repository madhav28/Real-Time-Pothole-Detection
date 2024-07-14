from ultralytics import YOLO
 
model = YOLO('yolov8n.pt')
 
model.train(
   data='./dataset/data.yaml',
   imgsz=1280,
   epochs=50,
   batch=16,
   name='model'
)