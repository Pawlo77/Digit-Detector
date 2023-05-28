# Simple Digit Classifier

## How it Works
This project provides a simple paint app that allows you to draw digits and receive predictions on the drawn digit. Here's how it works:

1. You draw a digit on the canvas.
2. Press the "Scan" button.
3. The program scans the canvas and crops the smallest possible rectangle that contains the entire drawing.
4. The cropped rectangle is resized to 28x28 pixels.
5. The resized image is fed into a trained Neural Network model.
6. The model predicts the digit based on the input image.
7. The predicted digit is displayed in a pop-up window.

## Paint App
The paint app allows you to:
- Draw digits on a canvas
- Reset the canvas
- Erase drawings
- Change brush colors

Once you press the "Scan" button, a pop-up window will display the model's prediction for the drawn digit.

## Requirements
To obtain accurate predictions, please ensure the following conditions are met:
- The drawn digit should be the only object on the board.
- The smaller the digit, the thicker its 28x28 version will be, resulting in more accurate predictions.

## Performance Enhancement
You can improve the app's performance by adjusting the `paint_size` parameter in the `settings.py` file.

---

Regarding the trained models:

## Model Selection
Several models were tested, but the default used model (Model 1) outperformed the others, demonstrating good generalization on a small 100-sample test dataset.

## Model Descriptions
- `final_model2`: A Sequential Neural Network trained in TensorFlow (Keras) with around 700k parameters. It was trained on the normal MNIST dataset for 11 epochs.
- `final_model1`: A Sequential Neural Network trained in TensorFlow (Keras) with around 2,700k parameters. It was trained on the normal MNIST dataset for 18 epochs.
- `final_model2`: A Sequential Neural Network trained in TensorFlow (Keras) with around 700k parameters. It was trained on the normal MNIST dataset.
- `final_model1`: A Sequential Neural Network trained in TensorFlow (Keras) with around 2,700k parameters. It was trained on the normal MNIST dataset for 22 epochs.
- `final_model1`: A Sequential Neural Network trained in TensorFlow (Keras) with around 2,700k parameters. It was trained on the normal MNIST dataset for 12 epochs.

Models 2-4 differ slightly, but all of them are deeper than the first model. However, the first model performs better in terms of both performance and accuracy, making it the recommended choice.

---

Technical Details:

- Training Data: All five models were trained on datasets similar to MNIST, such as MNIST Extended. However, the original MNIST dataset yielded the best performance.

This project offers a practical learning experience for implementing machine learning algorithms and provides various functionalities for data preprocessing, model building, and evaluation.

---

**Note**: For more detailed information and instructions on using the project, please refer to the project's documentation.
