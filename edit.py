
import os
import sys

# cd src && ffmpeg -f concat -i files.txt -c copy output.mkv && cd ..

clips = []

output_file = "output.mkv"
path_output_file = os.path.join("src", output_file)

if os.path.exists(path_output_file):
    os.remove(path_output_file)


with open(os.path.join("src", "files.txt"), "w") as text_file:
    for r, d, f in os.walk("src"):
        for file in f:

            video_path = os.path.join(r, file)

            if video_path.endswith(".mkv") and not (video_path.endswith(output_file)):

                print(file)

                text_file.write("file '" + file + "' \n")


print("\n\n**********Compiling....********************\n\n")
# after run, compile
os.system("cd src && ffmpeg -f concat -i files.txt -c copy output.mkv && cd ..")
print("\n\n**********Done!********************\n\n")



