from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
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
<div id="box"></div>
<form onsubmit="handleSubmit(); return false;">

    <input id="password-reminder" type=password>

</form>
<script>
    var box = document.querySelectorAll("box")[0]
    function handleSubmit() {"{"}
    var val = document.getElementById('password-reminder')
    var box = document.getElementById('box')
    box.innerHTML += `<br>${"{"}val.value{"}"} is not the password`;
    val.value = null;
    {"}"}
    function showPass () {"{"}
     alert("password")
    {"}"}
</script>
</body>
</html>
"""


@app.get("/test")
async def test():
    return HTMLResponse(html_1)

app.mount('/static', StaticFiles(directory="/code"), name="static")

