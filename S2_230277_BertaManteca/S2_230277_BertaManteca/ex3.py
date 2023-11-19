import subprocess
import json

class VideoAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file


    def count_tracks_in_mp4(self):
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-show_entries', 'stream=index',
            '-select_streams', 'v:0',
            '-of', 'json',
            self.input_file
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            # Parse the JSON output to get the track count
            try:
                json_output = json.loads(result.stdout)
                track_count = len(json_output['streams'])
                print(f'The MP4 container contains {track_count} tracks.')
            except json.JSONDecodeError as e:
                print(f'Error decoding JSON: {e}')
        else:
            print(f'Error running ffprobe: {result.stderr}')

def ejecutar():
    input_file = 'BigBuckBunny_512kb.mp4'
    output_file = 'EX3.mp4'

    video_analyzer = VideoAnalyzer(input_file, output_file)
    video_analyzer.count_tracks_in_mp4()

if __name__ == "__main__":
    ejecutar()
