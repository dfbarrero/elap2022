import os, shutil
from PIL import Image

def move_files():
    folder = os.getcwd()
    # count increase by 1 in each iteration
    # iterate all files from a directory
    for class_name in os.listdir(folder)[1:]:
        print("class name " + class_name)
        count = 1
        for subfolder in os.listdir(folder+"/"+class_name):
            print("...subfolder name " + subfolder+"/"+class_name)
            for file_name in os.listdir(folder+"/"+class_name+"/"+subfolder):
                print("......file name " + file_name)
                # Construct old file name
                source = folder + "/" + class_name + "/" + subfolder +  "/" + file_name
                # Adding the count to the new file name and extension
                file_type = file_name.split(".")[1]
                destination = folder +  "/" + class_name +  "/" + str(count) + "." + file_type
                # Renaming the file
                os.rename(source, destination)
                count += 1

def resize():
    folder = os.getcwd()
    for class_name in os.listdir(folder)[1:]:
        print("class name " + class_name)
        for file_name in os.listdir(folder+"/"+class_name):
            print("...file name "+"/"+folder+"/"+class_name+"/"+file_name)
            width = 180
            height = 180
            path = folder+"/"+class_name+"/"+file_name
            try:
                img = Image.open(path)
                img = img.resize((width, height), Image.ANTIALIAS)
                img.save(path)
            except:
                print("xxxfile name "+"/"+folder+"/"+class_name+"/"+file_name)
                os.remove(path)

def make_subset(subset_name, start_index, end_index):
    folder = os.getcwd()
    for category in ("Comic", "Manga"):
        dir = folder+"/"+subset_name+"/"+category+"/"
        for file_type in [".png",".jpg"]:
            fnames = [f"{folder}/{category}/{i}"+file_type for i in range(start_index, end_index)]
            for fname in fnames:
                print("..."+fname)
                print(dir)
                try:
                    shutil.copy(fname,dir)
                except:
                    print("xxx"+fname)

def make_subsets():
    make_subset("train", start_index=1, end_index=2000)
    make_subset("validation", start_index=2000, end_index=3000)
    make_subset("test", start_index=3000, end_index=4347)

make_subsets()