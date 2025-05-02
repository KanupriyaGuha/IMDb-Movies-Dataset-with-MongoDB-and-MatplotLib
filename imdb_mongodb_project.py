import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

print("📥 Loading data...")
movies = pd.read_csv("title.basics.tsv", sep='\t', na_values='\\N')
ratings = pd.read_csv("title.ratings.tsv", sep='\t', na_values='\\N')

print("🎬 Filtering movie records...")
movies = movies[movies["titleType"] == "movie"]

print("🔗 Merging data...")
df = pd.merge(movies, ratings, on="tconst")
df = df[[
    "tconst", "primaryTitle", "startYear",
    "runtimeMinutes", "genres", "averageRating", "numVotes"
]]

print("🧹 Cleaning data...")
df.dropna(inplace=True)
df.drop_duplicates(subset="tconst", inplace=True)
df["startYear"] = df["startYear"].astype(int)
df["runtimeMinutes"] = df["runtimeMinutes"].astype(int)
df["genres"] = df["genres"].apply(lambda x: x.split(","))

print("🧠 Connecting to MongoDB...")
client = MongoClient("mongodb://localhost:27017/")
db = client["imdb"]
collection = db["movies"]
collection.delete_many({})
print(f"🚀 Inserting {len(df)} records into MongoDB...")
collection.insert_many(df.to_dict("records"))

print("\n📊 Record count in MongoDB:", collection.count_documents({}))
print("📄 Sample document keys:", list(collection.find_one().keys()))

print("\n📈 Aggregating top 10 genres...")
pipeline = [
    {"$unwind": "$genres"},
    {"$group": {"_id": "$genres", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
]
top_genres = list(collection.aggregate(pipeline))

print("📉 Generating bar chart...")
labels = [g["_id"] for g in top_genres]
counts = [g["count"] for g in top_genres]

plt.figure(figsize=(10, 6))
plt.bar(labels, counts, color='skyblue')
plt.title("Top 10 Movie Genres (IMDb)")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_genres.png")
plt.show()

print("\n✅ Done! Chart saved as 'top_genres.png'.")
