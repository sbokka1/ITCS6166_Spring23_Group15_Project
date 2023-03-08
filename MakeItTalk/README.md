## MakeItTalk Model
### We have tried makeittalk model and installed all the required dependencies using the commands provided in the readme file https://github.com/yzhou359/MakeItTalk.
Steps followed to execute the model
1. We have created a conda environment makeittalk_env using the command: conda create -n makeittalk_env python=3.6
and starting the conda activate makeittal![conda env](https://user-images.githubusercontent.com/112770055/223622691-c13342dd-423f-4860-80e4-8a8bcaef3084.jpg)
k_env.

2. We have installed ffmpeg from this website and added to the environment variables
3. We have installed the required dependencies using
![requirements](https://user-images.githubusercontent.com/112770055/223622729-c54a4880-2aae-4e17-bd12-694df74f62fb.jpg)
4. We have installed CUDA as well to run the model using the local system GPU
5. We have run the the model using the command python main_end2end.py --jpg anne.jpg  
