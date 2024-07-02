import requests

url = 'https://api.duckduckgo.com/'
params = {
    'word': 'Toledo',
    'format': 'json'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    
    if 'AbstractSource' in data and data['AbstractSource'] == 'Wikipedia':
        print("El AbstractSource es Wikipedia.")
    else:
        print("El AbstractSource no es Wikipedia.")
    
    related_topics = []
    
    for topic in data.get('RelatedTopics', []):
        if 'Name' in topic:
            first_url = topic.get('FirstURL', '')
            text = topic.get('Text', '')
            related_topics.append({'FirstURL': first_url, 'Text': text})
        elif 'Topics' in topic:  
            for subtopic in topic['Topics']:
                first_url = subtopic.get('FirstURL', '')
                text = subtopic.get('Text', '')
                related_topics.append({'FirstURL': first_url, 'Text': text})
    
    for item in related_topics:
        print(f"FirstURL: {item['FirstURL']}")
        print(f"Text: {item['Text']}\n")
else:
    print(f"Error en la llamada a la API. Status code: {response.status_code}")