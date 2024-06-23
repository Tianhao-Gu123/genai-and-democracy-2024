-----MAN PAGE------

GenAI and Democracy Project
NAME
GenAI and Democracy - A project exploring the intersection of Generative AI (LLMs) and democratic processes.

SYNOPSIS
This project provides a framework for experimenting with large language models (LLMs) to understand their potential impact on democracy. It includes a Dockerized environment for running inference, preprocessing data, and setting up user configurations.

DESCRIPTION
The GenAI and Democracy project is part of the GenerativeAI and Democracy seminar at HfP / TUM. It aims to provide participants with the tools and knowledge needed to explore how generative AI can be used within the context of democratic processes. The project leverages open-source LLMs, allowing users to run these models efficiently on their hardware.

Getting Started
To begin, users should familiarize themselves with LLMs by reading the Introduction on LLMs. The project setup involves adjusting the user_config.py file to fit the user's needs and understanding the Docker environment specified in the Dockerfile and requirements.txt.

Components
user_setup.py: Initializes the environment. Must return a non-zero exit code if unsuccessful.
user_preprocess.py: Preprocesses input data and saves it to preprocessed-file.json.
user_inference.py: Takes a user query and outputs a response based on preprocessed data.
Running the Project
The project runs inside a Docker container. The startup sequence involves running user_setup.py, user_preprocess.py, and finally user_inference.py with specified user queries. Testing individual components of the pipeline is possible using test.py.

Environment
The Docker container includes Python 3.11.0, numpy 1.24.0, torch 2.0.0, and transformers 4.12.0. Users are encouraged to match these versions in their local environment to avoid discrepancies.

FILES
Dockerfile: Specifies the Docker environment.
requirements.txt: Lists the Python package dependencies.
user_config.py: User-specific configuration settings.
user_setup.py, user_preprocess.py, user_inference.py: Core scripts for the project pipeline.
SEE ALSO
Ollama for running LLMs.
Introduction on LLMs for a primer on large language models.
AUTHORS
This project is a collaborative effort by participants of the GenerativeAI and Democracy seminar at HfP / TUM.

EXAMPLE
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

