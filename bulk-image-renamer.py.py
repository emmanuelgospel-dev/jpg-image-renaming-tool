import os

def rename_images():
    folder = input("Enter folder path: ").strip()
    
    if not os.path.isdir(folder):
        print("Invalid folder path.")
        return

    # Include both .jpg and .jpeg
    images = [f for f in os.listdir(folder) 
              if f.lower().endswith((".jpg", ".jpeg"))]
    images.sort()

    # Optional: cap at 50
    images = images[:50]

    for index, file in enumerate(images, start=1):
        new_name = f"IMG{index:02}.jpg"
        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, new_name)

        if os.path.exists(new_path):
            print(f"Skipping: {new_name} already exists.")
            continue

        os.rename(old_path, new_path)
        print(f"Renamed: {file} -> {new_name}")

    print("Renaming completed.")

if __name__ == "__main__":
    rename_images()