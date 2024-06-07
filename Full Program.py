## Section 1: Import statements

# Standard packages
import math
import os

# Other packages. Download tkinter, numpy, matplotlib, PIL if they are not already downloaded
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tkinter.filedialog import askopenfilename
from functools import partial
from PIL import Image
from tkinter import filedialog


## Section 2: Graphical User Interface
window = tk.Tk()
window.title('My Window')
window.geometry('900x470')
window.columnconfigure(0, minsize=300)
window.columnconfigure(1, minsize=200)
window.columnconfigure(2, minsize=200)
window.columnconfigure(3, minsize=200)

# Default inputs. Adjust the values in this part of the code to change the default values
before_image = tk.StringVar(value='')
after_image = tk.StringVar(value='')
output_before_image = tk.StringVar(value='')
output_after_image = tk.StringVar(value='')
directory = tk.StringVar(value='')
save_to_a_file = tk.BooleanVar(value=False)
two_file_var = tk.BooleanVar(value=False)
equalization_var = tk.BooleanVar(value=False)
matching_var = tk.BooleanVar(value=True)
plotting_var = tk.BooleanVar(value=False)
directory_var = tk.BooleanVar(value=False)
second_directory = tk.StringVar(value='')
third_directory = tk.StringVar(value='')
first_save_directory = tk.StringVar(value='')
second_save_directory = tk.StringVar(value='')
third_save_directory = tk.StringVar(value='')
show_axes_var = tk.BooleanVar(value=True)

# Functions to open file explorer
def update_variable(var):
    input_file = askopenfilename()
    var.set(input_file)

def update_directory_variable(var):
    input_folder = filedialog.askdirectory()
    var.set(input_folder)

# Functions to make additional options appear
def two_images(): # The user selects two images which allows them to input before and after images and gives a choice to create plots or save files
    tk.Label(window, text='Before Image').grid(row=2, column=0)
    tk.Entry(window, textvariable=before_image, width=45).grid(row=3, column=0)
    tk.Button(window, text='Open', command=partial(update_variable, before_image)).grid(row=2, column=0, sticky='E',
                                                                                        padx=15)
    tk.Label(window, text='After Image').grid(row=4, column=0)
    tk.Entry(window, textvariable=after_image, width=45).grid(row=5, column=0)
    tk.Button(window, text='Open', command=partial(update_variable, after_image)).grid(row=4, column=0, sticky='E',
                                                                                       padx=15)
    save_check_button = tk.Checkbutton(window, text='Save to a file', variable=save_to_a_file,
                                       command=set_save_file)  # command=set_save_file,
    save_check_button.grid(row=6, column=0, sticky='W', ipadx=15)
    plot_check_button = tk.Checkbutton(window, text='Create plots', variable=plotting_var,
                                       command=create_plots_function)
    plot_check_button.grid(row=6, column=0, sticky='E', ipadx=15)

def set_save_file(): # The user selects where they would like to save the files to
    tk.Label(window, text='Output Before Image (include extension like.jpg)').grid(row=7, column=0)
    tk.Entry(window, textvariable=output_before_image, width=45).grid(row=8, column=0)
    tk.Label(window, text='Output After Image (include extension like.png)').grid(row=9, column=0)
    tk.Entry(window, textvariable=output_after_image, width=45).grid(row=10, column=0)

def create_plots_function(): # The user can decide if they want to show the axes after they click on create plots
    axes_check_button = tk.Checkbutton(window, text='Show axes', variable=show_axes_var)
    axes_check_button.grid(row=11, column=0, sticky='W', ipadx=15)

def set_directories(): # The user can choose directory locations after selecting directory enhancements
    tk.Label(window, text='First Input Directory').grid(row=2, column=1)
    tk.Entry(window, textvariable=directory, width=45).grid(row=3, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, directory)).grid(row=2, column=1,
                                                                                               sticky='E', padx=15)
    tk.Label(window, text='Second Input Directory').grid(row=4, column=1)
    tk.Entry(window, textvariable=second_directory, width=45).grid(row=5, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, second_directory)).grid(row=4, column=1,
                                                                                                      sticky='E',
                                                                                                      padx=15)
    tk.Label(window, text='Third Input Directory').grid(row=6, column=1)
    tk.Entry(window, textvariable=third_directory, width=45).grid(row=7, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, third_directory)).grid(row=6, column=1,
                                                                                                     sticky='E',
                                                                                                     padx=15)
    tk.Label(window, text='First Save Directory').grid(row=8, column=1)
    tk.Entry(window, textvariable=first_save_directory, width=45).grid(row=9, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, first_save_directory)).grid(row=8, column=1,
                                                                                               sticky='E', padx=15)
    tk.Label(window, text='Second Save Directory').grid(row=10, column=1)
    tk.Entry(window, textvariable=second_save_directory, width=45).grid(row=11, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, second_save_directory)).grid(row=10, column=1,
                                                                                                      sticky='E',
                                                                                                      padx=15)
    tk.Label(window, text='Third Save Directory').grid(row=12, column=1)
    tk.Entry(window, textvariable=third_save_directory, width=45).grid(row=13, column=1)
    tk.Button(window, text='Open', command=partial(update_directory_variable, third_save_directory)).grid(row=12, column=1,
                                                                                                     sticky='E',
                                                                                                     padx=15)
# Buttons and headers that always show up
# First column
tk.Label(window, text='Two Images', font='bold').grid(row=0, column=0)
save_check_button = tk.Checkbutton(window, text='Two Images', variable=two_file_var, command=two_images)
save_check_button.grid(row=1,column=0, sticky='W', ipadx = 15)

# Second column
tk.Label(window, text='Directory', font='bold').grid(row=0, column=1)
directory_check_button = tk.Checkbutton(window, text='Enhancement to Directory', variable=directory_var, command=set_directories)
directory_check_button.grid(row=1,column=1, sticky='W', ipadx = 15)

# Third column
tk.Label(window, text='Method', font='bold').grid(row=0, column=2)
equalization_check_button = tk.Checkbutton(window, text='Equalization', variable=equalization_var)
equalization_check_button.grid(row=1,column=2, sticky='W', padx=15)
matching_check_button = tk.Checkbutton(window, text='Match After Image to Before Image', variable=matching_var)
matching_check_button.grid(row=2,column=2, sticky='W', padx=15)

# Run button
tk.Button(window, text='Run', command=window.destroy).grid(row=17, column=2)  # Closes the window and starts the program
window.mainloop()


# Get statements to get the values from tkinter once the GUI has been closed
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
first_save_directory_str = first_save_directory.get()
second_save_directory_str = second_save_directory.get()
third_save_directory_str = third_save_directory.get()
show_axes_bool = show_axes_var.get()

# Section 3: Functions
def find_average_values(img): # Finds the average green, red, and blue values in an image
    img_rgb = img.convert('RGB')
    pixel_data = img_rgb.getdata()
    sum_red = sum_green = sum_blue = 0

    for r, g, b in pixel_data:
        sum_red += r
        sum_green += g
        sum_blue += b

    num_pixels = img.width * img.height
    average_red = sum_red / num_pixels
    average_green = sum_green / num_pixels
    average_blue = sum_blue / num_pixels
    return average_red, average_green, average_blue

def find_closest_value(before_cumulative_list, target): # Finds the index of the closest value in a list
    index = 0
    best_difference = 1000000000
    for k in range(len(before_cumulative_list)):
        difference = abs(before_cumulative_list[k] - target)
        if difference < best_difference:
            best_difference = difference
            best_index = k
    return best_index

# Section 4: Equalize and match functions
def equalize(image_str, file_name_to_save, to_save): # Equalizes an image and saves it to a file if desired
    full_file_name = image_str
    save_full_file_name = file_name_to_save
    print('Equalizing', full_file_name)
    image_jpg = mpimg.imread(full_file_name)

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

    new_pixel_values_red = []
    new_pixel_values_green = []
    new_pixel_values_blue = []

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

    if to_save:
        print('Saving equalized image at', save_full_file_name)
        folder = os.path.dirname(save_full_file_name)
        if not os.path.exists(folder) and folder != '': # If the folder exists and isn't an empty string
            os.makedirs(folder)
        equalized_image.save(save_full_file_name)
    if directory_bool:
        plt.close('all')
    return new_pixel_values_red, new_pixel_values_green, new_pixel_values_blue, equalized_image

# Matches the second image to the first image
def match(before_image_str, after_image_str, after_image_name_to_save, to_save):
    print('Matching', after_image_str, 'to', before_image_str)
    before_image_jpg = mpimg.imread(before_image_str)
    after_image_jpg = mpimg.imread(after_image_str)

    if before_image_str[-3:] == 'png':  # puts brightness values to 0 to 256
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

    width, height = before_image.size
    L = 256
    N = width * height

    bin_edges = np.arange(0, 255 + 2, 1)
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

    scaled_values_red = []
    scaled_values_green = []
    scaled_values_blue = []

    for i in range(len(before_image_counts_red)):
        scaled_values_red += [round(find_closest_value(before_image_cumulative_red, after_image_cumulative_red[i]))]
        scaled_values_blue += [round(find_closest_value(before_image_cumulative_blue, after_image_cumulative_blue[i]))]
        scaled_values_green += [round(find_closest_value(before_image_cumulative_green, after_image_cumulative_green[i]))]

    new_pixel_values_red = []
    new_pixel_values_green = []
    new_pixel_values_blue = []

    for i in range(len(after_image_pixels)):
        new_pixel_values_red += [scaled_values_red[after_image_pixels[i][0]]]
        new_pixel_values_green += [scaled_values_green[after_image_pixels[i][1]]]
        new_pixel_values_blue += [scaled_values_blue[after_image_pixels[i][2]]]

    # Find average values
    avg_red, avg_green, avg_blue = find_average_values(before_image)

    # Created cumulative histogram plots and matched things
    if create_plots_bool:
        # fig1, axs1 = plt.subplots(4, 4, figsize=(10, 8))
        axs[2, 0].imshow(before_image_jpg)
        axs[2, 0].set_title('Before Cumulative')

        axs[3, 0].imshow(after_image_jpg)
        axs[3, 0].set_title('After Cumulative')

        # Before Image
        axs[2, 0].imshow(before_image_jpg)
        axs[2, 1].plot(range(len(before_image_cumulative_red)), before_image_cumulative_red, color='red', alpha=0.5)
        axs[2, 2].plot(range(len(before_image_cumulative_green)), before_image_cumulative_green, color='green', alpha=0.5)
        axs[2, 3].plot(range(len(before_image_cumulative_blue)), before_image_cumulative_blue, color='blue', alpha=0.5)

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
        axs[3, 0].imshow(after_image_jpg)
        axs[3, 1].plot(range(len(after_image_cumulative_red)), after_image_cumulative_red, color='red', alpha=0.5)
        axs[3, 2].plot(range(len(after_image_cumulative_green)), after_image_cumulative_green, color='green', alpha=0.5)
        axs[3, 3].plot(range(len(after_image_cumulative_blue)), after_image_cumulative_blue, color='blue', alpha=0.5)

    avg_red_diff = avg_red - sum(new_pixel_values_red) / len(new_pixel_values_red)
    avg_green_diff = avg_green - sum(new_pixel_values_green) / len(new_pixel_values_green)
    avg_blue_diff = avg_blue - sum(new_pixel_values_blue) / len(new_pixel_values_blue)

    new_red_band = Image.new('L', after_image.size)
    new_red_band.putdata(new_pixel_values_red)
    new_green_band = Image.new('L', after_image.size)
    new_green_band.putdata(new_pixel_values_green)
    new_blue_band = Image.new('L', after_image.size)
    new_blue_band.putdata(new_pixel_values_blue)
    matched_after_image = Image.merge('RGB', (new_red_band, new_green_band, new_blue_band))

    if to_save:
        print('Saving matched image at', after_image_name_to_save)
        folder = os.path.dirname(after_image_name_to_save)
        if not os.path.exists(folder) and folder != '':
            os.makedirs(folder)
        matched_after_image.save(after_image_name_to_save)

    if directory_bool:
        plt.close('all')

    return new_pixel_values_red, new_pixel_values_green, new_pixel_values_blue, matched_after_image

# Section 4: Main Script
# Let user know about potential errors

if output_before_image_str != '' and matching_bool == True:
    print('The before image will not change so no file will be saved for the before image.')

# Terminal errors
if output_after_image_str == '' and matching_bool and two_files and save_to_a_file_bool:
    print('Please select a file name to save the new matched output after image.')
elif output_before_image_str == '' and two_files and equalization_bool and save_to_a_file_bool:
    print('Please select a file name to save the equalized image to.')
elif equalization_bool == matching_bool: # If there is no enhancement technique selected or both are selected
    print('Please select one radiometric enhancement technique at a time')

# If there are no terminal errors, run the script for two files if it is checked
elif two_files:
    # Read in the images
    before_image_jpg = mpimg.imread(before_image_str)
    after_image_jpg = mpimg.imread(after_image_str)

    # Flatten the images
    if before_image_str[-3:] == 'png': # puts values back to 0 to 256
        before_image_pixels = (before_image_jpg.reshape((-1, 3)) * 255).astype(int)
        after_image_pixels = (after_image_jpg.reshape((-1, 3)) * 255).astype(int)
    else: # images are jpgs
        before_image_pixels = before_image_jpg.reshape((-1, 3))
        after_image_pixels = after_image_jpg.reshape((-1, 3))

    # Create the plots
    if equalization_bool:
        fig, axs = plt.subplots(4, 4, figsize=(10,8))
    else:
        fig, axs = plt.subplots(5, 4, figsize=(10,10))

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

    # After Image Histograms
    image_counts_red1, bins_r1, _ = axs[1, 1].hist(after_image_pixels[:, 0], bins=bin_edges, color='red', alpha=0.5, label='Red')
    image_counts_green1, bins_g1, _ = axs[1, 2].hist(after_image_pixels[:, 1], bins=bin_edges, color='green', alpha=0.5, label='Red')
    image_counts_blue1, bins_b1, _ = axs[1, 3].hist(after_image_pixels[:, 2], bins=bin_edges, color='blue', alpha=0.5, label='Red')


    if equalization_bool:
        num_bins = 10

        # Before Image
        new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, equalized_before_image = equalize(before_image_str, output_before_image_str, save_to_a_file_bool)
        if create_plots_bool:
            axs[2,1].hist(new_pixel_vals_red, bins=num_bins, color='red', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
            axs[2,2].hist(new_pixel_vals_green, bins=num_bins, color='green', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
            axs[2,3].hist(new_pixel_vals_blue, bins=num_bins, color='blue', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)
            axs[2, 0].set_title('Equalized Before Image')
            axs[2, 0].imshow(equalized_before_image)

        # After Image
        new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, equalized_after_image = equalize(after_image_str, output_after_image_str, save_to_a_file_bool)
        if create_plots_bool:
            axs[3,1].hist(new_pixel_vals_red, bins=num_bins, color='red', alpha=0.5, label='Red', weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
            axs[3,2].hist(new_pixel_vals_green, bins=num_bins, color='green', alpha=0.5, label='green', weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
            axs[3,3].hist(new_pixel_vals_blue, bins=num_bins, color='blue', alpha=0.5, label='blue', weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)
            axs[3, 0].set_title('Equalized After Image')
            axs[3, 0].imshow(equalized_after_image)
        num_rows = 4

    else: # Matching
        new_pixel_vals_red, new_pixel_vals_green, new_pixel_vals_blue, matched_after_image = match(before_image_str,
                                                                                                       after_image_str, output_after_image_str, save_to_a_file_bool)
        if create_plots_bool:
            axs[4, 0].set_title('Matched After Image')
            axs[4, 0].imshow(matched_after_image)

            num_bins = 256
            bin_edges = np.arange(0, 255 + 2, 1)
            axs[4, 1].hist(new_pixel_vals_red, bins=bin_edges, color='red', alpha=0.5, label='Red',
                           weights=np.ones_like(new_pixel_vals_red) / 256 * num_bins)
            axs[4, 2].hist(new_pixel_vals_green, bins=bin_edges, color='green', alpha=0.5, label='Red',
                           weights=np.ones_like(new_pixel_vals_green) / 256 * num_bins)
            axs[4, 3].hist(new_pixel_vals_blue, bins=bin_edges, color='blue', alpha=0.5, label='Red',
                           weights=np.ones_like(new_pixel_vals_blue) / 256 * num_bins)
            num_rows = 5
    if create_plots_bool:
        maximum_count = max(max(image_counts_red), max(image_counts_green), max(image_counts_blue), max(image_counts_red1), max(image_counts_green1), max(image_counts_blue1))
        # Remove ticks from images and set the y limit for the histograms for all graphs
        for i in range(num_rows):
            axs[i, 0].set_xticks([])
            axs[i, 0].set_yticks([])
            for j in range(3):
                if not(matching_bool and (i == 2 or i == 3)): # If they are not cumulative histograms
                    axs[i, j + 1].set_ylim(0, maximum_count)

        # Change formatting of histograms to show axes
        for i in range(num_rows):
            for j in range(3):
                if show_axes_bool:
                    axs[i, j + 1].set_ylabel('Frequency')
                    axs[i, j + 1].set_xlabel('Brightness')
                else:
                    axs[i,  j + 1].set_yticks([])
                    axs[i, j + 1].set_xticks([])

        plt.tight_layout()
        if create_plots_bool:
            plt.show()

elif directory_bool:
    if directory_str == '':
        print('Specify the first save directory in order to save files')
    elif equalization_bool:
        print('Equalizing directory:', directory_str)
        image_names = os.listdir(directory_str)
        print('Equalizing', len(image_names), 'images', image_names)
        for image_name in image_names:
            # print(image_name)
            equalize(directory_str + '/' + image_name, first_save_directory_str + '/' + image_name, True)
            plt.close('all')
        if second_directory_str !='':
            if second_save_directory_str == '':
                print('Please specify a second save directory')
            else:
                print('\nEqualizing directory:', second_directory_str)
                image_names = []
                image_names = os.listdir(second_directory_str)
                print('Equalizing', len(image_names), 'images', image_names)
                for image_name in image_names:
                    equalize(second_directory_str + '/' + image_name, second_save_directory_str + '/' + image_name, True)
                    plt.close('all')
        if third_directory_str !='':
            if third_save_directory_str == '':
                print('Please specify a third save directory')
            else:
                print('\nEqualizing directory:', third_directory_str)
                image_names = []
                image_names = os.listdir(third_directory_str)
                print('Equalizing', len(image_names), 'images', image_names)
                for image_name in image_names:
                    # print(image_name)
                    equalize(third_directory_str + '/' + image_name, third_save_directory_str + '/' + image_name, True)
                    plt.close('all')
    elif matching_bool:
        print('Matching the second directory to the first directory.')
        print('Matching directory', second_directory_str, 'to', directory_str, '\b.')
        print('Creating new files at', first_save_directory_str)
        image_names = os.listdir(second_directory_str)
        print('List of images to try to be matched:', len(image_names), image_names)
        image_names_to_compare = os.listdir(directory_str)
        print('List of comparison images', len(image_names_to_compare), image_names_to_compare)
        list_of_unmatched_images = []
        for image_name in image_names:
            before_full_file_name = directory_str + '/' + image_name
            after_full_file_name = second_directory_str + '/' + image_name
            after_full_file_save_name = first_save_directory_str + '/' + image_name
            if image_name in image_names_to_compare:

                match(before_full_file_name, after_full_file_name, after_full_file_save_name, True)
                plt.close('all')
            else:
                list_of_unmatched_images += [image_name]
        if len(list_of_unmatched_images) > 0: # If there are unmatched images
            print('List of unmatched images in the folder:', directory_str, list_of_unmatched_images)
        if third_directory_str!= '':
            if third_save_directory_str != '':
                print('Matching three folders will only use two output directories.')
            if second_save_directory_str != '':
                print('\nMatching the third directory to the first directory.')
                print('Matching directory', third_directory_str, 'to', directory_str, '\b.')
                print('Creating new files at', second_save_directory_str)
                image_names = os.listdir(third_directory_str)
                print('List of images to be matched:', image_names)
                image_names_to_compare = os.listdir(directory_str)
                print('List of comparison images', image_names_to_compare)
                list_of_unmatched_images = []

                for image_name in image_names:
                    before_full_file_name = directory_str + '/' + image_name
                    after_full_file_name = third_directory_str + '/' + image_name
                    after_full_file_save_name = second_save_directory_str + '/' + image_name
                    if image_name in image_names_to_compare:
                        match(before_full_file_name, after_full_file_name, after_full_file_save_name, True)
                        plt.close('all')
                    else:
                        list_of_unmatched_images += [image_name]
                if len(list_of_unmatched_images) > 0:
                    print('List of unmatched images', list_of_unmatched_images)
                    print('\nMatching the unmatched images from the third directory to the second directory.')
                    print('Matching directory', third_directory_str, 'to', second_directory_str, '\b. Creating new files at',
                          second_save_directory_str)
                    image_names = os.listdir(third_directory_str)
                    print('List of images to be matched:', list_of_unmatched_images)
                    image_names_to_compare = os.listdir(second_directory_str)
                    print('List of comparison images', image_names_to_compare)
                    before_full_file_name = second_directory_str + '/' + image_name
                    after_full_file_name = third_directory_str + '/' + image_name
                    after_full_file_save_name = second_save_directory_str + '/' + image_name

                    for image_name in list_of_unmatched_images:
                        if image_name in image_names_to_compare:
                            match(before_full_file_name, after_full_file_name, after_full_file_save_name, True)
                            list_of_unmatched_images.remove(image_name)
                    if len(list_of_unmatched_images) > 0:
                        print('List of unmatched images in third directory:', list_of_unmatched_images)
            else:
                print('\nPlease specify a second directory to save files to so that the third folder can be matched to the first folder')
else:
    print('Please select either two files or directory matching')
print('Program Finished')
