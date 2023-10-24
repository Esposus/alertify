from fastapi import FastAPI
from routers import router as api_router

app = FastAPI()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
