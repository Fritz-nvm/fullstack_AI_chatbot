from fastapi import FastAPI, Request
import uvicorn
import os
import sys
from dotenv import load_dotenv
from src.routes.chat import chat_routes


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))




load_dotenv()

api = FastAPI() #innitialize fast api

api.include_router(chat_routes)


@api.get("/test")
async def root():
    return {"msg": "API is Online"}


if __name__ == "__main__":
    if os.environ.get('APP_ENV') == "development":
        uvicorn.run("main:api", host="0.0.0.0", port=3500,
                    workers=4, reload=True)
    else:
      pass