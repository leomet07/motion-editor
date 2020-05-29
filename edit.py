"""
from moviepy.editor import *
import os

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip(os.path.join("src", "hand.mp4"))

# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)



# Overlay the text clip on the first video clip


# Write the result to a file (many options available !)
clip.write_videofile("myHolidays_edited.mp4")
"""

from moviepy.editor import *

clips = []
for r, d, f in os.walk("src"):
    for file in f:

        video_path = os.path.join(r, file)

        if video_path.endswith(".mp4"):
            print(video_path)

            vid = VideoFileClip(video_path)
            vid = vid.resize((460, 720))
            clips.append(vid)


final_clip = concatenate_videoclips(clips)

# You can write any format, in any quality.
final_clip.write_videofile("final.mp4")
