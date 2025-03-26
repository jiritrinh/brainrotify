import ffmpeg
import os
import subprocess
from pathlib import Path



video_file = "brainrot_video.mp4"
audio_file = "speech.mp3"
subtitles =  "subtitles.srt"

 

def create_video(video_file, audio_file, subtitles):
    
    video_path = str(Path(__file__).parent / video_file)  
    audio_path = str(Path(__file__).parent / audio_file)  
    subtitles_path = str(Path(__file__).parent / subtitles)
    
    cmd = f"""
        ffmpeg -i {video_path} -i {audio_path} \
        -filter_complex \
        "[0:v]subtitles='{subtitles_path}':force_style='\
        FontName=Impact,\
        Fontsize=24,\
        PrimaryColour=&HFFFFFF&,\
        Alignment=10'[v]; \
        [1:a]volume=1.5,afade=t=in:st=0:d=0.5[a] \
        " \
        -map "[v]" -map "[a]" \
        -c:v libx264 -preset fast -crf 22 \
        -c:a aac -b:a 192k \
        -movflags +faststart \
        -y output_first.mp4
        """
    subprocess.run(cmd, shell=True)  
        




