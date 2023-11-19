import subprocess

class VideoHistogramProcessor:
    def __init__(self, input_video, output_video):
        self.input_video = input_video
        self.output_video = output_video

    def equalize_histogram_video(self):
        cmd_equalize_histogram = [
            'ffmpeg',
            '-i', self.input_video,
            '-vf', 'eq=histogram=stretch',
            '-c:a', 'copy',
            '-y',
            self.output_video
        ]
        subprocess.run(cmd_equalize_histogram, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def ejecutar():
    input_video = 'LionelMessi.mp4'
    output_video = 'EX6_output_video_with_histogram.mp4'

    video_processor = VideoHistogramProcessor(input_video, output_video)
    video_processor.equalize_histogram_video()

if __name__ == "__main__":
    ejecutar()


