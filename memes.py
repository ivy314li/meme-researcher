import csv
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions, SentimentOptions

#read csv file
csv_write = []
csv_write.append(['confession', 'sentiment', 'joy', 'sadness', 'fear', 'disgust', 'anger'])

with open('ucsdconfessions.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    clist = list(csv_reader)

print(clist)

for i in range(len(clist)):
    #analyze confession
    confession = clist[i][0]

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2018-11-16',
        iam_apikey='YOUR_API_KEY',
        url='YOUR_URL_')

    response = natural_language_understanding.analyze(
        text = confession,
        features=Features(
            sentiment = SentimentOptions(),
            emotion = EmotionOptions()
                )).get_result()

    datas = []
    #select data from json
    datas.append(confession)
    datas.append(response["sentiment"]["document"]["score"])
    datas.append(response["emotion"]["document"]["emotion"]["joy"])
    datas.append(response["emotion"]["document"]["emotion"]["sadness"])
    datas.append(response["emotion"]["document"]["emotion"]["fear"])
    datas.append(response["emotion"]["document"]["emotion"]["disgust"])
    datas.append(response["emotion"]["document"]["emotion"]["anger"])

    csv_write.append(datas)

csv_file.close()

#write to csv_file
with open('person.csv', 'w') as csMeep:
    writer = csv.writer(csMeep)
    writer.writerows(csv_write)

csMeep.close()
