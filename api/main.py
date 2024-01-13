from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title='Book Store API',
              version='1.0.0')

@app.get('/', response_class=JSONResponse)
def info():
    return JSONResponse(status_code=200, content={
        'app_name': 'Book Store API',
        'version': '1.0.0',
        'author': 'Adan Mercado',
        'email': 'adanmercado.dev@gmail.com'
    })