import subprocess
import os

class VideoSubtitlesProcessor:
    def __init__(self, input_video, output_video):
        self.input_video = input_video
        self.output_video = output_video

    def download_subtitles(self, output_subtitle_file):
        cmd_download_subtitles = [
            'ffmpeg',
            '-i', self.input_video,
            '-map', '0:s:0',  # Select the first subtitle stream
            '-c:s', 'srt',
            output_subtitle_file
        ]
        result = subprocess.run(cmd_download_subtitles, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print(f"Subtitle download failed. Error: {result.stderr.decode('utf-8')}")

    def integrate_subtitles(self, input_subtitle_file):
        cmd_integrate_subtitles = [
            'ffmpeg',
            '-i', self.input_video,
            '-vf', f'subtitles={input_subtitle_file}',
            '-c:a', 'copy',
            '-t', '50',  # Cut the video to 50 seconds
            self.output_video
        ]
        result = subprocess.run(cmd_integrate_subtitles, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print(f"Subtitle integration failed. Error: {result.stderr.decode('utf-8')}")

def ejecutar():
    input_video = 'LionelMessi.mp4'
    output_video = 'EX4_output_video_with_subtitles.mp4'
    subtitle_file = 'subtitles.srt'

    video_processor = VideoSubtitlesProcessor(input_video, output_video)
    video_processor.download_subtitles(subtitle_file)
    video_processor.integrate_subtitles(subtitle_file)

if __name__ == "__main__":
    ejecutar()




