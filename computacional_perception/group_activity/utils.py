import cv2 as cv
import matplotlib.pyplot as plt

def show_images_side_by_side(image1, image2, title1 = "Image 01", title2 = "Image 02", size = 10):

    plt.figure(figsize=(2 * size, size))

    # First image: (row, col, file)
    plt.subplot(1, 2, 1)
    if len(image1.shape) == 3 and image1.shape[2] == 3:
        plt.imshow(cv.cvtColor(image1, cv.COLOR_BGR2RGB))
    else:
        plt.imshow(image1, cmap='gray')
    plt.title(title1)
    plt.axis('off')

    plt.subplot(1, 2, 2)  #
    if len(image2.shape) == 3 and image2.shape[2] == 3:
        plt.imshow(cv.cvtColor(image2, cv.COLOR_BGR2RGB))
    else:
        plt.imshow(image2, cmap='gray')

    plt.title(title2)
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    pass


def show_single_image(image, title='Img', size=10):

    plt.figure(figsize=(size, size))

    if len(image.shape) == 3 and image.shape[2] == 3:
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    else:
        # Show in grayscale
        plt.imshow(image, cmap='gray')

    plt.title(title)
    plt.axis('off')
    plt.show()
    pass


def plot_histograms_side_by_side(histogram1, histogram2, title1, title2, color_mode = 'grayscale'):
    fig, axes = plt.subplots(1, 2, figsize=(16, 4))

    # First histogram
    ax1 = axes[0]

    if color_mode == 'color':
        for col, hist in histogram1.items():
            ax1.plot(hist, label=f'Canal {col.upper()}')
        ax1.legend()
    else:
        ax1.plot(histogram1['gray'], color='black')

    ax1.set_title(title1)
    ax1.set_xlabel('Intensidad')
    ax1.set_ylabel('Número de Píxeles')
    ax1.grid()

    # Second histogram
    ax2 = axes[1]

    if color_mode == 'color':
        for col, hist in histogram2.items():
            ax2.plot(hist, label=f'Canal {col.upper()}')
        ax2.legend()
    else:
        ax2.plot(histogram2['gray'], color='black')

    ax2.set_title(title2)
    ax2.set_xlabel('Intensidad')
    ax2.set_ylabel('Número de Píxeles')
    ax2.grid()

    plt.tight_layout()
    plt.show()