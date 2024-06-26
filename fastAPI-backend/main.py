import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM # AutoTokenizer, AutoModelForCausalLM needed for using transformers, we are using the inference API. We do not need it
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define a Pydantic model (Type) for the request body
class GenerateRequest(BaseModel):
    prompt: str

# Allow all origins during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows only your frontend origin
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Retrieve token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN environment variable is not set")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/favicon.ico")
def get_favicon():
    # You can return a file response here if you have a specific favicon.ico
    # file in your static directory, or just return a redirect if not needed.
    return {"message": "Favicon not found"}


API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.post("/generate/")
async def query(payload: GenerateRequest):
    logger.debug(f"Received request with payload: {payload}")
    data = {"inputs": payload.prompt }
    response = requests.post(API_URL, headers=headers, json=data)
    try:
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        logger.error(f"Failed to decode JSON response: {response.text}")
        return {"error": "Failed to decode JSON response from the API"}
    logger.debug(f"Response from API: {response_json}")
    return response_json


# Run the server with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
