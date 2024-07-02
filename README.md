-----MAN PAGE FOR BEGINNERS------

GenAI and Democracy Project

!NAME
GenAI and Democracy - A project exploring the intersection of Generative AI (LLMs) and democratic processes.

!SYNOPSIS
This project provides a framework for experimenting with large language models (LLMs) to understand their potential impact on democracy. It includes a Dockerized environment for running inference, preprocessing data, and setting up user configurations.

!DESCRIPTION
The GenAI and Democracy project is part of the GenerativeAI and Democracy seminar at HfP / TUM. It aims to provide participants with the tools and knowledge needed to explore how generative AI can be used within the context of democratic processes. The project leverages open-source LLMs, allowing users to run these models efficiently on their hardware.

!Components
user_setup.py: Initializes the environment. Must return a non-zero exit code if unsuccessful.
user_preprocess.py: Preprocesses input data and saves it to preprocessed-file.json.
user_inference.py: Takes a user query and outputs a response based on preprocessed data.

!Running the Project
The project runs inside a Docker container. The startup sequence involves running user_setup.py, user_preprocess.py, and finally user_inference.py with specified user queries. Testing individual components of the pipeline is possible using test.py.

!Environment
The Docker container includes Python 3.11.0, numpy 1.24.0, torch 2.0.0, and transformers 4.12.0. Users are encouraged to match these versions in their local environment to avoid discrepancies.

!EXAMPLE
' Prerequisites
' Make sure you have Docker installed on your machine. If not, you can download and install it from Docker's official website: https://www.docker.com/
(https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)

' Build the Docker Image:
shell("sudo docker build -t googl2 .")

' Run the Docker Container:
shell("docker run -p 4000:80 googl2")

' Find the Running Docker Container Name:
shell("docker ps")

' Example output:
' CONTAINER ID   IMAGE   COMMAND                  CREATED         STATUS         PORTS                   NAMES
' 7b1e1fbf9208   googl   "tail -f /dev/null"      5 minutes ago   Up 5 minutes   0.0.0.0:4000->80/tcp    stoic_dewdney

' Run Inference Using the Docker Container:
shell("docker exec stoic_dewdney python user_inference.py --query 'How many people live in London?' --query_de 'myFirstQ'")

' Stopping the Docker Container and release the Port:
shell("docker stop confident_torvalds")

' Example Usage
![image](https://github.com/PhillipTian/genai-and-democracy-2024/assets/87056960/3b5921d4-23b9-4ad8-b9b5-3e5f990847bc)


