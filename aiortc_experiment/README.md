# Experimenting with aiortc
I used aiortc repo: https://github.com/aiortc/aiortc to learn to understand how WebRTC works and tinker with its internals.
Since the repository is quite old, newer version of python didn't work. So I figured python3.9 worked well.
# What is aiortc?
aiortc is a Python library that enables developers to implement WebRTC and ORTC protocols, which are used for real-time communication between web browsers and other devices. Unlike other existing implementations of WebRTC and ORTC, aiortc provides Python bindings and is more flexible, allowing developers to integrate their own audio or video processing algorithms into their applications. This makes aiortc a valuable tool for developers who prefer Python as their primary language and want to create custom real-time communication applications.

# Setting up environment
Creating conda environment 
` conda create -n aiortc_experiment python=3.9 `
<img width="1002"  src="https://user-images.githubusercontent.com/124751592/223612470-263cb82a-035a-4025-8184-68ef81853e7b.png">
Activate conda environment
` conda activate aiortc_experiment `
<img width="1002" alt="2" src="https://user-images.githubusercontent.com/124751592/223612771-8890c313-f043-4d83-90de-8bf426650352.png">
Installing pip
`conda install -c anaconda pip`
<img width="1002" alt="3" src="https://user-images.githubusercontent.com/124751592/223612961-da0ad057-c55a-46dd-b240-b98eca4db7f0.png">
Installing necessary system libraries
`brew install ffmpeg opus libvpx pkg-config`
<img width="1002" alt="4" src="https://user-images.githubusercontent.com/124751592/223613024-04b93b4c-1fc1-4536-ac66-4a8bc2193259.png">
Installing required python libraries
`pip install aiohttp aiortc opencv-python`
<img width="1002" alt="5" src="https://user-images.githubusercontent.com/124751592/223615678-21d17e1b-da10-4839-a955-e84fa0992ffc.png">
Cloning the aiortc repo
`git clone https://github.com/aiortc/aiortc.git`
Running the server
`python server.py`
<img width="1002" alt="9" src="https://user-images.githubusercontent.com/124751592/223616674-c77ddae0-3685-4565-aa86-dac1c9fd71e4.png">
Using the video and starting the stream
<img width="1538" alt="11" src="https://user-images.githubusercontent.com/124751592/223616747-a249de55-a7b8-419b-acd2-7b065cfb94b3.png">
<img width="1582" alt="13" src="https://user-images.githubusercontent.com/124751592/223616809-bdb84ddc-3b69-4942-bec5-12946de74858.png">
<img width="1582" alt="14" src="https://user-images.githubusercontent.com/124751592/223616867-9d6af5e5-de37-4a1c-a8a3-cec4a2afe331.png">

