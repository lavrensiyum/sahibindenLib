import pandas as pd

def dataToPandas(title, link, square_meters, rooms, price, date, district):
        data = {
                "title": [title],
                "link": [link],
                "square_meters": [square_meters],
                "rooms": [rooms],
                "price": [price],
                "date": [date],
                "district": [district]
        }

        df = pd.DataFrame(data, index=[0])  # Pass index=[0] when creating the DataFrame
        df.to_csv("data.csv", mode="a", header=False)

def dataCSVControl(title, link, square_meters, rooms, price, date, district):
        df = pd.read_csv("data.csv")
        df = df.drop("Unnamed: 0", axis=1)
        df = df.drop_duplicates(subset=['link'], keep='first')
        df = df.reset_index(drop=True)
        df.to_csv("data.csv")

        if link not in df["link"].values:
                return True
        else:
                return False


def dataWorkerStart(title, link, square_meters, rooms, price, date, district):
       
       # CSV dosyası kontrol edilir. Yoksa oluşturulur.
        try:
                df = pd.read_csv("data.csv")
        except:
                df = pd.DataFrame(columns=["title", "link", "square_meters", "rooms", "price", "date", "district"])
                df.to_csv("data.csv")

        # CSV dosyası kontrol edilir. İlan daha önce kaydedilmediyse kaydedilir.
        bool_CSV_Control = dataCSVControl(title, link, square_meters, rooms, price, date, district)
        if bool_CSV_Control:
            dataToPandas(title, link, square_meters, rooms, price, date, district)

