import imageio
import numpy as np
import matplotlib.pyplot as plt


def rgb_to_grayscale(image):
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]) 

image_path = 'C:\Users\ACER\OneDrive\Pictures\Documents\USB Drive\UTS PBP\UTS PBP\tugas telat\sesi 3\cv voli.jpeg' 
image_rgb = imageio.imread(image_path)

image_gray = rgb_to_grayscale(image_rgb)

histogram, bin_edges = np.histogram(image_gray, bins=256, range=(0, 255))

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.imshow(image_gray, cmap='gray')
plt.title('Gambar Grayscale')
plt.axis('off')

plt.subplot(2, 1, 2)
plt.plot(bin_edges[0:-1], histogram)
plt.title('Histogram Grayscale')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

plt.savefig('histogram_grayscale.png')

plt.show()

total_pixels_per_intensity = histogram
dominant_intensity = np.argmax(histogram)

print(f"Jumlah total piksel untuk setiap intensitas: {total_pixels_per_intensity}")
print(f"Intensitas yang paling dominan: {dominant_intensity} dengan jumlah piksel {histogram[dominant_intensity]}")