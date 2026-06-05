from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")

templates=Jinja2Templates(directory="templates")
posts: list[dict] = [
    {
        "id": 1,
        "author": "Anurag Gorantla",
        "title": "Why I Switched From Watching Tutorials to Actually Building",
        "content": "Tutorial hell is real. I spent 3 months watching videos feeling productive. The day I closed YouTube and opened a blank file — that's when I actually started learning.",
        "date_posted": "May 10, 2025",
    },
    {
        "id": 2,
        "author": "Ravi Teja",
        "title": "LeetCode Isn't About Memorizing Solutions",
        "content": "The moment I stopped copy-pasting solutions and started tracing through problems manually with pen and paper — my understanding jumped completely. Slow down to speed up.",
        "date_posted": "May 15, 2025",
    },
    {
        "id": 3,
        "author": "Priya Sharma",
        "title": "How I Got My First Real Users on a Side Project",
        "content": "I stopped building things for my resume and started solving one problem I personally felt every day. Shipped something ugly but useful. 12 real users in the first week.",
        "date_posted": "May 22, 2025",
    },
    {
        "id": 4,
        "author": "Kiran Reddy",
        "title": "Backend Development Changed How I Think About the Web",
        "content": "Before backend, a website was magic to me. Now I see the request, the validation, the database call, the response — every layer is visible. It's like getting X-ray vision.",
        "date_posted": "June 1, 2025",
    },
]
@app.get("/",include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request,"home.html",{"posts":posts,"title":"HOME"})
@app.get("/api/posts")
def get_posts():
    return posts
