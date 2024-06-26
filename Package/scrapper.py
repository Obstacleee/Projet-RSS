import feedparser
import datetime as dt

def rss_collect(feed):
    news_feed = feedparser.parse(feed)

    flux_Rss = []
    lien = []
    titres = []
    for entry in news_feed.entries:
        
        dateHier = dt.datetime.now()
        date_fin = dt.datetime.now()
        dateHier = int(dateHier.timestamp()) - 86400 
        datePubli = entry.published
        datePubli = dt.datetime.strptime(datePubli, "%a, %d %b %Y %H:%M:%S %z")
        datePubli = int(datePubli.timestamp())

        if dateHier < datePubli:

            title = entry.title.replace('\xa0', ' ')
            summary = entry.summary.replace('\xa0', ' ')

            lien.append(entry.link)
            lien.append(";")

            titres.append(title)
            titres.append(";")

            flux_Rss.append(title)
            flux_Rss.append(summary)
            flux_Rss.append("...")
            
    flux_Rss = ''.join([item for sublist in flux_Rss for item in sublist if item])
    lien = ''.join([item for sublist in lien for item in sublist if item])
    titres = ''.join([item for sublist in titres for item in sublist if item])

    date_debut = dt.datetime.fromtimestamp(dateHier)
    return flux_Rss , date_debut , date_fin , lien, titres


