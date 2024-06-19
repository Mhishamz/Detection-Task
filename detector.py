from ultralytics import YOLO

model = YOLO("yolov9s.pt")

def Predict(image):
    results = model(image)
    my_categories=[]
    for box in results[0].boxes:
      class_id = results[0].names[box.cls[0].item()]
      print("Object type:", class_id)
      my_categories.append(class_id)
    return my_categories