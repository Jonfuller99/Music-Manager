from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {
        "message": "this is the main page",
        "age": 12,
        "items" : [
            {"game" : "fortnite", "year": '2018', "img": "../assets/fortnite-logo-1.jpg"},
            {"game" : "Minecraft", "year": '2011', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "League of Legends", "year": '2009', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Counter-Strike 2", "year": '2023', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Valorant", "year": '2020', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Apex Legends", "year": '2019', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Call of Duty: Warzone", "year": '2020', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Grand Theft Auto V", "year": '2013', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Dota 2", "year": '2013', "img": "assets/fortnite-logo-1.jpg"} ,
            {"game" : "Overwatch 2", "year": '2022', "img": "assets/fortnite-logo-1.jpg"},
            {"game" : "Rocket League", "year": '2015', "img": "assets/fortnite-logo-1.jpg"}
        ],
        "url": "http://localhost:8000/api/hello" 
    }

@app.get("/api/hello")
async def read_root():
    return {"message": "hello this is the fast api working"}