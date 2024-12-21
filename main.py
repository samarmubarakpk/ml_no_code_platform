from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import StringIO
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
async def split_data(file: UploadFile = File(...), train_size: float = 0.7, val_size: float = 0.15):
    # Ensure file is CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    try:
        # Read uploaded file
        file_content = await file.read()
        data = pd.read_csv(StringIO(file_content.decode('utf-8')))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading file: {str(e)}")

    # Ensure 'target' column exists
    if 'target' not in data.columns:
        raise HTTPException(status_code=400, detail="CSV file must contain a 'target' column.")

    # Split data
    splitter = DataSplitter()
    splits = splitter.split_data(data, 'target', train_size, val_size)
    sizes = splitter.get_split_sizes()

    return {"split_sizes": sizes}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
