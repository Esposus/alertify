from fastapi import FastAPI
from routers import router as api_router

app = FastAPI()
app.include_router(api_router)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)
