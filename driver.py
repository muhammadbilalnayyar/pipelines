import os

import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# Get the current working directory
cwd = os.getcwd()

# Check if logs directory exists, if not create it
logs_dir = os.path.join(cwd, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Check if logs directory exists, if not create it
data_dir = os.path.join(cwd, "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

if __name__ == "__main__":
    uvicorn.run("src.api:app", host="0.0.0.0", port=8000, workers=1, reload=True)
