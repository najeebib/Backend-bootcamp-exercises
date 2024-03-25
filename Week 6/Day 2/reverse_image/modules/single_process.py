from PIL import Image
import time
def single_process(path):
    img = Image.open(path)

    width, height = img.size

    pix = img.load()

    start_time = time.time()
    # go through each pixel and reverse i
    for y in range(height):
        for x in range(width):
            # reverse the pixel by getting the absolute value of 255 minus the pixel
            r = abs(255 - pix[x,y][0])
            g = abs(255 - pix[x,y][1])
            b = abs(255 - pix[x,y][2])
            # save new pixel
            pix[x,y] = (r, g, b)

    end_time = time.time()
    total = end_time - start_time
    print(f"Image reversing with single thread took {total}")
    # show new image
    img.show()
    img.save('./images/single_process_reversed.jpg')
