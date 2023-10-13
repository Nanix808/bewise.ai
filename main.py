import uvicorn
from fastapi import FastAPI

from bewise.questions.router import questions_router
from bewise.database import create_db

app = FastAPI(debug=False)
app.include_router(questions_router, prefix='/api/questions', tags=['api_v1'])


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}



def main():
    # Create table
    create_db()
    uvicorn.run(app="main:app", host='0.0.0.0',  port=8000, reload=True)
    
if __name__ == '__main__':
    main()
