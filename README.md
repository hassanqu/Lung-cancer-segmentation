
# 🧠 Lung Cancer Segmentation with YOLOv8

This project demonstrates lung cancer segmentation using a custom-trained YOLOv8 model. It uses the Ultralytics YOLOv8 segmentation framework to detect and visualize cancer regions in medical images.

---

## 📌 Features

- ✅ Custom YOLOv8 segmentation model (`best.pt`)
- ✅ Visualizes masks, bounding boxes, and class labels
- ✅ Saves output results to an `out/` directory
- ✅ Easy-to-run Python script for inference

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/furzamharis/lungcancer-seg.git
cd lungcancer-seg
````

### 2. Install Dependencies

Make sure you have Python ≥3.8 and then run:

```bash
pip install -r requirements.txt
```

### 3. Run Inference

```bash
python predict_and_save.py
```

This will:

* Load your custom model from `runs/segment/train2/weights/best.pt`
* Predict on a test image
* Display the segmented result
* Save the output to the `out/` folder

---

## 🖼 Sample Output

The output will look like this (with masks and labels drawn):

```
out/
└── segmented_seq1_valid_images_18.jpg
```

---

## 📁 Project Structure

```
lungcancer-seg/
├── datasets/                         # Test images
├── runs/segment/train2/weights/     # Custom model weights (best.pt)
├── out/                             # Output folder for results
├── predict_and_save.py              # Inference and visualization script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## ⚙️ Requirements

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* OpenCV
* matplotlib
* PyTorch

Install all with:

```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is intended for educational and research purposes only.

---

## 🙋‍♂️ Questions?

Feel free to open an issue or contact the maintainer.

```
