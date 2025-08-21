from PIL import Image, ImageFilter

def apply_filter(input_path, output_path, filter_type="BLUR"):
    img = Image.open(input_path)
    if filter_type == "BLUR":
        img = img.filter(ImageFilter.BLUR)
    elif filter_type == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)
    img.save(output_path)
    print(f"Filtered image saved to {output_path}")

# Example usage
apply_filter("input.jpg", "output.jpg", filter_type="BLUR")
