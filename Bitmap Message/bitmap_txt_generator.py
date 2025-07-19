from PIL import Image

# ASCII characters from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.5)  # Adjust for terminal aspect ratio
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")  # Convert to grayscale

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''.join([ASCII_CHARS[pixel // 25] for pixel in pixels])  # 0–255 mapped to 0–10
    return ascii_str

def convert_image_to_ascii(path, new_width=100):
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    image = resize_image(image, new_width)
    image = grayify(image)
    
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = "\n".join([ascii_str[i:i+img_width] for i in range(0, len(ascii_str), img_width)])
    
    return ascii_img

# Example usage:
ascii_art = convert_image_to_ascii("image.bmp", new_width=80)
print(ascii_art)

# Save the ASCII art to a text file
with open("ascii_art.txt", "w") as f:
    f.write(ascii_art)
