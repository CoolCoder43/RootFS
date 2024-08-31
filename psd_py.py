from PIL import Image
from psd_tools import PSDImage

# Step 1: Load the PSD file
psd = PSDImage.open('final.psd')

# Step 2: Create a base image with the specified dimensions
base_image_width = psd.width  # Example width
base_image_height = psd.height  # Example height
base_image = Image.new('RGB', (base_image_width, base_image_height), (255, 255, 255))  # White background
image = Image.open('pvc_card.png')

# Step 3: Iterate through the PSD layers and place them on the base image
for layer in psd:
    if layer.is_group():
        continue  # Skip groups if necessary
    if layer.visible:
        # Get the layer image, position, and size
        # layer_image = layer.composite()
        layer_position = (layer.left, layer.top)
        layer_size = (layer.width, layer.height)

        # Resize the layer image to its specified dimensions (if needed)
        layer_image = image.resize(layer_size)

        # Paste the layer image onto the base image at the specified coordinates
        base_image.paste(layer_image, layer_position, layer_image)

# Step 4: Save the final image
base_image.save('output_image.png')
