
import os
import sys

# cd src && ffmpeg -f concat -i files.txt -c copy output.mkv && cd ..

clips = []



def compile(file_of_names, direc):
    print("\n\n**********Compiling....********************\n\n")
    # after run, compile
    file_of_names = file_of_names.strip()
    direc = direc.strip()
    os.system("cd out && ffmpeg -f concat -i " + str(file_of_names) +  " -c copy output.mkv && cd ..")
    print("\n\n**********Done!********************\n\n")

def trim_vid(input_file, output_file, start_time, duration):
    
    input_file = input_file.strip()
    output_file = output_file.strip()
    start_time = start_time.strip()
    duration = duration.strip()

    os.system("ffmpeg  -i " +  str(input_file) + " -ss " + str(start_time) + " -t " + str(duration) + " -c copy " + str(output_file))


#trim_vid("run.mkv", "out.mkv" , "00:00:05", "00:00:05")