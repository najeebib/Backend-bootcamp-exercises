from PIL import Image
import concurrent.futures
import time

def process_chunk(path, width, start_y, end_y):
    img = Image.open(path)
    pix = img.load()
    for y in range(start_y, end_y):
        for x in range(width):
            r = abs(255 - pix[x, y][0])
            g = abs(255 - pix[x, y][1])
            b = abs(255 - pix[x, y][2])
            pix[x, y] = (r, g, b)
    return img, start_y, end_y

def multi_process(path):
    img = Image.open(path)
    width, height = img.size

    start_time = time.time()
    # number of processes to use
    # each process will take 1/8th of the image, which is (6000x500) pixels each
    num_of_processes = 8
    # number of height pixels each process will work on (4000/8 = 500)
    pixels_per_process = height // num_of_processes

    # use ProcessPoolExecutor to execute the process_chunk function concurrently
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(num_of_processes):
            # calculate the starting and ending y-coordinate for each process
            start_y = i * pixels_per_process
            end_y = start_y + pixels_per_process
            # submit the process_chunk function to the executor
            futures.append(executor.submit(process_chunk, path, width, start_y, end_y))
        # retrieve the images and start_y, end_y from each process when it finishes
        processed_images = [future.result() for future in concurrent.futures.as_completed(futures)]

    end_time = time.time()
    total = end_time - start_time
    print(f"Image reversing with multiprocessing took {total}")

    # create a new blank image with the same width and height
    final_img = Image.new('RGB', (width, height))

    # loop through each processed image and its start_y end_y values
    for processed_img, start_y, end_y in sorted(processed_images, key=lambda x: x[1]):
        # (0, start_y, width, end_y) this is the coordenations of the box that has the edited part of the image, we want to crop the image to include only this part
        # crop the processed image to include only the edited part
        edited_region = processed_img.crop((0, start_y, width, end_y))
        # paste the edited region on the image
        final_img.paste(edited_region, (0, start_y))

    final_img.show()