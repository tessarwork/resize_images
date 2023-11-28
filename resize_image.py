from PIL import Image
import os, sys

def resize_image(input_path, output_folder, sizes): 
    if not os.path.exists(output_folder): 
        os.makedirs(output_folder)

    input_image = Image.open(input_path)

    for i, size in enumerate(sizes): 
        width, height = input_image.size
        aspect_ratio = width / height
        new_width = size
        new_height = int(size / aspect_ratio)

        resized_image = input_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        output_path = os.path.join(output_folder, f"resized_{i+1}.jpg")
        resized_image.save(output_path)

input_image_path = "Ronaldo Original .jpg"
output_folder_path = "resized_path"
sizes = [485, 480, 475, 470, 465, 460, 455, 450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400, 395, 390, 385, 380, 375, 370, 365, 360, 355, 350, 345, 340, 335, 330, 325, 320, 315, 310, 305, 300, 295, 290, 285, 280, 275, 270, 265, 260, 255, 250, 245, 240, 235, 230, 225, 220, 215, 210, 205]


resize_image(input_image_path, output_folder_path, sizes)

    
