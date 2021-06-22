from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_cnn
import os

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection: 
# Set up (DB: mars_info_app, Collection: mars_info)
mongo = PyMongo(app, uri="mongodb://localhost:27017/cnn_news_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    news_info = mongo.db.news_info.find_one()

    # Return template and data
    return render_template("index.html", news_info=news_info)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

  # Run scrapped functions
  news_info = mongo.db.news_info
  news_data = scrape_cnn.scrape_cnn_news()

  # Update the Mongo database using update and upsert=True
  news_info.update({}, news_data, upsert=True)

  # Redirect back to home page
  return redirect("/", code=302)
  
if __name__ == "__main__":
    app.run(debug=True)
