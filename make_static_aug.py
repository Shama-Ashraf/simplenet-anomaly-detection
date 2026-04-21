import os
import random
from PIL import Image
from torchvision import transforms

random.seed(1)

src_dir = "data/sleeve/train/good"
dst_dir = "data_static/sleeve/train/good"

os.makedirs(dst_dir, exist_ok=True)

aug = transforms.Compose([
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomAffine(
        degrees=3,
        translate=(0.01, 0.01),
        scale=(0.99, 1.01)
    )
])

files = sorted([
    f for f in os.listdir(src_dir)
    if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
])

copies_per_image = 2   # 🔥 important

for fname in files:
    path = os.path.join(src_dir, fname)
    img = Image.open(path).convert("RGB")

    base, ext = os.path.splitext(fname)

    # save original
    img.save(os.path.join(dst_dir, fname))

    # create augmented versions
    for i in range(copies_per_image):
        out = aug(img)
        out_name = f"{base}_aug{i}{ext}"
        out.save(os.path.join(dst_dir, out_name))

print("done")
print("original:", len(files))
print("total:", len(files)*(1+copies_per_image))
