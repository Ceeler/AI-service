from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from endpoints import predict


app = FastAPI(title="DIGITS")

origins = [
    "http://localhost.tiangolo.com",
    "http://192.168.0.116:8080",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router, prefix="/predict", tags=["predict"])

@app.get("/")
async def root():
    return {"message" : "Hello world"}

   
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)