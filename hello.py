import feedparser
from flask import Flask

app =Flask(__name__)

RSS_FEED ={'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
           'ole': 'https://www.ole.com.ar/rss/river-plate/'}

@app.route("/")
def get_ole():
    return get_news('ole')

@app.route("/bbc")
def get_bbc():
    return get_news('bbc')


def get_news(publication):
    feed = feedparser.parse(RSS_FEED[publication])
    first_article = feed['entries'][0]
    return """
        <html>
            <body>
                <h1>Headlines</h1>
                <b>{0}</b><br/>
                <i>{1}</i><br/>
                <p>{2}</p><br/>
            </body>
        </html>
    """.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000,debug=True)