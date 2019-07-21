import feedparser
from flask import Flask
from flask import render_template
app =Flask(__name__)

RSS_FEED ={'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
           'ole': 'https://www.ole.com.ar/rss/river-plate/'}

@app.route("/")
def get_ole():
    return get_news('ole')

@app.route("/bbc")
def get_bbc():
    return get_news('bbc')

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return render_template("home.html", article=first_article)

if __name__ == '__main__':
    app.run(port=5000,debug=True)