
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

def compile(file_of_names):
    print("\n\n**********Compiling....********************\n\n")
    # after run, compile
    file_of_names = file_of_names.strip()
    os.system("cd src && ffmpeg -f concat -i " + str(file_of_names) +  " -c copy output.mkv && cd ..")
    print("\n\n**********Done!********************\n\n")

def trim_vid(input_file, output_file, start_time, duration):
    
    input_file = input_file.strip()
    output_file = output_file.strip()
    start_time = start_time.strip()
    duration = duration.strip()

    os.system("ffmpeg -i " +  str(input_file) + " -ss " + str(start_time) + " -t " + str(duration) + " -c copy " + str(output_file))


#trim_vid("run.mkv", "out.mkv" , "00:00:05", "00:00:05")