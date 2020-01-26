import pymongo
from bs4 import BeautifulSoup
from newspaper import Article
# import nltk
# nltk.download('punkt')
from multiprocessing.pool import ThreadPool
from tqdm import tqdm

def alterObject(obj_id, collection, i):
    item = collection.find_one({'_id': obj_id})
    url = item["url"]
    article = Article(url)
    try:
        article.download()
        article.parse()
        article.nlp()
        set_obj = {}
        if article.top_image:
            set_obj["image"] = article.top_image
        if article.summary:
            set_obj["description"] = article.summary
        if article.title:
            set_obj["title"] = article.title
        newItems = {
            '$set': set_obj
        }
        collection.update_one({'_id': obj_id}, newItems)
    except:
        return
    print(i)


if __name__ == '__main__':
    client = pymongo.MongoClient("mongodb+srv://title_appender:ypLsou4jlqwaaE1I@skarcluster-zb6ru.gcp.mongodb.net/test?retryWrites=true&w=majority")
    database = client.events
    collection = database.events

    ids = collection.find().distinct('_id')
    num = 20
    tp = ThreadPool(num)

    for i, obj_id in enumerate(ids):
        tp.apply_async(alterObject, (obj_id, collection,i, ))

    tp.close()
    tp.join()

# print(collection.find_one()["_id"])

# count = 0
# for event in collection.find():
#     date = event["date"]
#     url = event["url"]
#     article = Article(url)
#     article.download()
#     article.parse()
#     article.nlp()
#     print(url, date.year, date.month, article.top_image, article.summary)
#     # print(date.year, date.month, url)
#     # newvalues = { "$set": { "image": "none provided" } }
#     # collection.update_one(event, newvalues)
#     if count < 10:
#         count += 1
#         continue
#     else:
#         break

# pprint.pprint(collection.count_documents({}))

