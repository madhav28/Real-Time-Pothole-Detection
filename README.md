# Real-Time-Pothole-Detection
## About
In this real-time pothole detection project, I developed an advanced system using the 'yolov8n.pt' model, trained on a meticulously curated dataset of 6,962 images. The primary objective was to achieve rapid inference speeds, and the model excels by processing video feeds at an impressive rate of approximately 100 frames per second. This high-speed detection capability ensures immediate identification and reporting of potholes, significantly enhancing road safety and maintenance efficiency. By leveraging the robust YOLOv8n architecture, the model strikes an optimal balance between speed and accuracy, making it highly effective for real-time applications. The project aims to reduce accidents and vehicle damage, while enabling more efficient allocation of resources for road repairs, contributing to smarter and safer urban infrastructure.

## Commands
### Create Environment
conda env create -f environment.yml<br>
conda activate venv

### Train Model
python train.py
