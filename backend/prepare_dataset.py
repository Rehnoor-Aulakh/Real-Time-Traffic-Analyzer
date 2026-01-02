import os
import random
import shutil

SOURCE_DIR = "Fully_annotate"
OUTPUT_DIR = "traffic_dataset"

image_paths=[]

for root,dirs,files in os.walk(SOURCE_DIR):
    for file in files:
        if file.lower().endswith(".jpg"):
            full_path=os.path.join(root,file)
            image_paths.append(full_path)

print(f"Total images found: {len(image_paths)}")

random.shuffle(image_paths)

print("Sample shuffled images:")
for path in image_paths[:5]:
    print(path)

print("Copying images into traffic_dataset...")

print("Copying images into traffic_dataset...")

for idx, src_path in enumerate(image_paths, start=1):
    filename = f"img_{idx:06d}.jpg"
    dst_path = os.path.join(OUTPUT_DIR, filename)

    shutil.copy(src_path, dst_path)

print(f"Dataset prepared successfully with {len(image_paths)} images.")