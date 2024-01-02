<div align="center">
<img src="https://github.com/Sebastvin/engineer-demo/assets/34211633/a7327ebd-8489-4c8d-a58b-8936967bf639" height="300" width="300">
<br>
<img src="https://github.com/Sebastvin/engineer-demo/assets/34211633/01e65a79-69e8-4c58-bccb-ab9939ecf442">
</div>

<hr>


![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Sebastvin/summedia/test.yml)
[![GitHub License](https://img.shields.io/github/license/Sebastvin/summedia)](https://github.com/Sebastvin/summedia)
[![GitHub issues](https://img.shields.io/github/issues/Sebastvin/summedia)](https://github.com/Sebastvin/summedia/issues)


# Using SumMedia in a News Web Application

The SumMedia library is a powerful Python tool used for extracting and parsing newspaper articles. It simplifies the process of web scraping, article downloading and working with openai API.  The plugin enables various functionalities related to news content personalization and categorization. Here's an overview of its key features and functionalities:

## Table of Contents
1. [Article Extraction](#article-extraction)
2. [SumMedia for Filtering and Categorizing Articles](#summedia-for-filtering-and-categorizing-articles)
3. [SumMedia as a Personal Assistant for Reading Articles](#summedia-as-a-personal-assistant-for-reading-articles)
4. [SumMedia for Generating Post for Social Media](#summedia-for-generating-post-for-social-media)
5. [Multi-language Support](#multi-language-support)


---

## Article Extraction
#### SumMedia can download articles from a given URL and extract useful information like the text, authors, publish date, images, videos, and more.

Example:
```python
from summedia.fetching_data import (
    article_time_read,
    get_images_from_html,
    get_text_from_article,
)

text_article = get_text_from_article("www.example.url")
time_read = article_time_read(text_article, words_per_minute=238)
img_urls = get_images_from_html("www.example.url")
```
---

### SumMedia for Filtering and Categorizing Articles
#### The work can involve using ChatGPT to analyze and filter news, removing spam, false information, or inappropriate content. You can also develop an algorithm for categorizing articles based on topic, location, date, and other factors.

Example:
```python
import os
from summedia.text import Text

txt = Text(api_key=os.environ.get("OPENAI_API_KEY"))
tag_and_categorize_text = txt.tag_and_categorize_text("your text here", model_type="gpt-3.5-turbo-1106")
```
---

### SumMedia as a Personal Assistant for Reading Articles
#### SumMedia can browse various news websites, fetch article headlines and brief summaries, and then deliver them in a user-friendly manner.

Example:
```python
import os
from summedia.text import Text
from summedia.level import SimplificationLevel

text = Text(api_key=os.environ.get("OPENAI_API_KEY"))
summary_article = text.summarize_text("www.example.url", max_number_words=150, model_type="gpt-3.5-turbo-1106")
analyze_sentiment = text.analyze_sentiment("www.example.url", model_type="gpt-3.5-turbo-1106")
to_bullet_list = text.to_bullet_list("www.example.url", model_type="gpt-3.5-turbo-1106")
adjust_text_complexity = text.adjust_text_complexity("www.example.url", level = SimplificationLevel.STUDENT, model_type="gpt-3.5-turbo-1106")
```
---

### SumMedia for Generating Post for Social Media
#### With SumMedia you are able to automate posts to Twitter/X and facebook by just specifying the url for article. 

Example:
```python
import os
from summedia.social_media import SocialMedia

social_media = SocialMedia(api_key=os.environ.get("OPENAI_API_KEY"))

post_to_facebook = social_media.post_to_facebook(
    "your text here", model_type="gpt-3.5-turbo-1106"
)

condense_text_to_tweet = social_media.condense_text_to_tweet(
    "your text here", model_type="gpt-3.5-turbo-1106"
)
```
---

### Multi-language Support
####  SumMedia is capable of handling articles in different languages, making it versatile for international applications. 
#### You can also use it as an article translator.

Example:
```python
import os
from summedia.text import Text

txt = Text(api_key=os.environ.get("OPENAI_API_KEY"))
translate_text = txt.translate_text("your text here", model_type="gpt-3.5-turbo-1106", language_to_translate="en")
```

---

### Requirements & Costs
You'll need a <b>paid</b> OpenAI account and an API key.

Check out more here:
https://openai.com/pricing

### Installation
```
pip install summedia
```


#### How to run tests
```
pytest --cov=summedia
```