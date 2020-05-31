import os
import shutil
from detect import detect
import edit

if os.path.exists("out"):
    shutil.rmtree("out")
os.mkdir("out")

# then combine links
all_output_file = "output.mkv"
path_all_output_file = os.path.join("out", all_output_file)

if os.path.exists(path_all_output_file):
    os.remove(path_all_output_file)

with open(os.path.join("out", "files.txt"), "w") as text_file:
    for r, d, f in os.walk("src"):
        for file in f:

            video_path = os.path.join(r, file)

            out_path_global = os.path.join("out", file)

            if video_path.endswith(".mkv"):

                print(file)

                # times = detect(0)
                times = detect(video_path, False)
                print(times)

                count = 1
                for time in times:

                    start = time["start"]
                    duration = time["duration"]

                    output_file = out_path_global.replace(".", "_" + str(count) + ".")

                    edit.trim_vid(
                        video_path, output_file, str(start), str(duration),
                    )

                    if output_file.endswith(".mkv") and not (
                        output_file.endswith(all_output_file)
                    ):

                        print(output_file)

                        text_file.write(
                            "file '" + output_file[len("out") + 1 :] + "' \n"
                        )

                    count += 1

edit.compile("files.txt", "out")
