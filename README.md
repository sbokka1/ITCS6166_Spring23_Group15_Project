## CCN Project Group 15
### Team Members:
Srikar Chamarthy - 801317299

Aneela Gannarapu - 801312361

Aravind Pabbisetty - 801254719

Sai Kiran Reddy Bokka - 801283586

### Project Title:
Video Call Application (WebRTC) with audio driven talking head generation.

### Introduction:
The project is centered around a video call, where we capture the audio of the caller (sender) and transmit over to the receiver where the face of the caller is transitioned to the animated character or a hero. While the audio of the caller remains the same. 

The key benefits of above transition are as follows:
* The privacy of the callers is protected as we are changing the face of callers to well-know characters. Thereby, the identity of users can be withheld with utmost security. 
* The disturbances that occur due to poor network connection can be avoided as we are transmitting only audio. This is because audio transmission requires less bandwidth when compared video transmission.

### Architecture:
We are planning to build a web application so we will be using Client-Server Architecture. We will be using WebRTC protocol for real time communication. In this application architecture first the peers will exchange their offer and anwser responses via a Signaling server.The offer and answer responses will contain session description, peers media capabilities etc. Once its done then they exchance ICE(Inter Connectivity Establishment) candidates to identify and exchange network adresses,ports via the same signaling server. In between the peers there will be a relay server which hosts the ML model used to convert the audio stream from the first peer using the face selected into the audio driven face stream. The relay server will send the converted stream to the other peer in the WebRTC session. The signaling server and relay server can be implemented using the same server but for the architecture purpose we have shown differently.
![Video Chat Application with Audio driven face](https://user-images.githubusercontent.com/28972981/220796088-b1e02861-2120-4e0b-a953-db1e09c13bf0.png)

### Technologies to be Used:
Python,
WebRTC,
Streamlit.
(Will be updated if there are any changes further)

### Iteration 1:
* Installing Python3.x
* Installing Conda and setting up Conda environment.
* Researching provided ML models for the audio driven approach and deciding which model to implement.
* Learning about streamlit and WebRTC concepts.

### Iteration 2:
* Creating a UI design for the application.
* Developing a video call application using WebRTC(aiortc library).
* Implementing code to send the audio stream and the image selected in the UI to the relay server.

### Iteration 3:
* Installing all the required libraries for the chosen ML model in the Conda environment.
* Integrating ML model to transform audio and selected image to generate a video.
* Transmitting the generated video to the second client via the relay server.

### Iteration 4:
* Testing the application end-to-end and checking the performance/latency of the application.
* Improve the code to optimize and improve lantency if needed.
* Try to develop a mobile application within the deadline if feasible.

### Iteration 5:
* Perform final tests to ensure the video transmission is in place and  work on fixing the bugs if any.
* Focus will be on the project documentation that includes step-by-step instructions to execute the project and presentations that includes test-case results.


![flowchart](https://user-images.githubusercontent.com/28972981/220804654-d224f40a-0608-4aa9-961b-52e3530f04eb.jpeg)
