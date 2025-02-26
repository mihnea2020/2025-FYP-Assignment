class Main:
    #Libraries
    import cv2
    import matplotlib.pyplot as plt 
    import matplotlib.image as mpimg
    import numpy as np
    from PIL import Image 

    #Import image directly on gray scale
    image = cv2.imread('img_1441.png', cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    kernel = np.ones((3,3), np.uint8)

    # Apply Morphological Operations
    closed = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)  # Fills small holes
    opened = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)  # Removes small noise

    # Display Results
    plt.figure(figsize=(10,5))
    plt.subplot(2,3,1), plt.imshow(image, cmap='gray'), plt.title("Original"), plt.axis("off")
    plt.subplot(2,3,3), plt.imshow(opened, cmap='gray'), plt.title("Threshold"), plt.axis("off")
    

    plt.show()
