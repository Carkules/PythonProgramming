from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_path, output_path, watermark_text):
    """Creates an image with watermark.
    Args:
        input_path (str): path to the original image,
        output_path (str): path to the image with watermark,
        watermark_text (str): text that will appear on watermark.
    
    Returns: image with watermark.
    
    Raises: AnyError: if anything bad happens."""
    
    img = Image.open(input_path)
    width, height = img.size
    watermark_color = (255, 255, 255, 50)
    
    img_watermark = Image.new("RGBA", img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img_watermark)
    
    font_size = 1/6 * width
    font = ImageFont.truetype("arial.ttf", font_size)

    left, top, right, bottom = font.getbbox(watermark_text)
    text_w, text_h = right - left, bottom - top
    x = (width - text_w) // 2
    y = (height - text_h) // 2
    
    draw.text((x, y), watermark_text, fill=(watermark_color), font=font)
    
    img_with_watermark = Image.alpha_composite(img.convert("RGBA"), img_watermark)
    
    img_with_watermark.convert("RGB").save(output_path)