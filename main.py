from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2
import os

# Load your custom segmentation model
model = YOLO("lungcancer-seg/runs/segment/train2/weights/best.pt")

# Input image path
image_path = "lungcancer-seg/datasets/Lung_Cancer_NormAug_Validation-4/test/images/seq1_valid_images_18_jpg.rf.3695ef168f67c0170c915c28ef2d03f8.jpg"

# Output directory
output_dir = "out"
os.makedirs(output_dir, exist_ok=True)

# Run prediction
results = model(image_path)

# Process results
for i, result in enumerate(results):
    if result.masks is not None:
        # Visualized result with masks, boxes, labels
        img = result.plot()

        # Display image using matplotlib
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(10, 10))
        plt.imshow(img_rgb)
        plt.axis("off")
        plt.title("YOLOv8 Segmentation Result")
        plt.show()

        # Save to output folder
        filename = os.path.basename(image_path)
        save_path = os.path.join(output_dir, f"segmented_{filename}")
        cv2.imwrite(save_path, img)
        print(f"Result saved to: {save_path}")
    else:
        print("No masks detected.")
