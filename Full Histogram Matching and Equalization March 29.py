import tkinter as tk
import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter.filedialog import askopenfilename
from functools import partial
from PIL import Image
import os
from tkinter import filedialog

import winsound

# GUI
window = tk.Tk()
window.title('My Window')
window.geometry('900x470')
window.columnconfigure(0, minsize=300)
window.columnconfigure(1, minsize=200)
window.columnconfigure(2, minsize=200)
window.columnconfigure(3, minsize=200)

# Default inputs. Adjust this part of the code if you want it to run on something consistently
before_image = tk.StringVar(value='C:\\Users\\samue\\Downloads\\BANDON_Dataset\\train\\train\\imgs\\bj\\t1\\L81_00991_784143.jpg')
after_image = tk.StringVar(value='C:\\Users\\samue\\Downloads\\BANDON_Dataset\\train\\train\\imgs\\bj\\t2\\L81_00991_784143.jpg')
output_before_image = tk.StringVar(value='Histogram_Matched_Before_Image.jpg')
output_after_image = tk.StringVar(value='Histogram_Matched_After_Image.jpg')
directory = tk.StringVar(value='')
save_to_a_file = tk.BooleanVar(value=True)
two_file_var = tk.BooleanVar(value=False)
equalization_var = tk.BooleanVar(value=True)
matching_var = tk.BooleanVar(value=False)
plotting_var = tk.BooleanVar(value=False)
directory_var = tk.BooleanVar(value=True)
second_directory = tk.StringVar(value='')
third_directory = tk.StringVar(value='')

def update_variable(var):
    input_file = askopenfilename()
    var.set(input_file)

def update_directory_variable(var):
    input_folder = filedialog.askdirectory()
    var.set(input_folder)

tk.Label(window, text='Two Images', font='bold').grid(row=0, column=0)
save_check_button = tk.Checkbutton(window, text='Two Images', variable=two_file_var)
save_check_button.grid(row=1,column=0, sticky='W', ipadx = 15)
tk.Label(window, text='Before Image').grid(row=2, column=0)
tk.Entry(window, textvariable=before_image, width=45).grid(row=3, column=0)
tk.Button(window, text='Open', command=partial(update_variable,before_image)).grid(row=2, column=0, sticky='E', padx=15)

tk.Label(window, text='After Image').grid(row=4, column=0)
tk.Entry(window, textvariable=after_image, width=45).grid(row=5, column=0)
tk.Button(window, text='Open', command=partial(update_variable,after_image)).grid(row=4, column=0, sticky='E', padx=15)

save_check_button = tk.Checkbutton(window, text='Save to a file', variable=save_to_a_file) #command=set_save_file,
save_check_button.grid(row=6,column=0, sticky='W', ipadx = 15)
plot_check_button = tk.Checkbutton(window, text='Create Plots', variable=plotting_var)
plot_check_button.grid(row=6,column=0, sticky='E', ipadx = 15)

tk.Label(window, text='Output Before Image').grid(row=7, column=0)
tk.Entry(window, textvariable=output_before_image, width=45).grid(row=8, column=0)

tk.Label(window, text='Output After Image').grid(row=9, column=0)
tk.Entry(window, textvariable=output_after_image, width=45).grid(row=10, column=0)



tk.Label(window, text='Directory', font='bold').grid(row=0, column=1)
directory_check_button = tk.Checkbutton(window, text='Save to a Directory', variable=directory_var) #command=set_save_file,
directory_check_button.grid(row=1,column=1, sticky='W', ipadx = 15)

tk.Label(window, text='Directory').grid(row=2, column=1)
tk.Entry(window, textvariable=directory, width=45).grid(row=3, column=1)
tk.Button(window, text='Open', command=partial(update_directory_variable, directory)).grid(row=2, column=1, sticky='E', padx=15)
tk.Label(window, text='Second Directory').grid(row=4, column=1)
tk.Entry(window, textvariable=second_directory, width=45).grid(row=5, column=1)
tk.Button(window, text='Open', command=partial(update_directory_variable, second_directory)).grid(row=4, column=1, sticky='E', padx=15)
tk.Label(window, text='Third Directory').grid(row=6, column=1)
tk.Entry(window, textvariable=third_directory, width=45).grid(row=7, column=1)
tk.Button(window, text='Open', command=partial(update_directory_variable, third_directory)).grid(row=6, column=1, sticky='E', padx=15)


tk.Label(window, text='Method', font='bold').grid(row=0, column=2)
equalization_check_button = tk.Checkbutton(window, text='Equalization', variable=equalization_var)
equalization_check_button.grid(row=1,column=2, sticky='W', padx=15)
matching_check_button = tk.Checkbutton(window, text='Match After Image to Before Image', variable=matching_var)
matching_check_button.grid(row=2,column=2, sticky='W', padx=15)


tk.Button(window, text='Run', command=window.destroy).grid(row=17, column=2)  # Closes the window and starts the program
window.mainloop()

# Get statements
save_to_a_file_bool = save_to_a_file.get()
before_image_str = before_image.get()
after_image_str = after_image.get()
output_before_image_str = output_before_image.get()
output_after_image_str = output_after_image.get()
directory_str = directory.get()
matching_bool = matching_var.get()
equalization_bool = equalization_var.get()
directory_bool = directory_var.get()
create_plots_bool = plotting_var.get()
two_files = two_file_var.get()
second_directory_str = second_directory.get()
third_directory_str = third_directory.get()


def find_average_values(img):
    img_rgb = img.convert('RGB')

    # Get the pixel data
    pixel_data = img_rgb.getdata()

    sum_r = sum_g = sum_b = 0

    # Iterate through each pixel
    for r, g, b in pixel_data:
        sum_r += r
        sum_g += g
        sum_b += b

    # Calculate the average for each channel
    num_pixels = img.width * img.height
    avg_r = sum_r / num_pixels
    avg_g = sum_g / num_pixels
    avg_b = sum_b / num_pixels
    # print('Average values for', avg_r, avg_g, avg_b)
    return avg_r, avg_g, avg_b



def equalize(image_str, file_name_to_save, cur_dir):
    if directory_bool:
        full_file_name = cur_dir + '/' + image_str
    else:
        full_file_name = image_str
    print('Equalizing', full_file_name)
    image_jpg = mpimg.imread(full_file_name)


    # if image_str[-3:] == 'png': # puts values back to 0 to 256
    #     # png_image = Image.open(full_file_name)
    #     # image_array = np.array(png_image.convert('RGB'))
    #     # image_jpg = mpimg.imread(image_array)
    #     # image_pixels = (image_jpg * 255).astype(np.uint8).reshape((-1, 3))
    #     png_image = Image.open(full_file_name)
    #     # Convert and save as JPG
    #     png_image.convert('RGB').save(full_file_name[-3:] + '.jpg', 'JPEG')
    #     image_jpg = mpimg.imread(full_file_name[-3:] + '.jpg')
    # # else: # image is a jpg
    # image_pixels = image_jpg.reshape((-1, 3))
    if image_str[-3:] == 'png': # puts values back to 0 to 256
        image_pixels = (image_jpg.reshape((-1, 3)) * 255).astype(int)
        #print(image_pixels)
    else: # image is a jpg
        image_pixels = image_jpg.reshape((-1, 3))
    image_cumulative_red = []
    image_cumulative_green = []
    image_cumulative_blue = []

    image = Image.open(full_file_name)
    # image.show()
    width, height = image.size
    L = 256
    N = width * height

    bin_width = 1
    bin_edges = np.arange(0, 255 + 2, 1)
    # print(len(bin_edges))
    image_counts_red, bins, _ = plt.hist(image_pixels[:, 0], bins=bin_edges, color='red', alpha=0, label='Red')
    image_counts_green, bins, _ = plt.hist(image_pixels[:, 1], bins=bin_edges, color='green', alpha=0, label='Red')
    image_counts_blue, bins, _ = plt.hist(image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0, label='Red')

    for i in range(len(image_counts_red)):
        if i > 0:
            image_cumulative_red += [image_cumulative_red[i - 1] + image_counts_red[i]]
            image_cumulative_green += [image_cumulative_green[i - 1] + image_counts_green[i]]
            image_cumulative_blue += [image_cumulative_blue[i - 1] + image_counts_blue[i]]
        else:
            image_cumulative_red += [image_counts_red[i]]
            image_cumulative_green += [image_counts_green[i]]
            image_cumulative_blue += [image_counts_blue[i]]

    scaled_values_red = []
    scaled_values_green = []
    scaled_values_blue = []
    for i in range(len(image_counts_red)):
        scaled_values_red += [round((L - 1) / N * image_cumulative_red[i])]
        scaled_values_green += [round((L - 1) / N * image_cumulative_green[i])]
        scaled_values_blue += [round((L - 1) / N * image_cumulative_blue[i])]

    # print('Scaled values red', scaled_values_red)
    new_pixel_values_red = []
    new_pixel_values_green = []
    new_pixel_values_blue = []
    # print(image_pixels)
    # print(type(image_pixels))
    # print(len(image_pixels))
    for i in range(len(image_pixels)):
        new_pixel_values_red += [scaled_values_red[image_pixels[i][0]]]
        new_pixel_values_green += [scaled_values_green[image_pixels[i][1]]]
        new_pixel_values_blue += [scaled_values_blue[image_pixels[i][2]]]


    new_red_band = Image.new('L', image.size)
    new_red_band.putdata(new_pixel_values_red)
    new_green_band = Image.new('L', image.size)
    new_green_band.putdata(new_pixel_values_green)
    new_blue_band = Image.new('L', image.size)
    new_blue_band.putdata(new_pixel_values_blue)
    equalized_image = Image.merge('RGB', (new_red_band, new_green_band, new_blue_band))
    # equalized_image.show()
    if save_to_a_file_bool:
        equalized_image.save(full_file_name)
    # image_counts_red.remove()
    # image_counts_blue.remove()
    # image_counts_green.remove()
    # if directory_str != '':
    #     plt.close('all')

    return new_pixel_values_red, new_pixel_values_green, new_pixel_values_blue, equalized_image

# Matches two images together
def match(before_image_str, after_image_str, after_image_name_to_save):
    print('Matching', after_image_str, 'to', before_image_str)
    # print(before_image_str, after_image_str)
    before_image_jpg = mpimg.imread(before_image_str)
    after_image_jpg = mpimg.imread(after_image_str)

    # plt.imshow(image_jpg)

    if before_image_str[-3:] == 'png':  # puts values back to 0 to 256
        before_image_pixels = (before_image_jpg.reshape((-1, 3)) * 255).astype(int)
        after_image_pixels = (after_image_jpg.reshape((-1, 3)) * 255).astype(int)
    else:  # image is a jpg
        before_image_pixels = before_image_jpg.reshape((-1, 3))
        after_image_pixels = after_image_jpg.reshape((-1, 3))
    before_image_cumulative_red = []
    before_image_cumulative_green = []
    before_image_cumulative_blue = []
    after_image_cumulative_red = []
    after_image_cumulative_green = []
    after_image_cumulative_blue = []

    before_image = Image.open(before_image_str)
    after_image = Image.open(after_image_str)
    # image.show()
    width, height = before_image.size
    L = 256
    N = width * height

    bin_edges = np.arange(0, 255 + 2, 1)
    # before_image_counts_red, bins, _ = plt.hist(before_image_pixels[:, 0], bins=256, color='red', alpha=0, label='Red')
    # before_image_counts_green, bins, _ = plt.hist(before_image_pixels[:, 1], bins=256, color='green', alpha=0, label='Red')
    # before_image_counts_blue, bins, _ = plt.hist(before_image_pixels[:, 2], bins=256, color='blue', alpha=0, label='Red')
    # after_image_counts_red, bins, _ = plt.hist(after_image_pixels[:, 0], bins=256, color='red', alpha=0, label='Red')
    # after_image_counts_green, bins, _ = plt.hist(after_image_pixels[:, 1], bins=256, color='green', alpha=0, label='Red')
    # after_image_counts_blue, bins, _ = plt.hist(after_image_pixels[:, 2], bins=256, color='blue', alpha=0, label='Red')
    before_image_counts_red, bins, _ = plt.hist(before_image_pixels[:, 0], bins=bin_edges, color='red', alpha=0, label='Red')
    before_image_counts_green, bins, _ = plt.hist(before_image_pixels[:, 1], bins=bin_edges, color='green', alpha=0, label='Red')
    before_image_counts_blue, bins, _ = plt.hist(before_image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0, label='Red')
    after_image_counts_red, bins, _ = plt.hist(after_image_pixels[:, 0], bins=bin_edges, color='red', alpha=0, label='Red')
    after_image_counts_green, bins, _ = plt.hist(after_image_pixels[:, 1], bins=bin_edges, color='green', alpha=0, label='Red')
    after_image_counts_blue, bins, _ = plt.hist(after_image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0, label='Red')

    for i in range(len(before_image_counts_red)):
        if i > 0:
            before_image_cumulative_red += [before_image_cumulative_red[i - 1] + before_image_counts_red[i]]
            before_image_cumulative_green += [before_image_cumulative_green[i - 1] + before_image_counts_green[i]]
            before_image_cumulative_blue += [before_image_cumulative_blue[i - 1] + before_image_counts_blue[i]]
        else:
            before_image_cumulative_red += [before_image_counts_red[i]]
            before_image_cumulative_green += [before_image_counts_green[i]]
            before_image_cumulative_blue += [before_image_counts_blue[i]]
    for i in range(len(before_image_counts_red)):
        if i > 0:
            after_image_cumulative_red += [after_image_cumulative_red[i - 1] + after_image_counts_red[i]]
            after_image_cumulative_green += [after_image_cumulative_green[i - 1] + after_image_counts_green[i]]
            after_image_cumulative_blue += [after_image_cumulative_blue[i - 1] + after_image_counts_blue[i]]
        else:
            after_image_cumulative_red += [after_image_counts_red[i]]
            after_image_cumulative_green += [after_image_counts_green[i]]
            after_image_cumulative_blue += [after_image_counts_blue[i]]
    # plt.show()

    scaled_values_red = []
    scaled_values_green = []
    scaled_values_blue = []
    # Find the same value in the next histogram
    def find_closest_value(bef_cumulative_list, target):
        # return min(lst, key=lambda x: abs(x - target))
        index = 0
        best_difference = 1000000000
        for k in range(len(bef_cumulative_list)):
            difference = abs(bef_cumulative_list[k] - target)
            if difference < best_difference:
                best_difference = difference
                best_index = k
        return best_index
        # return min(range(len(lst)), key=lambda i: abs(lst[i] - target))
    # print('Bef cumulative red', before_image_cumulative_red)
    # print('Aft cumulative red', after_image_cumulative_red)
    for i in range(len(before_image_counts_red)):
        scaled_values_red += [round(find_closest_value(before_image_cumulative_red, after_image_cumulative_red[i]))]
        scaled_values_blue += [round(find_closest_value(before_image_cumulative_blue, after_image_cumulative_blue[i]))]
        scaled_values_green += [round(find_closest_value(before_image_cumulative_green, after_image_cumulative_green[i]))]
        # scaled_values_red += [round(find_closest_value(after_image_cumulative_red, before_image_cumulative_red[i]))]
        # scaled_values_blue += [round(find_closest_value(after_image_cumulative_blue, before_image_cumulative_blue[i]))]
        # scaled_values_green += [round(find_closest_value(after_image_cumulative_green, before_image_cumulative_green[i]))]
        # scaled_values_red += [round(after_image_cumulative_red[i] * before_image_cumulative_red[i]/ (256/2))]

    # print('Scaled values red', len(scaled_values_red), scaled_values_red)
    # for i in range(len(before_image_counts_red)):
    #     search_index_red = 0
    #     while after_image_cumulative_red[search_index_red] < before_image_cumulative_red[i]:
    #         search_index_red += 1
    #     if after_image_cumulative_red[search_index_red] == before_image_cumulative_red[i]:
    #         scaled_values_red += [round(after_image_cumulative_red[i])]
    #     else:
    #         y_1 = before_image_cumulative_red[i] - after_image_cumulative_red[search_index_red - 1]
    #         y_2 = after_image_cumulative_red[search_index_red] - before_image_cumulative_red[i]
    #         x = y_1/(y_2 + y_1)
    #         difference_after_red = after_image_cumulative_red[i] - after_image_cumulative_red[i - 1]
    #         scaled_values_red += [round(after_image_cumulative_red[i] + difference_after_red)]
    #
    #     scaled_values_red += [round((L - 1) / N * before_image_cumulative_red[i] / after_image_cumulative_red[i])]
    #     scaled_values_green += [round((L - 1) / N * before_image_cumulative_green[i] / after_image_cumulative_red[i])]
    #     scaled_values_blue += [round((L - 1) / N * before_image_cumulative_blue[i] / after_image_cumulative_red[i])]


    # for i in range(len(before_image_counts_red)):
    #     scaled_values_red += [round((L - 1) / N * before_image_cumulative_red[i] / after_image_cumulative_red[i])]
    #     scaled_values_green += [round((L - 1) / N * before_image_cumulative_green[i] / after_image_cumulative_red[i])]
    #     scaled_values_blue += [round((L - 1) / N * before_image_cumulative_blue[i] / after_image_cumulative_red[i])]

    new_pixel_values_red = []
    new_pixel_values_green = []
    new_pixel_values_blue = []
    # print(image_pixels)
    # print(type(image_pixels))
    # print(len(image_pixels))
    for i in range(len(after_image_pixels)):
        new_pixel_values_red += [scaled_values_red[after_image_pixels[i][0]]]
        new_pixel_values_green += [scaled_values_green[after_image_pixels[i][1]]]
        new_pixel_values_blue += [scaled_values_blue[after_image_pixels[i][2]]]

    # Find average values
    avg_red, avg_green, avg_blue = find_average_values(before_image)

    # Created cumulative histogram plots and matched things
    if create_plots_bool:
        fig1, axs1 = plt.subplots(4, 4, figsize=(10, 8))
        axs1[0, 0].imshow(before_image_jpg)
        axs1[0, 0].set_title('Before Image')

        axs1[1, 0].imshow(after_image_jpg)
        axs1[1, 0].set_title('After Image')

        # Before Image
        axs1[0, 0].imshow(before_image_jpg)
        axs1[0, 1].plot(range(len(before_image_cumulative_red)), before_image_cumulative_red, color='red', alpha=0.5)
        axs1[0, 2].plot(range(len(before_image_cumulative_green)), before_image_cumulative_green, color='green', alpha=0.5)
        axs1[0, 3].plot(range(len(before_image_cumulative_blue)), before_image_cumulative_blue, color='blue', alpha=0.5)
        # axs[0, 1].axvline(x=avg_red, color='black', linestyle='-', linewidth=2)
        # axs[0, 2].axvline(x=avg_green, color='black', linestyle='-', linewidth=2)
        # axs[0, 3].axvline(x=avg_blue, color='black', linestyle='-', linewidth=2)
        aft_img_cumulative_red_copy = []
        aft_img_cumulative_green_copy = []
        aft_img_cumulative_blue_copy = []
        for i in range(len(before_image_counts_red)):
            if i > 0:
                aft_img_cumulative_red_copy += [after_image_cumulative_red[i - 1] + after_image_counts_red[i]]
                aft_img_cumulative_green_copy += [after_image_cumulative_green[i - 1] + after_image_counts_green[i]]
                aft_img_cumulative_blue_copy += [after_image_cumulative_blue[i - 1] + after_image_counts_blue[i]]
            else:
                aft_img_cumulative_red_copy += [after_image_counts_red[i]]
                aft_img_cumulative_green_copy += [after_image_counts_green[i]]
                aft_img_cumulative_green_copy += [after_image_counts_blue[i]]
        # After image
        axs1[1, 0].imshow(after_image_jpg)
        axs1[1, 1].plot(range(len(after_image_cumulative_red)), after_image_cumulative_red, color='red', alpha=0.5)
        axs1[1, 2].plot(range(len(after_image_cumulative_green)), after_image_cumulative_green, color='green', alpha=0.5)
        axs1[1, 3].plot(range(len(after_image_cumulative_blue)), after_image_cumulative_blue, color='blue', alpha=0.5)

        # Make the unshifted after image
        new_red_band1 = Image.new('L', after_image.size)
        new_red_band1.putdata(new_pixel_values_red)
        new_green_band1 = Image.new('L', after_image.size)
        new_green_band1.putdata(new_pixel_values_green)
        new_blue_band1 = Image.new('L', after_image.size)
        new_blue_band1.putdata(new_pixel_values_blue)
        matched_after_image_unshifted = Image.merge('RGB', (new_red_band1, new_green_band1, new_blue_band1))

        # Unshifted after image plots
        axs1[2, 0].imshow(matched_after_image_unshifted)
        axs1[2, 0].set_title('After Image')
        bin_edges = np.arange(0, 255 + 2, 1)
        image_counts_red1, bins_r1, _ = axs1[2, 1].hist(new_pixel_values_red, bins=bin_edges, color='red', alpha=0.5, label='Red')
        image_counts_green1, bins_g1, _ = axs1[2, 2].hist(new_pixel_values_green, bins=bin_edges, color='green', alpha=0.5, label='Red')
        image_counts_blue1, bins_b1, _ = axs1[2, 3].hist(new_pixel_values_blue, bins=bin_edges, color='blue', alpha=0.5, label='Red')
        # axs1[2, 1].axvline(x=sum(new_pixel_values_red)/len(new_pixel_values_red), color='black', linestyle='-', linewidth=2)
        # axs1[2, 2].axvline(x=sum(new_pixel_values_green)/len(new_pixel_values_green), color='black', linestyle='-', linewidth=2)
        # axs1[2, 3].axvline(x=sum(new_pixel_values_blue)/len(new_pixel_values_blue), color='black', linestyle='-', linewidth=2)



    # Find values to shift by
    avg_red_diff = avg_red - sum(new_pixel_values_red) / len(new_pixel_values_red)
    avg_green_diff = avg_green - sum(new_pixel_values_green) / len(new_pixel_values_green)
    avg_blue_diff = avg_blue - sum(new_pixel_values_blue) / len(new_pixel_values_blue)
    # print('Average differences', avg_red_diff, avg_green_diff, avg_blue_diff)

    # Apply shift
    # for i in range(len(after_image_pixels)):
    #     new_pixel_values_red[i] += round(avg_red_diff)
    #     if new_pixel_values_red[i] < 0:
    #         new_pixel_values_red[i] = 0
    #     elif new_pixel_values_red[i] > 255:
    #         new_pixel_values_red[i] = 255
    #     new_pixel_values_blue[i] += round(avg_blue_diff)
    #     if new_pixel_values_blue[i] < 0:
    #         new_pixel_values_blue[i] = 0
    #     elif new_pixel_values_blue[i] > 255:
    #         new_pixel_values_blue[i] = 255
    #     new_pixel_values_green[i] += round(avg_green_diff)
    #     if new_pixel_values_green[i] < 0:
    #         new_pixel_values_green[i] = 0
    #     elif new_pixel_values_green[i] > 255:
    #         new_pixel_values_green[i] = 255

    new_red_band = Image.new('L', after_image.size)
    new_red_band.putdata(new_pixel_values_red)
    new_green_band = Image.new('L', after_image.size)
    new_green_band.putdata(new_pixel_values_green)
    new_blue_band = Image.new('L', after_image.size)
    new_blue_band.putdata(new_pixel_values_blue)
    matched_after_image = Image.merge('RGB', (new_red_band, new_green_band, new_blue_band))
    if create_plots_bool:
        for j in range(4):
            for k in range(4):
                axs1[k, j].set_xticks([])
                axs1[k, j].set_yticks([])
        axs1[3, 0].imshow(matched_after_image)
        axs1[3, 0].set_title('After Image Shifted')
        bin_edges = np.arange(0, 255 + 2, 1)
        image_counts_red1, bins_r1, _ = axs1[3, 1].hist(new_pixel_values_red, bins=bin_edges, color='red', alpha=0.5, label='Red')
        image_counts_green1, bins_g1, _ = axs1[3, 2].hist(new_pixel_values_green, bins=bin_edges, color='green', alpha=0.5, label='Red')
        image_counts_blue1, bins_b1, _ = axs1[3, 3].hist(new_pixel_values_blue, bins=bin_edges, color='blue', alpha=0.5, label='Red')
        # plt.show()

    # equalized_image.show()
    if save_to_a_file_bool:
        matched_after_image.save(after_image_name_to_save)
    # image_counts_red.remove()
    # image_counts_blue.remove()
    # image_counts_green.remove()
    if directory_str != '':
        plt.close('all')

    # print('Before image')
    # find_average_values(before_image)
    # print('After image')
    # find_average_values(after_image)
    # print('Matched after image')
    # find_average_values(matched_after_image)
    return new_pixel_values_red, new_pixel_values_green, new_pixel_values_blue, matched_after_image


if two_files:
    # Read in the images
    before_image_jpg = mpimg.imread(before_image_str)
    after_image_jpg = mpimg.imread(after_image_str)
    # plt.imshow(before_image_jpg)
    # Flattens the images
    if before_image_str[-3:] == 'png': # puts values back to 0 to 256
        before_image_pixels = (before_image_jpg.reshape((-1, 3)) * 255).astype(int)
        after_image_pixels = (after_image_jpg.reshape((-1, 3)) * 255).astype(int)
    else: # image is a jpg
        # image_pixels = image_jpg.reshape((-1, 3))
        before_image_pixels = before_image_jpg.reshape((-1, 3))
        after_image_pixels = after_image_jpg.reshape((-1, 3))
    # Plots
    fig, axs = plt.subplots(4, 4, figsize=(10,8))
    # fig, axs = plt.subplots(6, 4, figsize=(12,8))
    # Image plots
    axs[0,0].imshow(before_image_jpg)
    axs[0,0].set_title('Before Image')

    axs[1,0].imshow(after_image_jpg)
    axs[1,0].set_title('After Image')

    # Before image histograms
    bin_edges = np.arange(0, 255 + 2, 1)
    image_counts_red, bins_r, _ = axs[0,1].hist(before_image_pixels[:, 0], bins=bin_edges, color='red', alpha=0.5, label='Red')
    image_counts_green, bins_g, _ = axs[0,2].hist(before_image_pixels[:, 1], bins=bin_edges, color='green', alpha=0.5, label='Red')
    image_counts_blue, bins_b, _ = axs[0,3].hist(before_image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0.5, label='Red')

    num_bins = 10
    row_index_for_matched_after_image = 3
    if equalization_bool:
        new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, matched_before_image = equalize(before_image_str, output_before_image_str, before_image_str)
        axs[2,1].hist(new_pixel_vals_red, bins=num_bins, color='red', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
        axs[2,2].hist(new_pixel_vals_green, bins=num_bins, color='green', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
        axs[2,3].hist(new_pixel_vals_blue, bins=num_bins, color='blue', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)
        axs[2, 0].set_title('Equalized Before Image')
        axs[2, 0].imshow(matched_before_image)
    elif matching_bool:
        row_index_for_matched_after_image = 2

    # After Image Histograms
    bin_edges = np.arange(0, 255 + 2, 1)
    image_counts_red1, bins_r1, _ = axs[1, 1].hist(after_image_pixels[:, 0], bins=bin_edges, color='red', alpha=0.5, label='Red')
    image_counts_green1, bins_g1, _ = axs[1, 2].hist(after_image_pixels[:, 1], bins=bin_edges, color='green', alpha=0.5, label='Red')
    image_counts_blue1, bins_b1, _ = axs[1, 3].hist(after_image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0.5, label='Red')


    new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, matched_after_image = equalize(after_image_str, output_after_image_str, after_image_str)
    axs[row_index_for_matched_after_image,1].hist(new_pixel_vals_red, bins=bin_edges, color='red', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
    axs[row_index_for_matched_after_image,2].hist(new_pixel_vals_green, bins=bin_edges, color='green', alpha=0.5, label='green', weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
    axs[row_index_for_matched_after_image,3].hist(new_pixel_vals_blue, bins=bin_edges, color='blue', alpha=0.5, label='blue', weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)

    if matching_bool:
        axs[2, 0].set_title('Equalized After Image')
        axs[2, 0].imshow(matched_after_image)
        new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, matched_after_image = match(before_image_str,
                                                                                                       after_image_str, after_image_str)
        num_bins = 256
        bin_edges = np.arange(0, 255 + 2, 1)
        axs[3, 1].hist(new_pixel_vals_red, bins=bin_edges, color='red', alpha=0.5, label='Red',
                       weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
        axs[3, 2].hist(new_pixel_vals_green, bins=bin_edges, color='green', alpha=0.5, label='Red',
                       weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
        axs[3, 3].hist(new_pixel_vals_blue, bins=bin_edges, color='blue', alpha=0.5, label='Red',
                       weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)

    # print('Red', image_counts_red1)
    # print('Blue', image_counts_blue1)
    # print('Blue_new', image_counts_aft)
    maximum_count = max(max(image_counts_red), max(image_counts_green), max(image_counts_blue), max(image_counts_red1), max(image_counts_green1), max(image_counts_blue1))
    # print(np.max(image_counts_red), max(image_counts_green), max(image_counts_blue), max(image_counts_red1), max(image_counts_green1), max(image_counts_blue1))
    print('Max count', maximum_count)
    for i in range(4):
        for j in range(3):
            axs[i, j + 1].set_ylim(0, maximum_count)
    # Matched images

    if equalization_bool:
        axs[3,0].set_title('Equalized After Image')
        axs[3,0].imshow(matched_after_image)
    elif matching_bool:
        axs[3,0].set_title('Matched After Image')
        axs[3,0].imshow(matched_after_image)

    # Change formatting of images
    for i in range(4):
        axs[i,0].set_xticks([])
        axs[i,0].set_yticks([])

    # Change formatting of histograms
    for i in range(4):
        for j in range(3):
            # axs[i, j + 1].set_ylabel('Frequency')
            # axs[i, j + 1].set_xlabel('Brightness')
            axs[i,  j + 1].set_yticks([])
            axs[i, j + 1].set_xticks([])
            axs[i, j + 1].set_xlim(0, 256)
            # axs[i, j + 1].grid()

    # Add space between plots? plt.subplots_adjust(wspace=0.4, hspace=0.4)
    # plt.tight_layout()
    # plt.title(after_image_str)
    if create_plots_bool:
        plt.show()

elif directory_bool:
    if equalization_bool:
        print('Equalizing directory:', directory_str)
        image_names = os.listdir(directory_str)
        print('Equalizing', len(image_names), 'images', image_names)
        for image_name in image_names:
            # print(image_name)
            equalize(image_name, image_name, directory_str)
            plt.close('all')
        if second_directory_str !='':
            print('Equalizing directory:', second_directory_str)
            image_names = []
            image_names = os.listdir(second_directory_str)
            print('Equalizing', len(image_names), 'images', image_names)
            for image_name in image_names:
                equalize(image_name, image_name, second_directory_str)
                plt.close('all')
        if third_directory_str !='':
            print('Equalizing directory:', third_directory_str)
            image_names = []
            image_names = os.listdir(third_directory_str)
            print('Equalizing', len(image_names), 'images', image_names)
            for image_name in image_names:
                # print(image_name)
                equalize(image_name, image_name, third_directory_str)
                plt.close('all')
    elif matching_bool:
        print('Matching directory', second_directory_str, 'to', directory_str)
        image_names = os.listdir(second_directory_str)
        print('List of images to try to be matched:', len(image_names), image_names)
        image_names_to_compare = os.listdir(directory_str)
        print('List of comparison images', len(image_names_to_compare), image_names_to_compare)
        list_of_unmatched_images = []
        for image_name in image_names:
            before_full_file_name = directory_str + '/' + image_name
            after_full_file_name = second_directory_str + '/' + image_name
            if image_name in image_names_to_compare:
                # print('Matching', image_name, '\b. Overwriting', after_full_file_name)
                match(before_full_file_name, after_full_file_name, after_full_file_name)
                plt.close('all')
            else:
                list_of_unmatched_images += [image_name]
        print('List of unmatched images', list_of_unmatched_images)
        if third_directory_str!= '':
            print('\nMatching directory', third_directory_str, 'to', directory_str)
            image_names = os.listdir(third_directory_str)
            print('List of images to be matched:', image_names)
            image_names_to_compare = os.listdir(directory_str)
            print('List of comparison images', image_names_to_compare)
            list_of_unmatched_images = []
            for image_name in image_names:
                before_full_file_name = directory_str + '/' + image_name
                after_full_file_name = third_directory_str + '/' + image_name
                if image_name in image_names_to_compare:
                    # print('Matching', image_name, '\b. Overwriting', after_full_file_name)
                    match(before_full_file_name, after_full_file_name, after_full_file_name)
                    plt.close('all')
                else:
                    list_of_unmatched_images += [image_name]
            print('List of unmatched images', list_of_unmatched_images)
            print('\nMatching the unmatched images from the third directory to the second directory')
            for image_name in list_of_unmatched_images:
                before_full_file_name = second_directory_str + '/' + image_name
                after_full_file_name = third_directory_str + '/' + image_name
                print('Matching', image_name, 'in third directory to second directory', '\b. Overwriting', after_full_file_name)
                match(before_full_file_name, after_full_file_name, after_full_file_name)

    else:
        print('Please select a method to alter the images')
    # print(image_names)

frequency = 600  # Set frequency (2500 Hz)
duration = 1000  # Set duration (1000 ms or 1 second)
winsound.Beep(frequency, duration)
winsound.Beep(500, 1000)
winsound.Beep(frequency, duration)