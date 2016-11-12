import os
from moviepy.editor import VideoFileClip


def split_into_images(video_file_path):
    directory = video_file_path.replace('.mp4', '') + '_output/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    clip = VideoFileClip(video_file_path)
    duration = clip.duration
    clip_seconds = range(int(duration))
    for second in clip_seconds:
        m, s = divmod(second, 60)
        h, m = divmod(m, 60)
        time = '%d:%02d:%02d' % (h, m, s)
        clip.save_frame("{}/{}-frame.jpeg".format(directory, second), t=time)


for file in os.listdir("/Users/jed0001k/PycharmProjects/private/video-summarizer/tosplit"):
    if file.endswith(".mp4"):
        split_into_images("/Users/jed0001k/PycharmProjects/private/video-summarizer/tosplit/" + file)
