#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Import Splinter and BeautifulSoup
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[17]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[18]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[19]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[20]:


slide_elem.find('div', class_='content_title')


# In[21]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[22]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[23]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[24]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[25]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[26]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[27]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[28]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[29]:



df.to_html()


# In[30]:


# browser.quit()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[46]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[62]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# Parse the data
html = browser.html
urls_soup = soup(html, 'html.parser')

# 3. Write code to retrieve the image urls and titles for each hemisphere.
divs=urls_soup.find("div", class_= 'collapsible results')

relative_urls=set([anchor['href'] for anchor in anchors])
print(f'Found {len(relative_urls)} URLs')

base_url= 'https://marshemispheres.com/'

for relative_url in relative_urls:
    hemispheres = {}
    
    full_url = f'{base_url}{relative_url}'
    browser.visit(full_url)
    browser.links.find_by_text('Open').click()
    
    # Parse the data
    html = browser.html
    urls_soup = soup(html, 'html.parser')
    
   
    downloads_div = urls_soup.find('div', class_='downloads')
    img_anchor = downloads_div.find('a', target="_blank")
    img_url = img_anchor['href']
    tot_url= f'{base_url}{img_url}'
    print(f'--> url: {tot_url}')
    
    title_elem = urls_soup.find('div', class_='cover')
    title = title_elem.find("h2", class_='title').get_text()
    print(f'--> title: {title}')
    
    hemispheres = {
        'img_url': tot_url,
        'title': title,
    }
    hemisphere_image_urls.append(hemispheres)
 


# In[63]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[64]:


# 5. Quit the browser
browser.quit()


# In[ ]:




