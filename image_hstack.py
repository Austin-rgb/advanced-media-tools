from PIL import Image
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

# Open the images
image1 = Image.open(file1)
image2 = Image.open(file2)

# Ensure both images have the same width
def resize_image(image, target_width):
    width, height = image.size
    new_height = int((target_width / width) * height)
    return image.resize((target_width, new_height))

# Find the maximum width
max_width = max(image1.width, image2.width)

# Resize both images to the same width
image1_resized = resize_image(image1, max_width)
image2_resized = resize_image(image2, max_width)

# Determine the total height and create a new blank image
total_height = image1_resized.height + image2_resized.height
new_image = Image.new('RGB', (max_width, total_height))

# Paste the images one below the other
new_image.paste(image1_resized, (0, 0))
new_image.paste(image2_resized, (0, image1_resized.height))

# Save the final image
new_image.save('joined_image_vertical.jpg')

