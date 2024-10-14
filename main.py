from dotenv import load_dotenv, find_dotenv
import time
from openai import OpenAI
import logging
from datetime import datetime
import requests
import json
load_dotenv()
client = OpenAI()
model = "gpt-4o"
def get_news(topic):
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&apiKey=f5bdaf50a5aa406181f3298f1d013dcf&pageSize=5"
    )
    try:
        response = requests.get(url)
        if response.status_code == 200:
            news = json.dumps(response.json(), indent =4)
            news_json = json.loads(news)
            data = news_json
            #loop through API return
            status = data["status"]
            total_results = data["totalResults"]
            articles = data["articles"]
            final_news = []
            for article in articles:
                title = article["title"]
                url = article["url"]
                source_name = article["source"]["name"]
                author = article["author"]
                description = article["description"]
                content = article["content"]
                title_description = f"""
                Title: {title}
                Author: {author}
                Source: {source_name}
                Description: {description}
                URL: {url}
                
                """

                final_news.append(title_description)

            return final_news
        else:
            return []

    except requests.exceptions.RequestException as e:
        print("Error!", e)

def main():
    news = get_news("trump")
    print(news[0])

 class AssistantManager:
     thread_id = None
     assistant_id = None

     def __init__(self, model: str=model):
         self:client = client
         self.model = model
         self.assistant = None,
         self.thread = None,
         self.Run = None
         self.summary = None

         if AssistantManager.assistant_id:
             self.assistant = self.client.beta.assistants.retrieve(
                 assistant_id=AssistantManager.assistant_id
             )
         if AssistantManager.thread_id:
             self.thread = self.client.beta.threads.retrieve(
                 thread_id=AssistantManager.thread_id
             )
    def create_assistant(self, name, instructions, tools):

    if __name__ == "__main__":
        main()

if __name__ == "__main__":
    main()

