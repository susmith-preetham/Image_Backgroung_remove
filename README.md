In this project, we aim to remove the background of an image and replace it with a solid color. We then add text on the image. We use the 'transparent-background' package to remove the background.
```python
from transparent_background import Remover
remover = Remover()
img = remover.process(img, type="[37, 102, 255]")
img.save("image_path")
This is the basic use of 'transparent-background'.
