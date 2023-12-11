# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# def max_pooling(image, pool_size):
#     # Apply max pooling to the image
#     result = cv2.resize(image, (0, 0), fx=1/pool_size, fy=1/pool_size, interpolation=cv2.INTER_MAX)
#     return result
#
# # Load your image
# image_path = '/home/mefathim-tech-49/Downloads/download.jpeg'  # Replace with the path to your image
# original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#
# # Define the pool size (e.g., 2 for 2x2 max pooling)
# pool_size = 2
#
# # Apply max pooling
# pooled_image = max_pooling(original_image, pool_size)
#
# # Plot the original and pooled images side by side
# plt.figure(figsize=(8, 4))
#
# plt.subplot(1, 2, 1)
# plt.title('Original Image')
# plt.imshow(original_image, cmap='gray')
# plt.axis('off')
#
# plt.subplot(1, 2, 2)
# plt.title('Max Pooled Image')
# plt.imshow(pooled_image, cmap='gray')
# plt.axis('off')
#
# plt.show()


