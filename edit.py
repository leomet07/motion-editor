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

clips = [
    VideoFileClip(os.path.join("src", "example_01.mp4")),
    VideoFileClip(os.path.join("src", "example_02.mp4")),
    VideoFileClip(os.path.join("src", "example_03.mp4")),
]


fade_duration = 0  # 1-second fade-in for each clip
clips = [clip.crossfadein(fade_duration) for clip in clips]

final_clip = concatenate_videoclips(clips, padding=-fade_duration)

# You can write any format, in any quality.
final_clip.write_videofile("final.mp4")
