import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from scipy.fft import fft2, ifft2, fftshift, ifftshift

def load_image(image_path):
    image = io.imread(image_path)
    
    if image.shape[-1] == 4:  
        image = image[:, :, :3]
    image = image / 255.0  
    
    return image

def fft_reconstruction_color(image, percentage):
    reconstructed_image = np.zeros_like(image)
    for i in range(3):
        channel = image[:, :, i]
        f_transform = fft2(channel)
        f_transform_shifted = fftshift(f_transform)
        
        total_pixels = channel.size
        num_coefficients = int(total_pixels * (percentage / 100.0))
        
        flattened = np.abs(f_transform_shifted).flatten()
        threshold = np.partition(flattened, -num_coefficients)[-num_coefficients]
        
        f_transform_shifted[np.abs(f_transform_shifted) < threshold] = 0
        f_transform_unshifted = ifftshift(f_transform_shifted)
        reconstructed_image[:, :, i] = np.abs(ifft2(f_transform_unshifted))
    
    return reconstructed_image

def pixel_sampling_reconstruction(image, percentage):
    sampled_image = np.zeros_like(image)
    total_pixels = int(image.shape[0] * image.shape[1] * (percentage / 100.0))
    
    for i in range(3): 
        channel = image[:, :, i]
        flattened = channel.flatten()
        sorted_indices = np.argsort(flattened)[::-1]  
        
        sampled_indices = sorted_indices[:total_pixels]
        mask = np.zeros_like(flattened, dtype=bool)
        mask[sampled_indices] = True
        
        sampled_channel = mask.reshape(channel.shape) * channel
        sampled_image[:, :, i] = sampled_channel
    
    return sampled_image

def plot_images_comparison(original, fft_reconstructed, sampled_reconstructed):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    ax = axes.ravel()

    ax[0].imshow(original)
    ax[0].set_title("Original Image")

    ax[1].imshow(np.clip(fft_reconstructed, 0, 1))
    ax[1].set_title("Reconstructed with FFT")

    ax[2].imshow(np.clip(sampled_reconstructed, 0, 1))
    ax[2].set_title("Reconstructed without FFT (Pixel Sampling)")

    for a in ax:
        a.axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    Tk().withdraw()
    image_path = askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    
    if not image_path:
        print("No file selected. Exiting.")
        return
    
    percentage = float(input("Enter the percentage of pixels to retain (0-100): "))
    
    image = load_image(image_path)
    fft_reconstructed = fft_reconstruction_color(image, percentage)
    sampled_reconstructed = pixel_sampling_reconstruction(image, percentage)
    
    plot_images_comparison(image, fft_reconstructed, sampled_reconstructed)

if __name__ == "__main__":
    main()
