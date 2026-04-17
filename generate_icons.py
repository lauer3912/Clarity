#!/usr/bin/env python3
from PIL import Image, ImageDraw
import os

os.makedirs('ios/Clarity/Assets.xcassets/AppIcon.appiconset', exist_ok=True)

def create_icon(size, filename):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calm purple gradient
    for y in range(size):
        ratio = y / size
        r = int(124 + (26 - 124) * ratio)
        g = int(106 + (109 - 106) * ratio)
        b = 255
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))
    
    center = size // 2
    radius = int(size * 0.35)
    draw.ellipse([center-radius, center-radius, center+radius, center+radius], 
                 fill=None, outline=(255,255,255,255), width=max(2,size//25))
    inner_r = int(radius * 0.3)
    draw.ellipse([center-inner_r, center-inner_r, center+inner_r, center+inner_r], 
                 fill=(255,255,255,255))
    
    img.save(filename, 'PNG')

sizes = [
    (20, 'Icon-20@1x.png'),
    (40, 'Icon-20@2x.png'),
    (60, 'Icon-20@3x.png'),
    (29, 'Icon-29@1x.png'),
    (58, 'Icon-29@2x.png'),
    (87, 'Icon-29@3x.png'),
    (40, 'Icon-40@1x.png'),
    (80, 'Icon-40@2x.png'),
    (120, 'Icon-40@3x.png'),
    (76, 'Icon-76@1x.png'),
    (152, 'Icon-76@2x.png'),
    (167, 'Icon-83.5@2x.png'),
    (1024, 'Icon-1024@1x.png'),
]

for size, name in sizes:
    create_icon(size, f'ios/Clarity/Assets.xcassets/AppIcon.appiconset/{name}')
    print(f'Created {name}')

print('Done!')
