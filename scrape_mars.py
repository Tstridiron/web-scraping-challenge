#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install splinter')
from bs4 import BeautifulSoup
from splinter import Browser
import os
import pandas as pd
import time


# In[10]:


# Set Executable Path & Initialize Chrome Browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[11]:


#Visiting NASA Mars News
url = "https://mars.nasa.gov/news/"
browser.visit(url)
html = browser.html
soup = bs(html,"html.parser")


# In[12]:


#Title and Paragraph
news_title = soup.find("div",class_="content_title").text
news_paragraph = soup.find("div", class_="section_description").text
print(f"Title: {news_title}")
print(f"Paragraph: {news_paragraph}")


# In[13]:


#PL Mars Space Images - Featured Image
url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
browser.visit(url_image)


# In[14]:


#Finding image
full_image_button = browser.find_by_id("full_image")
full_image_button.click()


# In[15]:


browser.is_element_present_by_text("more info", wait_time=1)
more_info_element = browser.find_link_by_partial_text("more info")
more_info_element.click()


# In[16]:


html = browser.html
image_soup = BeautifulSoup(html, "html.parser")

img_url = image_soup.select_one("figure.lede a img").get("src")
img_url
#Full image URL
img_url = f"https://www.jpl.nasa.gov{img_url}"
print(img_url)


# In[17]:


#Mars Weather (Twitter)
url_weather = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_weather)


# In[18]:


html_weather = browser.html
soup = bs(html_weather, "html.parser")
mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
print(mars_weather)


# In[19]:


mars_df = pd.read_html("https://space-facts.com/mars/")[0]
#print(mars_df)
mars_df.columns=["Description", "Value"]
mars_df


# In[20]:


#Mars Hemispheres
# Visit the USGS Astrogeology Science Center Site
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(url)


# In[22]:


hemisphere_image_urls = []

# Get a List of All the Hemispheres
links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    # Find Element on Each Loop to Avoid a Stale Element Exception
    browser.find_by_css("a.product-item h3")[item].click()
    
    # Find Sample Image Anchor Tag & Extract <href>
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    # Get Hemisphere Title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    # Append Hemisphere Object to List
    hemisphere_image_urls.append(hemisphere)
    
    # Navigate Backwards
    browser.back()
    
hemisphere_image_urls


# In[ ]:




