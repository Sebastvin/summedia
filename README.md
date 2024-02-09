<div align="center">
<img src="https://github.com/Sebastvin/engineer-demo/assets/34211633/a7327ebd-8489-4c8d-a58b-8936967bf639" height="300" width="300">
<br>
<img src="https://github.com/Sebastvin/engineer-demo/assets/34211633/01e65a79-69e8-4c58-bccb-ab9939ecf442">
</div>

<hr>


![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/Sebastvin/summedia/test.yml)
[![GitHub License](https://img.shields.io/github/license/Sebastvin/summedia)](https://github.com/Sebastvin/summedia)
[![GitHub issues](https://img.shields.io/github/issues/Sebastvin/summedia)](https://github.com/Sebastvin/summedia/issues)


# SumMedia in a News Web package

The SumMedia is a powerful Python tool used for extracting and parsing newspaper articles. It simplifies the process of web scraping, article downloading and working with openai API. The plugin enables various functionalities related to news content personalization and categorization. Here's an overview of its key features and functionalities:

## Table of Contents
1. [Article Extraction](#article-extraction)
2. [SumMedia for Filtering and Categorizing Articles](#summedia-for-filtering-and-categorizing-articles)
3. [SumMedia as a Personal Assistant for Reading Articles](#summedia-as-a-personal-assistant-for-reading-articles)
4. [SumMedia for Generating Post for Social Media](#summedia-for-generating-post-for-social-media)
5. [Multi-language Support](#multi-language-support)


---

### Article Extraction
Download articles from a given URL and extract useful information like the text, authors, publish date, images, videos, and more.

```python
from summedia.fetching_data import (
    get_text,
    get_time_read,
    get_images,
    get_publishing_date,
    get_authors,
    get_title,
    get_movies,
    get_meta_description,
    get_meta_keywords
)

URL = "www.example.url"

text_article = get_text(URL)
time_read = get_time_read(URL, words_per_minute=238)
img_urls = get_images(URL)
publish_date = get_publishing_date(URL)
authors = get_authors(URL)
title = get_title(URL)
movies = get_movies(URL)
meta_description = get_meta_description(URL)
meta_keywords = get_meta_keywords(URL)
```
---

### Filtering and Categorizing Articles
The work can involve using ChatGPT to analyze and filter news or inappropriate content. You can also develop an algorithm for categorizing articles based on topic, location, date, and other factors.

```python
import os
from summedia.text import Text

txt = Text(api_key=os.environ.get("OPENAI_API_KEY"))
tag_and_categorize_text = txt.tag_and_categorize_text("your text here", model_type="gpt-3.5-turbo-1106")
```
---

### Personal Assistant for Reading Articles
Browse various news websites, fetch article headlines and brief summaries, and then deliver them in a user-friendly manner.

```python
import os
from summedia.text import Text
from summedia.level import SimplificationLevel

text = Text(api_key=os.environ.get("OPENAI_API_KEY"))
summary_article = text.summarize_text("www.example.url", max_number_words=150, model_type="gpt-3.5-turbo-1106")
analyze_sentiment = text.analyze_sentiment("www.example.url", max_number_words=150, model_type="gpt-3.5-turbo-1106")
to_bullet_list = text.to_bullet_list("www.example.url", model_type="gpt-3.5-turbo-1106")
adjust_text_complexity = text.adjust_text_complexity("www.example.url", level = SimplificationLevel.STUDENT, model_type="gpt-3.5-turbo-1106")
```
---

### Generating Post for Social Media
Automate posts to Twitter/X and facebook by just specifying the url for article.

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
Handling articles in different languages, making it versatile for international applications. You can also use it as an article translator.

```python
import os
from summedia.text import Text

txt = Text(api_key=os.environ.get("OPENAI_API_KEY"))
translate_text = txt.translate_text("your text here", model_type="gpt-3.5-turbo-1106", language_to_translate="en")
```

---
### Create your own prompt
Create a prompt tailored to your needs.

```python
import os
from summedia.elastic import ElasticAPIRequester

elastic_prompt = ElasticAPIRequester(api_key=os.environ.get("OPENAI_API_KEY"))
content_system_prompt = "YOUR SYSTEM PROMPT HERE"
content_user_prompt = "YOUR USER PROMPT HERE"
elastic_prompt_result = elastic_prompt.elastic_prompt(content_system_prompt, content_user_prompt,  model_type="gpt-3.5-turbo-1106")
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
