## MakeItTalk Model
### We have tried makeittalk model and installed all the required dependencies using the commands provided in the readme file https://github.com/yzhou359/MakeItTalk.
Steps followed to execute the model
1. We have created a conda environment makeittalk_env using the command: conda create -n makeittalk_env python=3.6
and starting the conda activate makeittalk_env
![conda env](https://user-images.githubusercontent.com/112770055/223622691-c13342dd-423f-4860-80e4-8a8bcaef3084.jpg)

2. We have installed ffmpeg from this website and added to the environment variables
3. We have installed the required dependencies 
   * ffmpeg-python
   * opencv-python
   * face_alignment
   * scikit-learn
   * pydub
   * pynormalize
   * soundfile
   * librosa
   * pysptk
   * pyworld
   * resemblyzer
![requirements](https://user-images.githubusercontent.com/112770055/223622729-c54a4880-2aae-4e17-bd12-694df74f62fb.jpg)
4. We have installed CUDA as well to run the model using the local system GPU
5. We have run the the model using the command python main_end2end.py --jpg anne.jpg(We have used CPU instead of CUDA as we are facing issues with connecting CUDA).
![output1](https://user-images.githubusercontent.com/112770055/223630509-6c54904a-f928-4b97-93f6-a7ecfd3a6146.jpg)
![finaloutput](https://user-images.githubusercontent.com/112770055/223630256-65f8c461-bfc1-47dd-ad47-def82b54d530.jpg)
It generated a new video file with anne image and the example audio
https://user-images.githubusercontent.com/112770055/223630321-28b1603a-dd6f-4cf5-b47b-b1d62f52a939.mp4

