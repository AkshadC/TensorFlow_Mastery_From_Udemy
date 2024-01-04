import os
import random
import  matplotlib.image as  mpimg
import matplotlib.pyplot as plt


def view_random_image(target_dir, target_class):
    target_folder = target_dir + "/" + target_class

    random_image = random.sample(os.listdir(target_folder), 1)

    img = mpimg.imread(target_folder + "/" + random_image[0])

    plt.imshow(img, cmap='viridis', vmin=0, vmax=255)
    plt.title(target_class)
    plt.axis('off')
    print(f"Image shape is : {img.shape}")
    return img
