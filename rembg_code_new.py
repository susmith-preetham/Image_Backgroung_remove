import cv2
import os
from PIL import Image
from PIL import UnidentifiedImageError
from transparent_background import Remover
from tqdm import tqdm

remover = Remover()

# Input and Output directories
inp_dir_paths = [r"D:\D_drive\BG_remove_new\New folder (6)"]

for inp_dir_path in inp_dir_paths:
    inp_dir = os.listdir(inp_dir_path)

    # Create an output directory with "_BG_REMOVED" added to the input directory path
    out_dir_path = inp_dir_path + "_BG_REMOVED"
    os.makedirs(out_dir_path, exist_ok=True)

    for i in tqdm(inp_dir):
        if i.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Define the path to the image
            img_path = os.path.join(inp_dir_path, i)
            
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
                out.save(os.path.join(out_dir_path, i))
            except (IOError, OSError, UnidentifiedImageError) as e:
                print(f"Error processing image {img_path}: {e}")