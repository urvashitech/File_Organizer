import os
import shutil 


file_types = {
    "Images" : [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "PDFs":      [".pdf"],
    "Videos":    [".mp4", ".mkv", ".avi", ".mov"],
    "Music":     [".mp3", ".wav", ".aac"],
    "Documents": [".docx", ".txt", ".xlsx", ".pptx"],
    "Archives":  [".zip", ".rar", ".tar"],
}
folder = "C:/Users/urvas/Downloads"

for file in os.listdir(folder) :
    print("Processing:", file)
    file_path = os.path.join(folder,file)
    print(file_path)
    if not os.path.isfile(file_path):
        continue
    
    name,ext = os.path.splitext(file)
    ext = ext.lower()
    print(file, ext) 
    moved = False

    for folder_name, extensions in file_types.items():
        if ext in extensions:
            destination = os.path.join(folder, folder_name) 
            os.makedirs(destination, exist_ok=True)  
            shutil.move(file_path, os.path.join(destination, file)) 
            print(f"✅ Moved: {file} → {folder_name}/") 
            moved = True 
            break 
        if not moved: 
            print(f"⚠️ Skipped: {file} (unknown type)") 
            print("\n🎉 Done! Your folder is now organized.")