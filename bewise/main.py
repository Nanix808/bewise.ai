import uvicorn
from fastapi import FastAPI
from questions.router import questions_router

from database import create_db

app = FastAPI(debug=True)
app.include_router(questions_router, prefix='/api/questions', tags=['api_v1'])

def main():
    # Create table
    create_db()
    uvicorn.run(app="main:app", host='127.0.0.1',  port=8000, reload=True)
    
if __name__ == '__main__':
    main()
