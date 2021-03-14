Title: Dunzo PM Intern
Date: 2018-07-19 12:48
Category: Pages
Tags: 2020, PM Intern, Dunzo
Slug: dunzo-pm-intern
Authors: Ayush Yembarwar
Summary: My answers for the Dunzo PM Intern 

The app changes I proposed in the form, are expanded upon, here.  

**Since the Dunzo PM Intern form says that I should suggest app changes, I shall refrain from suggesting changes like "introduce support for multiple pickups and multiple drops in Dunzo Assistant", since these are majorly changes to the logistics operation of Dunzo, and not the app itself.**     

<br/>

# Data:  


Using AppTweak, a common ASO tool, I was able to grab app installs over the past few months. [Google Sheets Link](https://docs.google.com/spreadsheets/d/1V5BWqrTYwKHU7b4hOU5sH5TSzR234saXKdAe8UAoCoY/edit?usp=sharing). Here is the data plotted granularly at the daily level:

![alt]({filename}..\images\Dunzo\graph_1.png)  

These are just estimates. Being an external source, the numbers might be inaccurate. Choosing only the data with a confidence rating > 0.5. The results are:  

![alt]({filename}..\images\Dunzo\graph_2.png)  

I shall assume that the numbers for the iOS app follow a similar trend.

<br/>

# Hypotheses:  


1. First dip - 1st Wk March. can be attributed to the first coronavirus scare - resulting in users' lowering dependence on delivery platforms.  

2. Spike near 23rd March. With movement restricted and most shops closed, users got over the first scare and grew to be dependent on on-demand delivery platforms for groceries, medical supplies, and other essentials. The higher download rates around March 24 can be attributed to this.  

3. Dip after April 3rd Wk. With competition from new services like Swiggy Genie (formerly Swiggy Go), customer acquisition rates might lower. The dip can probably be attributed to this. <br/> However, given the data source’s lower confidence in these newer numbers, they might be inaccurate.   

<br/>

# Conlusion and direction for changes:  


We can conclude that since the # of new installs quickly recovered after the first scare, the COVID situation has presented a scenario where people who would not have used delivery platforms like Dunzo are willing to give them a try.  
  
This unique opportunity should be capitalized upon by making Dunzo even more attractive. This could be achieved by:   
1. Adding new features, 
2. Highlighting use-cases for existing features and 
3. Improving the overall experience

> '1' and '2' expand the top of the funnel, targeting user adoption, whereas, '3' specifically targets user retention.    

<br/>

# App Changes: 

## 1. Improve the Search:   
The search bar is one of the central processes of the Dunzo app's ordering process. I felt some friction while using the Search, and upon asking my friends, they felt the same. Here are some changes to Search:  

- The Search bar is present on the bottom navbar as well as on the top of the home screen. On the home page, users need to scroll below the fold to see the Dunzo Assistant card. As search can be accessed from the navbar, deleting the search bar on top will make this card more visible. Also, search bars on the "groceries", "meats" pages might also be directing to the same main page.  

![alt]({filename}..\images\Dunzo\1_search_fruits.png)    
![alt]({filename}..\images\Dunzo\1_search_grocery.png)    
![alt]({filename}..\images\Dunzo\1_search_meat.png)    
![alt]({filename}..\images\Dunzo\1_search_medicines.png)    
<br/>
  
- A user searches for an item and clicks on a store. They do not like it and press the back button. This takes the user back to the search page but the search results are cleared and the user has to perform the search again. Retaining the search results will reduce friction. 

This image illustrates what happens currently:
![alt]({filename}..\images\Dunzo\clear_searches.png)  

<br/>
- I would recommend a “filter” feature for the search. Users can restrict search results to certain categories (groceries, restaurants, etc) or sort results by price, completion time, etc.

- Searching items (like “tomato”) turns up multiple stores that offer them, but stores offering only “tomato ketchup” also appear in the search. A user has to individually go through every store to check which “tomato” product the store offers. This is tedious and increases the # of clicks required. To solve this, search results can display the related products that they offer along with the store details.

-  The search is sometimes unable to return relevant results when searching using synonymous keywords (potatoes instead of potato) or misspellings.
This can be fixed by putting an “intent listening” process before actually searching through the search catalog. 
When a user navigates to the groceries tab and searches “potato”, it should realize that the ‘user intent’ is to buy “potatoes” from a grocery store, and it is not to buy a “cheese potato roll” from a Faaso’s restaurant.
Mapping this user intent will also help to tackle searches in vernacular languages, for example when I type “bhindi” instead of “ladies finger”.

> KPIs: Monitor "avg # of clicks to complete an order", "avg # of searches per order", "avg # of searches per session", "% order conversion".




## 2. The UI should reflect Dunzo’s safety efforts:  

Reports of transmission of infections through delivery partners have negatively impacted the perception of all delivery-based apps.
It is important to reassure the users that Dunzo is taking all precautions possible to prevent the spread. These measures were published in Dunzo’s blog (https://bit.ly/2NJrmda) but it’s not visible enough.

Showcasing Dunzo’s efforts on the home page UI will ensure users feel at ease while ordering. 
Dunzo already shows the delivery partner icons wearing masks. However, due to low contrast, it's not very noticeable. Masks are just one out of the many measures undertaken by Dunzo (No contact delivery, Sanitization, Temperature Checks, etc.)

I would suggest that a card with information about these measures be displayed on the home screen. The information can be reaffirmed at other touchpoints too. Providing social proof (“14 people recently ordered from here” or “3 people in your area got it DUN”) during the order process will also help.

> KPIs: This will affect overall usage. I will monitor DAU, MAU, "% order conversion"




## 3. Improve the clarity of instructions in the ‘Dunzo Assistant’ and ‘Send Packages’ services:


I got my parents to fill a few hypothetical ‘Dunzo Assistant’ and ‘Send Packages’ orders, with the intention to test the app on digitally un-savvy customers. 
Their top concern was ensuring that their important package was delivered or their task was completed. 
They struggled to explain the task. I observed:

a. Being uncomfortable with English, they would’ve been able to do it better in vernacular languages - Hindi or Marathi.
b. Some explanations would be better explained by accompanying the text with visual aids - a photo or a video.

I recommend a feature for users to add voice notes (Just English or also in vernacular languages) and add images (eg. pictures of the product they want delivered) while using these two services. This will open up newer, more complicated use-cases to users, driving user adoption and retention.

> KPIs: Effectiveness will be measured through decrease in "# of support requests raised" or "# of tasks cancelled by partners" or increase in "% task success".

