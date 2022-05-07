from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from base64 import b64encode

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

base_64 = b64encode(b'password123')

html_1 = f"""
<html>
<body>
<h1>Hello!</h1>
<input id="password-reminder" type=password>
<script>
    var pw = decodeURIComponent(atob("{base_64}"))
    window.onload = function () {"{"}document.getElementById('password-reminder').value = pw{"}"}
</script>
</body>
</html>
"""


@app.get("/test")
async def test():
    return HTMLResponse(html_1)
