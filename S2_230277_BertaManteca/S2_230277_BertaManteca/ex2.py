import subprocess

class VideoAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def create_new_bbb_container(self):
        # Cut BBB into 50 seconds video
        cut_output_file = 'EX2 videocortado_50s.mp4'
        cmd_cut = [
            'ffmpeg',
            '-i', self.input_file,
            '-ss', '00:00:00',
            '-t', '00:00:50',
            '-c', 'copy',
            cut_output_file
        ]
        subprocess.run(cmd_cut, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Export BBB(50s) audio as MP3 mono track
        mp3_mono_output_file = 'EX2 videocortado_50s_mono.mp3'
        cmd_mp3_mono = [
            'ffmpeg',
            '-i', cut_output_file,
            '-vn', '-ac', '1',
            '-q:a', '2',
            mp3_mono_output_file
        ]
        subprocess.run(cmd_mp3_mono, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Export BBB(50s) audio in MP3 stereo w/ lower bitrate
        mp3_stereo_output_file = 'EX2 videocortado_50s_stereo_lowbitrate.mp3'
        cmd_mp3_stereo_lowbitrate = [
            'ffmpeg',
            '-i', cut_output_file,
            '-vn', '-ac', '2', '-b:a', '64k',
            '-q:a', '2',
            mp3_stereo_output_file
        ]
        subprocess.run(cmd_mp3_stereo_lowbitrate, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Export BBB(50s) audio in AAC codec
        aac_output_file = 'EX2 Videocortado_50s_aac.aac'
        cmd_aac = [
            'ffmpeg',
            '-i', cut_output_file,
            '-vn', '-c:a', 'aac',
            aac_output_file
        ]
        subprocess.run(cmd_aac, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Package everything into an MP4 with FFMPEG
        mp4_output_file = 'EX2 videocortado_50s_final.mp4'
        cmd_mp4 = [
            'ffmpeg',
            '-i', cut_output_file,
            '-i', mp3_mono_output_file,
            '-i', mp3_stereo_output_file,
            '-i', aac_output_file,
            '-c', 'copy',
            mp4_output_file
        ]
        subprocess.run(cmd_mp4, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def ejecutar():
    input_file = 'BigBuckBunny_512kb.mp4'
    output_file = 'EX2 videofinal.mp4'

    video_analyzer = VideoAnalyzer(input_file, output_file)
    video_analyzer.create_new_bbb_container()

if __name__ == "__main__":
    ejecutar()






