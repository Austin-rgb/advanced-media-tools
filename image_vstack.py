from PIL import Image
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

# Open the images
image1 = Image.open(file1)
image2 = Image.open(file2)

# Ensure both images have the same height
def resize_image(image, target_height):
    width, height = image.size
    new_width = int((target_height / height) * width)
    return image.resize((new_width, target_height))

# Find the maximum height
max_height = max(image1.height, image2.height)

# Resize both images to the same height
image1_resized = resize_image(image1, max_height)
image2_resized = resize_image(image2, max_height)

# Determine the total width and create a new blank image
total_width = image1_resized.width + image2_resized.width
new_image = Image.new('RGB', (total_width, max_height))

# Paste the images into the new image
new_image.paste(image1_resized, (0, 0))
new_image.paste(image2_resized, (image1_resized.width, 0))

# Save the final image
new_image.save('joined_image_resized.jpg')

