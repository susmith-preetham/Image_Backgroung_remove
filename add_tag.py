from PIL import Image, ImageFont, ImageDraw  
from os import path
import os
from tqdm import tqdm
def find_empty_space(image_path, threshold=400):

    img = Image.open(image_path)
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

# Example usage
target = r"C:\\Users\\Gopi\\Desktop\\New folder (7) OUTPUT\\"
names_list2 = os.listdir(r"C:\Users\Gopi\Desktop\New folder (7) OUTPUT")
for path_name in tqdm(names_list2):
    image_path = target+path_name
    empty_space_coords = find_empty_space(image_path)
    name,ext = path.splitext(path_name)
    img = Image.open(image_path)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 30)
    I1.text((x, y), name,font=myFont, fill=(255, 255, 255))
# img.show()
    img.save(image_path)
# print("Empty space coordinates:", empty_space_coords)
