import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [{"role":"user", "content":prompt}]
    response = openai.chat.completions.create(
        model = model,
        messages = messages,
        temperature=0,
    )

    return response.choices[0].message.content

lamp_review = """
Needed a nice lamp for my bedroom, and this one had \
additional storage and not too high of a price point. \
Got it fast.  The string to our lamp broke during the \
transit and the company happily sent over a new one. \
Came within a few days as well. It was easy to put \
together.  I had a missing part, so I contacted their \
support and they very quickly got me the missing piece! \
Lumina seems to me to be a great company that cares \
about their customers and products!!
"""

prompt = f"""
What is the sentiment of the following product review, which is delimited with triple backticks?

Give your answer as a single word, either "positive"
or "negative".

Review text: ```{lamp_review}```
"""

response = get_completion(prompt)
print(response)

prompt = f"""
Identify a list of emotions that the writer of the \
following review is expressing. Include no more than \
five items in the list. Format your answer as a list of \
lower-case words separated by commas.

Review text: '''{lamp_review}'''
"""
response = get_completion(prompt)
print(response)

#Extracting information from review text
prompt = f"""
Identify the following items from the review text:
-Item purchased by the reiewer
-Company that made the item 

The review is delimited with triple backticks.
Format your response asa json object with "Item" and "Brand 
as the keys.  If the information is not present, use "unknown"
as the value.

Make your response as short as possible.

Review text: ```{lamp_review}```
"""

response = get_completion(prompt)
print(response)

#Identifying multiple tasks at once
prompt = f"""
Identify the following items from the review text:
-Sentiment(positve or negative)
-Is the reviewer expressing anger?(true or false)
-Item purchased by reviewer 
-Company that made the item

The review is delimited with triple backtick.
Format your response as a JSON object with "Sentiment", "Anger", "Item", and "Brand" as the keys. 
If the information is not present use unknown as the value.

Make your response as short as possible.
Format the Anger value as a boolean.

Review text: ```{lamp_review}```
"""

response = get_completion(prompt)
print(response)

#Inferring topics
story = """
In a recent survey conducted by the government, 
public sector employees were asked to rate their level 
of satisfaction with the department they work at. 
The results revealed that NASA was the most popular 
department with a satisfaction rating of 95%.

One NASA employee, John Smith, commented on the findings, 
stating, "I'm not surprised that NASA came out on top. 
It's a great place to work with amazing people and 
incredible opportunities. I'm proud to be a part of 
such an innovative organization."

The results were also welcomed by NASA's management team, 
with Director Tom Johnson stating, "We are thrilled to 
hear that our employees are satisfied with their work at NASA. 
We have a talented and dedicated team who work tirelessly 
to achieve our goals, and it's fantastic to see that their 
hard work is paying off."

The survey also revealed that the 
Social Security Administration had the lowest satisfaction 
rating, with only 45% of employees indicating they were 
satisfied with their job. The government has pledged to 
address the concerns raised by employees in the survey and 
work towards improving job satisfaction across all departments.
"""

prompt = f"""
Determine five topics that are being discussed in the \
following text, which is delimited by triple backticks.

Make each item one or two words long. 

Format your response as a list of items separated by commas.

Text sample: '''{story}'''
"""
response = get_completion(prompt)
print(response)
