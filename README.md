# AI Chat app starter using LLAMA with Hugging face inference API (Backend python, frontend Next.js)

This is a starter for creating a LLM based AI chat app with python (FastAPI) as backend and Next.js as frontend
In this starter we are using Meta-Llama-3-8B-Instruct with the inference API(Serverless) which is free.

## Folder structure

root

- client/ (frontend Next.js app)
  - (files and folders for Next.js frontend)
- fastAPI/ (backend FastAPI, Python app)
  - (files and folders for FastAPI backend)

Note: The main file for front end (UI) is page.tsx path: client/src/app/page.tsx and the main file for the backend is main.py, path: fastAPI-backend/main.py

## You can use the model Meta-Llama-3-8B-Instruct or any other model in the following ways:

- Inference API(Serverless) Free (This repo uses Inference API)
- Infererence Endpoints(dedicated) need a subscription
- Transformers, you can download and run the model on your computer or cloud (You need a GPU with atleast 12 or 24GB VRAM)
  You will need to create a free account for huggingface link: https://huggingface.co/welcome
  If the model you want to use is a gated model, you will also need a permission from the Model owner, this is not at all hard to get by the way
  but you will need it in order to use the model.

As you can see the Inference API is the cheapest easiest to use and does not require you to have a powerful machine/GPU/Compute.
Thus for this example we have used Inference API but you can use the other options depending on your use case.

## Additional setup and requirements:

- Get permision for using gated open source models like llama and others
- You will need to generate an access token on the hugging face website: https://huggingface.co/settings/tokens and use it
  either with an .env file inside the fastAPI directory or in the terminal export HF_TOKEN = os.getenv("HF_TOKEN") so that the token is available.

Caution: Never share or use the auth token directly in code or any other files.
