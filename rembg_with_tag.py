import cv2
import os
from os import path
from PIL import Image, ImageFont, ImageDraw  
from PIL import UnidentifiedImageError
from transparent_background import Remover
from tqdm import tqdm

remover = Remover()

def find_empty_space(img, threshold=400):

    # img = Image.open(image_path)
    width, height = img.size

    empty_space_coordinates = []

    for x in range(width):
        for y in range(height):
            pixel_value = sum(img.getpixel((x, y)))
            if pixel_value in range(390,394):
                empty_space_coordinates.append((x, y))
    x = min([i[0] for i in empty_space_coordinates[:10]])
    y = max([i[1] for i in empty_space_coordinates[:10]])
    return x,y

# Input and Output directories
inp_dir_paths = [r"C:\Users\Rahul\Desktop\Background remove\trial_bg_tag"]

for inp_dir_path in inp_dir_paths:
    inp_dir = os.listdir(inp_dir_path)

    # Create an output directory with "_BG_REMOVED" added to the input directory path
    out_dir_path = inp_dir_path + "_BG_REMOVED"
    os.makedirs(out_dir_path, exist_ok=True)

    for i in tqdm(inp_dir):
        if i.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Define the path to the image
            img_path = os.path.join(inp_dir_path, i)
            file_name = os.path.basename(img_path)
            name, file_extension = os.path.splitext(file_name)
            try:
                # Load the image directly using PIL
                with Image.open(img_path).convert('RGB') as img:
                    # If width is less than height, then the image is vertical
                    if img.width < img.height:
                        # Rotate the image by 90 degrees to make it horizontal
                        img_rotated = img.rotate(-90, expand=True)
                        img_rotated.save(img_path)
                        img = img_rotated
                    else:
                        pass

                    # Resize the image
                    img = img.resize((640, 480), Image.LANCZOS)
                    
                out = remover.process(img, type="[37, 102, 255]")
                
                x,y = find_empty_space(out)
                
                I1 = ImageDraw.Draw(out)
                myFont = ImageFont.truetype(r"C:\Users\Rahul\Desktop\Background remove\arial\arial.ttf", 30)
                I1.text((x, y), name,font=myFont, fill=(255, 255, 255))
                out.save(os.path.join(out_dir_path, i))
            except (IOError, OSError, UnidentifiedImageError) as e:
                print(f"Error processing image {img_path}: {e}")