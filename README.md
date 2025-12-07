# FFT Image Compression vs Pixel Sampling 🖼️📉

**Comparative analysis:** FFT frequency-domain compression vs direct pixel sampling for RGB images. This project demonstrates why frequency-based compression is superior to spatial brightness sampling.

## 📋 Features
- **FFT Method:** Frequency domain transformation → keep top N% coefficients → reconstruct
- **Pixel Sampling:** Sort pixels by brightness → keep top N% brightest → zero others
- **RGB Processing:** Independent channel processing for full-color support
- **Interactive GUI:** File picker + percentage input (0-100%)

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-0C55A6?style=flat&logo=scipy&logoColor=white)

## 🚀 Quick Start

**1. Install Dependencies**
```bash
pip install numpy matplotlib scikit-image scipy
# Note: tkinter is usually included with Python
```

**2. Run the Analysis**
```bash
python image_compression.py
```

**3. Usage**
1. Select an image from your computer.
2. Enter a compression percentage (e.g., `10` to keep only 10% of data).
3. View the side-by-side comparison.

## 🎯 How It Works



**Method 1: FFT Compression (Frequency Domain)**
`Original Image` → `Fast Fourier Transform` → `Keep Top N% Coefficients` → `Inverse FFT` → `Reconstructed Image`

**Method 2: Pixel Sampling (Spatial Domain)**
`Original Image` → `Sort Pixels` → `Keep Top N% Brightest` → `Zero Out Rest` → `Display Result`

## 📁 Files
```text
├── image_compression.py   # FFT + pixel sampling + visualization
└── requirements.txt       # Dependencies
```

## 🎓 Key Insight
> **FFT reconstruction preserves structural information significantly better than simple pixel sampling.** Even with only 5-10% of coefficients, the FFT method retains the recognizable shape and edges of the image, whereas pixel sampling results in scattered noise.
