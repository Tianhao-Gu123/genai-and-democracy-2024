' GenAI and Democracy 2024

' Welcome to the GenAI and Democracy 2024 project! This repository contains all necessary files and instructions to set up and run our Docker-based environment for processing and analyzing user queries with our advanced inference model.

' Getting Started

' Prerequisites
' Make sure you have Docker installed on your machine. If not, you can download and install it from Docker's official website: https://www.docker.com/

' Building and Running the Docker Container

' Build the Docker Image:
shell("docker build -t googl2 .")

' Run the Docker Container:
shell("docker run -p 4000:80 googl2")

' Find the Running Docker Container Name:
shell("docker ps")

' Example output:
' CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                   NAMES
' 7b1e1fbf9208   googl   "tail -f /dev/null"      5 minutes ago   Up 5 minutes   0.0.0.0:4000->80/tcp    stoic_dewdney

' Running Inference

' Run Inference Using the Docker Container:
shell("docker exec stoic_dewdney python user_inference.py --query 'How many people live in London?' --query_de 'myFirstQ'")

' Stopping the Docker Container

' Release the Port:
shell("docker stop confident_torvalds")

' Example Usage

' To run an example query, execute the following command:
shell("docker exec affectionate_antonelli python user_inference.py --query 'How many people live in London?' --query_de 'myFirstQ'")

' Output:
' :) Great! We have found some results for you! And the higher the score, the more relevant the text is.
' Score: 100.361

