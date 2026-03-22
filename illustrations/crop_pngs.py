#!/usr/bin/env python3
"""Crop PNG files to remove excess whitespace around diagram content."""

from PIL import Image
from pathlib import Path

def crop_png(image_path, margin=20):
    """
    Crop PNG to bounding box of non-white content with margin.
    
    Args:
        image_path: Path to PNG file
        margin: Pixels to keep around content (default 20)
    
    Returns:
        True if cropped, False if no changes needed
    """
    img = Image.open(image_path)
    
    # Convert to RGB if RGBA
    if img.mode == 'RGBA':
        img_rgb = Image.new('RGB', img.size, (255, 255, 255))
        img_rgb.paste(img, mask=img.split()[3])
        img = img_rgb
    
    # Get image data
    pixels = img.load()
    width, height = img.size
    
    # Find bounding box of non-white pixels (with tolerance for near-white)
    left, top, right, bottom = width, height, 0, 0
    threshold = 240  # Consider pixels with value > threshold as "white"
    
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            # Check if pixel is significantly non-white
            if isinstance(pixel, tuple):
                # RGB or RGBA
                if not all(val > threshold for val in pixel[:3]):
                    left = min(left, x)
                    top = min(top, y)
                    right = max(right, x)
                    bottom = max(bottom, y)
            else:
                # Grayscale
                if pixel <= threshold:
                    left = min(left, x)
                    top = min(top, y)
                    right = max(right, x)
                    bottom = max(bottom, y)
    
    # Add margin if content was found
    if left < width and top < height:
        left = max(0, left - margin)
        top = max(0, top - margin)
        right = min(width, right + margin)
        bottom = min(height, bottom + margin)
        
        # Check if crop is meaningful (not already the whole image)
        crop_box = (left, top, right, bottom)
        if crop_box != (0, 0, width, height):
            cropped = img.crop(crop_box)
            cropped.save(image_path)
            old_size = width * height
            new_size = (right - left) * (bottom - top)
            reduction = ((old_size - new_size) / old_size) * 100
            print(f"✓ {Path(image_path).name:50} | {width:4}×{height:4} → {right-left:4}×{bottom-top:4} ({reduction:5.1f}% reduction)")
            return True
        else:
            print(f"- {Path(image_path).name:50} | No significant whitespace to crop")
            return False
    else:
        print(f"- {Path(image_path).name:50} | No content detected")
        return False

# Process all PNGs in exports folder
REPO_ROOT = Path(__file__).resolve().parents[1]
export_dir = REPO_ROOT / "exports"
png_files = sorted(export_dir.glob('*.png'))

if png_files:
    print(f"\nCropping {len(png_files)} PNG files...\n")
    cropped_count = 0
    for png_file in png_files:
        if crop_png(str(png_file)):
            cropped_count += 1
    print(f"\n✓ Successfully cropped {cropped_count}/{len(png_files)} files")
else:
    print("No PNG files found in exports folder")
