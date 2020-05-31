import os
import shutil
from detect import detect
import edit

if os.path.exists("out"):
    shutil.rmtree("out")
    os.mkdir("out")

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
                end = time["end"]

                output_file = out_path_global.replace(".", "_" + str(count) + ".")

                edit.trim_vid(
                    video_path, output_file, str(start), str(end),
                )

                print("Start: " + str(start))

                count += 1
