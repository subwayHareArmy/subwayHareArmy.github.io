---
title: That's enough ~~internet~~ YouTube for today
description: temp
datePublished: 2020-04-15 22:16:00+05:30
dateModified: 2020-04-15 22:16:00+05:30
# img: ["./daancorona_progress.png"]
# imgAlt: A photo describing the revenue progress of the social venture startup, DaanCorona.
# ogImage: ./daancorona_progress.png
# TODO: Find and add a hero image here
tags: ["scraping", "youtube", "analysis"]
visibility: public
---

<!-- PELICAN_BEGIN_SUMMARY -->  
![alt](./temporary_red.png)  

<br>

If you find that the lower limit of your YouTube usage translates to ~1.5% of your life, you'd say, "That's enough YouTube for today," as well. This is probably why YouTube offers no easy way of downloading your history. I scraped for my history through my cookies, but it can downloaded via Google's Takeout service as well.
<!-- PELICAN_END_SUMMARY -->

<br>

Scraping YouTube History
========== 

<br>

While there are multiple methods to do this, I scraped the data by using YouTube cookies from my browser. I exported my cookies through the ***Edit This Cookie*** extension on Chrome. The actual scraping part was done using the Python library, ***Scrapy***.  You could use Selenium, beautifulsoup, and others as well.

<br>

Analysis
==========

<br>

After collecting the video URLs, titles, and duration, I saved it to a CSV file. This resulted in an over 5 MB file, just text. This should be indicative of the size of the history. The file contains over 19,000 rows. 

<br>

I used Python for the analysis. The Jupyter notebook at the end, outlines this analysis.

<br>

Here's  a bunch of insights:  

<br>

- I have watched over **19,340 videos**.
- Amongst these, areound **11,500** have been **unique** videos, and **7,500** have been **repeats**. There is some ambiguity here.
- I have watched videos from over **5,368 channels**.
- The total watch time comes out to **9899651 seconds** , **2750 hours** or **115 days**.
- This translates to **~1.42%** of my life.
