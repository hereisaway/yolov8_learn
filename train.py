from ultralytics import YOLO

if __name__ == '__main__':
    # 加载预训练模型
    model = YOLO('yolov8n.pt')

    model.train(data='train_cfg.yaml',epochs=100)

    model.val()