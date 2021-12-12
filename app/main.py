from fastapi import FastAPI
import uvicorn
import joblib
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://0.0.0.0",
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#total_sales_model = joblib.load('app/models/total_model.h5')
na_sales_model = joblib.load('app/models/NA_model.h5')
europe_sales_model = joblib.load('app/models/europe_model.h5')
japan_sales_model = joblib.load('app/models/japan_model.h5')
other_sales_model = joblib.load('app/models/other_model.h5')


@app.get("/predict/game-success/")
async def predictGameSuccess(score: int = 0, pltfrm: int = 7, gnr: int = 3, rtng: int = 2):

    critic_score, platform, genre, rating = score,[],[],[]
    for i in range(17):
        platform.append(0)

    for i in range(12):
        genre.append(0)
    
    for i in range(7):
        rating.append(0)

    platform[pltfrm] = 1
    genre[gnr] = 1
    rating[rtng] = 1

    x = [[critic_score] + platform + genre + rating]

    
    na_pred = na_sales_model.predict(x)
    eu_pred = europe_sales_model.predict(x)
    ja_pred = japan_sales_model.predict(x)
    oth_pred = other_sales_model.predict(x)

    na_pred = na_pred.tolist()
    eu_pred = eu_pred.tolist()
    ja_pred = ja_pred.tolist()
    oth_pred = oth_pred.tolist()

    return [na_pred,eu_pred, ja_pred, oth_pred]


if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0")