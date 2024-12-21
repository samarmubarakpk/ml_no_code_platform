from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from src.components.data_splitter import DataSplitter
from src.components.data_preprocessor import DataPreprocessor

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your React app will run here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ML Platform API is running"}

@app.post("/split-data")
async def split_data(train_size: float = 0.7, val_size: float = 0.15):
    # For prototype, using a simple example dataset
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'target': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    })
    
    splitter = DataSplitter()
    splits = splitter.split_data(data, 'target', train_size, val_size)
    sizes = splitter.get_split_sizes()
    
    return {"split_sizes": sizes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
