import cv2
import numpy as np
import subprocess

class VideoAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.cut_output_file = 'EX1 videocortado_9s.mp4'  # Add this line

    def generate_macroblocks_and_vectors_video(self):
        # Cut the video 9s
        cmd_cut = [
            'ffmpeg',
            '-i', self.input_file,
            '-ss', '00:00:00',
            '-t', '00:00:9',  # Fix the time format here
            '-c', 'copy',
            self.cut_output_file  # Use the instance variable here
        ]
        subprocess.run(cmd_cut, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cap = cv2.VideoCapture(self.cut_output_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter(self.output_file, fourcc, fps, (width, height))

        # Parameters for Dense Optical Flow
        params = {
            'pyr_scale': 0.5,
            'levels': 3,
            'winsize': 7,
            'iterations': 3,
            'poly_n': 5,
            'poly_sigma': 1.2,
            'flags': 0
        }

        prev_frame = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if prev_frame is not None:
                # Convert frames to grayscale
                prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # Calculate Dense Optical Flow
                flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, **params)

                # Draw motion vectors on the frame
                for y in range(0, height, 16):
                    for x in range(0, width, 16):
                        dx, dy = flow[y, x]
                        cv2.arrowedLine(frame, (x, y), (int(x + dx), int(y + dy)), (0, 0, 255), 1)

            macroblock_size = 16
            for y in range(0, height, macroblock_size):
                for x in range(0, width, macroblock_size):
                    cv2.rectangle(frame, (x, y), (x + macroblock_size, y + macroblock_size), (255, 255, 255), 1)

            out.write(frame)
            prev_frame = frame

        cap.release()
        out.release()
        cv2.destroyAllWindows()


def ejecutar():
    input_file = 'BigBuckBunny_512kb.mp4'
    output_file = 'EX1 output_with_macroblocks_and_vectors.mp4'

    video_analyzer = VideoAnalyzer(input_file, output_file)
    video_analyzer.generate_macroblocks_and_vectors_video()

if __name__ == "__main__":
    ejecutar()

