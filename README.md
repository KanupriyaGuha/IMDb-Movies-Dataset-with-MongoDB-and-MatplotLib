# IMDb-Movies-Dataset-with-MongoDB-and-MatplotLib
IMDb Big Data Project using MongoDB, MatplotLib and Python

# 🎬 IMDb Big Data Project with MongoDB

## 📌 Overview
This project demonstrates how to use MongoDB, a distributed NoSQL database, for ingesting, storing, cleaning, aggregating, and visualizing large-scale movie metadata from the IMDb dataset.

---

## 💡 Why MongoDB?
- Schema-less, document-oriented NoSQL database
- Ideal for hierarchical/semi-structured data like movies, genres, and ratings
- Fast aggregation pipelines
- Scales horizontally for Big Data workloads

---

## 📂 Dataset Used
- **Source**: [IMDb Datasets](https://www.imdb.com/interfaces/)
- **Files**:
  - `title.basics.tsv`: Basic movie info (title, year, genre, etc.)
  - `title.ratings.tsv`: Ratings and vote count
- **Format**: Tab-separated `.tsv`
- **Size**: 300K+ entries before cleaning

---

## ⚙️ Tools & Technologies
- Python 3.x
- MongoDB Community Edition (local)
- Libraries: `pandas`, `pymongo`, `matplotlib`

---

## 🚀 Project Workflow

1. Downloaded IMDb data (`.tsv.gz`) and extracted
2. Loaded and cleaned using `pandas`:
   - Removed nulls and duplicates
   - Converted numeric types
   - Split genre strings into arrays
3. Inserted cleaned data into MongoDB using `pymongo`
4. Aggregated top 10 movie genres using MongoDB aggregation framework
5. Visualized the result using `matplotlib`

##  Dataset
✅ Format: TSV (structured, parsed by pandas)
✅ Size: IMDb title.basics.tsv + title.ratings.tsv → combined dataset with 100,000+ rows and 7+ columns after cleaning.
