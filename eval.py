from ultralytics import YOLO

# 加载预训练模型
model=YOLO('yolov8n.yaml')
model = YOLO('yolov8n.pt')

model.predict('test_data/hardhat.mp4',save=True)