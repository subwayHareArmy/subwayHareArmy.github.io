Title: DaanCorona Learnings <working title>
date: 2020-05-12 22:16
authors: Ayush Yembarwar
comments: false
slug: daancorona-learnings
tags: daancorona, learnings, statistics, experience
status: draft

<!-- PELICAN_BEGIN_SUMMARY -->  
![alt]({filename}../images/DaanCorona/DAANCORONA_LOGO.png)  <br>



**DaanCorona** is an online platform for **selling vouchers for India's largely undigitized** small and medium **businesses**. You can find it here - [https://daancorona.tech](https://daancorona.tech)

We built DaanCorona during the COVID-19 lockdown. In these efforts, my role was most similar to one of a **co-lead** (one of two) and a **PM** (Product Manager).   

<!-- I wore many hats, while at DaanCorona, often at the same time. I don't think it translated well, all the time. -->

<!-- PELICAN_END_SUMMARY -->

Here's an [interview](https://epcbits.wordpress.com/2020/05/23/daancorona-tech/) we did with the English Press Club at BITS Pilani. Here's [another](https://online.fliphtml5.com/hfdbv/vrzd/#p=9) with the Alumni Relations Cell.  

I already wrote an explanatory post regarding this social initiative, [here]({filename}../../pages/daancorona.html).  

This post, however, shall be about some learnings. Take them with a grain of salt.  

<br>


# Payment split  

We accepted payments using the Razorpay payments gateway. While this added a small overhead with the transaction fees, DaanCorona operates on goodwil and hence expecting the customers to cover it wasn't a problem.  

Splitting the transactions-related data can uncover some insights. While I have little data to make these claims, one can surely use these for giving direction for the next project's design decisions.   
  
## By mode of Payment: 

Here's our revenue split according to payment modes (by volume).  
<!-- INSERT SAKEY DIAGRAM HERE -->  



<style>#chartdiv{width:100%;height:600px}</style>
<script src="https://www.amcharts.com/lib/4/core.js"></script>
<script src="https://www.amcharts.com/lib/4/charts.js"></script>
<script src="https://www.amcharts.com/lib/4/themes/animated.js"></script>
<script>/*<![CDATA[*/am4core.ready(function(){am4core.useTheme(am4themes_animated);var c=am4core.create("chartdiv",am4charts.SankeyDiagram);c.data=[{from:"Cash in the U.S.",color:"#f47b20"},{from:"Cash Overseas",color:"#000000"},{from:"Source",to:"Total non financial companies",value:100,color:"#f47b20",labelText:"[font-size:1.5em]Revenue\nsplitup\n\nBy mode of payment\n\n[/]Total Volume (%) \n [bold]100%[/b]",zIndex:100},{from:"Total non financial companies",to:"UPI",value:76.08,color:"#f47b20"},{from:"Total non financial companies",to:"Card Payments",value:16.29,color:"#f47b20",labelText:"Cards\n [bold]16.29%[/]"},{from:"Total non financial companies",to:"Net Banking",value:7.63,color:"#f47b20"},{from:"UPI",to:"UPI_2",value:76.08,color:"#f47b20",labelText:"UPI\n [bold]76.08%[/]"},{from:"Card Payments",to:"Debit Card",value:11.199,color:"#f47b20",labelText:"Debit Cards [bold]11.2%[/]"},{from:"Card Payments",to:"Credit Card",value:5.091,color:"#f47b20",labelText:"Credit Cards [bold]5.09%[/]"},{from:"Net Banking",to:"Net Banking_2",value:7.63,color:"#f47b20",labelText:"Net Banking [bold]7.63%[/]"}];c.paddingRight=30;c.paddingTop=80;c.paddingBottom=80;c.nodeAlign="bottom";c.minNodeSize=0.001;c.dataFields.fromName="from";c.dataFields.toName="to";c.dataFields.value="value";c.dataFields.color="color";var b=c.links.template;b.colorMode="gradient";b.fillOpacity=1;b.strokeOpacity=1;b.cursorOverStyle=am4core.MouseCursorStyle.pointer;b.readerTitle="drag me!";b.showSystemTooltip=true;b.tooltipText="";b.propertyFields.zIndex="zIndex";b.tension=0.6;c.nodes.template.width=0;c.nodes.template.nameLabel.disabled=true;c.nodes.template.draggable=true;c.nodes.template.inert=true;c.nodes.template.togglable=false;b.events.on("down",function(i){var j=i.target.dataItem.fromNode;var g=i.target.dataItem.toNode;var h=am4core.math.getDistance(i.pointer.point,{x:j.pixelX,y:j.pixelY});var k=Infinity;if(g){k=am4core.math.getDistance(i.pointer.point,{x:g.pixelX,y:g.pixelY})}if(h<k){j.dragStart(i.pointer)}else{g.dragStart(i.pointer)}});var f=c.links.template.bullets.push(new am4charts.LabelBullet());f.label.propertyFields.text="labelText";f.propertyFields.locationX="labelLocation";f.propertyFields.rotation="labelRotation";f.label.horizontalCenter="left";f.label.textAlign="start";f.label.dx=-50;var a=c.links.template.bullets.push(new am4charts.LabelBullet());a.label.text="${value}";a.label.fill=am4core.color("#ffffff");a.label.isMeasured=false;a.isMeasured=false;c.events.on("inited",function(){for(var h=0;h<c.links.length;h++){var j=c.links.getIndex(h);var g=j.bullets.getIndex(1);g.opacity=0;if(j.dataItem.toNode&&j.dataItem.value>10){g.label.fontSize=j.dataItem.value/10;e(g)}else{j.bullets.removeValue(g)}}});function e(g){var i=6000*Math.random()+3000;var h=g.animate([{property:"locationX",from:0.2,to:0.5},{property:"opacity",from:0,to:0.3}],i);h.events.on("animationended",function(j){d(j.target.object,i)})}function d(g,i){var h=g.animate([{property:"locationX",from:0.5,to:0.8},{property:"opacity",from:0.3,to:0}],i);h.events.on("animationended",function(j){setTimeout(function(){e(j.target.object)},Math.random()*5000)})}});/*]]>*/</script>
<div id="chartdiv"></div>




<!-- INSERT SAKEY DIAGRAM HERE -->  
Despite having very little data, UPI payments clearly take the cake here. It accounts for more than 75% of the payment volume. Although UPI being a majority was expected, A 3/4 share was surprising. Knowing our largest customer demographic - young adults in the 17 to 25 year age bracket - I would attribute UPI as their payment method of choice.

> **Takeaway:** When targeting the young adult demographic, side with a payment gateway that supports UPI payment.   

The split for payment modes (by number of transactions) offers very similar percentages.

> **Takeaway:** Does this mean people are comfortable making both, small and large payments through the each payment method? Have very little data.
<br>


## By Traffic:

Our platform is composed of a consumer-facing website and a business-facing app. Vouchers are bought throught the website. The website traffic is split according to the mode of access.

Here's our revenue split according to access modes (by volume).  
<!-- INSERT SAKEY DIAGRAM HERE -->  



<style>#chartdiv_2{width:100%;height:600px}</style>
<script>/*<![CDATA[*/am4core.ready(function(){am4core.useTheme(am4themes_animated);var a=am4core.create("chartdiv_2",am4charts.SankeyDiagram);a.data=[{from:"Source",to:"Total Sales",value:100,color:"#f47b20",labelText:"[font-size:1.5em]Revenue\nsplitup\n\nBy mode of access\n\n[/]Total Volume (%) \n [bold]100%[/b]",zIndex:100},{from:"Total Sales",to:"Mobile Web",value:63.87,color:"#f47b20",labelText:"Mobile Web Users\n [bold]64%[/]"},{from:"Total Sales",to:"Desktop",value:36.13,color:"#f47b20",labelText:"Desktop Users\n [bold]36%[/]"}];a.paddingRight=30;a.paddingTop=80;a.paddingBottom=80;a.nodeAlign="bottom";a.minNodeSize=0.001;a.dataFields.fromName="from";a.dataFields.toName="to";a.dataFields.value="value";a.dataFields.color="color";var b=a.links.template;b.colorMode="gradient";b.fillOpacity=1;b.strokeOpacity=1;b.cursorOverStyle=am4core.MouseCursorStyle.pointer;b.readerTitle="drag me!";b.showSystemTooltip=true;b.tooltipText="";b.propertyFields.zIndex="zIndex";b.tension=0.6;a.nodes.template.width=0;a.nodes.template.nameLabel.disabled=true;a.nodes.template.draggable=true;a.nodes.template.inert=true;a.nodes.template.togglable=false;b.events.on("down",function(f){var g=f.target.dataItem.fromNode;var d=f.target.dataItem.toNode;var e=am4core.math.getDistance(f.pointer.point,{x:g.pixelX,y:g.pixelY});var h=Infinity;if(d){h=am4core.math.getDistance(f.pointer.point,{x:d.pixelX,y:d.pixelY})}if(e<h){g.dragStart(f.pointer)}else{d.dragStart(f.pointer)}});var c=a.links.template.bullets.push(new am4charts.LabelBullet());c.label.propertyFields.text="labelText";c.propertyFields.locationX="labelLocation";c.propertyFields.rotation="labelRotation";c.label.horizontalCenter="left";c.label.textAlign="start";c.label.dx=-50});/*]]>*/</script>
<div id="chartdiv_2"></div>



<!-- INSERT SAKEY DIAGRAM HERE --> 
A majority of the transactions have users accessing the mobile web version of the website. Data from Google Analytics also backs this claim - a majority of our users are mobile users.

> **Takeaway:** Designing mobile first or responsive websites is a necessity. Especially if the primary distribution channel is mobile-based (Instagram, WhatsApp, etc.).   

WhatsApp was the marketing channel that really worked for us (more on this later), so having a responsive website was a no-brainer.    

<br>



# Designing for the stakeholders

At some points in the design process, we were stuck because we had many options to choose from. One such situation was when we were deciding on the mechanic for by which customer would redeem vouchers.      
We brainstorming a couple of ideas but the team was divided over them. Eventually, I came up with arguments supporting a particular option and the team seeing truth in it, agreed as well. However, this pickle would've been avoided had we used our stakeholder analysis to give our brainstorming some direction. We wouldn't have ended up with the extra options in the first place. 

> **Takeaway:** Every new insight / analysis needs to be brought to the foreground and discussed, otherwise it's wasted on you.

Taking a step back helped us decide on the redeeming mechanic. DaanCorona's group of target businesses were undigitized, local micro and small businesses. We'd spoken to owners of such businesses during the idea validation phase and even before. We knew the kind of phones and apps they used, comfort levels with technology, their concerns and reservations. Most were scared of technology and learning to use new apps was a stressful undertaking. The customers who would buy our vouchers were however a digitally literate, tech-savvy bunch.        
Designing the product around these considerations was a guiding design principle for the DaanCorona platform. Keeping this in mind, we could take a decision on the voucher redeeming mechanic. We decided to go with a 'user-initiates-the redeeming-request' model. This would ensure minimum effort from the business owner's side.       

> **Takeaway:** User research in really useful if used to design around the user's constraints.   

We even tried to stick to the designs of e-wallets that they used often. The intention was to make DaanCorona seem familiar and non-intimidating, while ensuring that concepts and knowledge from using e-wallets transferred well. From our interacting with the business owners, this seemed to have worked well.          
<br>  
A Gantt chart mapping the workflow:

![alt]({filename}../images/DaanCorona/gantt_3.png)     

> **Note:** Observe, very few processes depend on the business's participation (coloured blue). This is **intentional** since we're targeting a group that isn't very tech-savvy; owners of un-digitized local businesses.
<br>  



# Long term plans and 'vision'

I always considered 'vision' to be a set of lofty and ambiguous ideals, a buzzword which is given undue importance. I never really understood its use.   
Yet, going through our vision again, made quick work of a few problems we were struggling with. I realized that the vision is like a codified version of the product's priorities and other guidelines, it helps keep things in perspective. I'm a believer now.  

> The vision should alse be seen as an asset used for problem solving.  

We turned to the product vision and found answers for questions like "Are advertisements featuring just a few businesses, okay?". 
<br>  



# Building Trust 

A [study](https://www.funraise.org/giving-report/past-reports) <sup>1</sup> reports that one reason why people are reluctant to donate money is that they **don’t trust charity organizations** to spend their money well. Our entire product rests upon the ideal that it is a better alternative to donations, so we had to address this issue.  

Businesses without an existing online presence often don't do well on online platforms, primarily due to a lack of trust from customers.  

<br>

We mean for DaanCorona to be an intermediary between the customers buying vouchers and businesses selling them. Just the act of being an intermediary, we expect, will introduce trust and accountability into the equation. Ben Thompson, while writing about Airbnb, wrote something similar. According to him, 
Apart from this, we signed MoU's (Memorandums of Understanding) with every partner business, customizing it programatically to be specific for each business. 

> Even if the MoU has no teeth, just having a legal document in the picture will do two things<br>
> -> Builds trust with customers<br>
> -> Convinces businesses owners that everything is legit

I am not endorsing fooling people, just pointing out that such actions positively affect the trust in the product.   

Through the MoU, we transfers the responsibility of honouring vouchers onto the business itself. DaanCorona simply acts as an intermediary and limits its liability. Even so, surprisingly, a majority of our customers do not find it very difficult to trust us or our partner businesses. 

> I suspect either:<br>
> -> The "be-an-intermediary" strategy by itself is successful at building trust, or, <br>
> -> We are still targeting the demographics which are okay with donating money.

<br>  



# Quality vs. Speed

[This is a draft]

For other great mental models, read [this article](https://blackboxofpm.com/product-management-mental-models-for-everyone-31e7828cb50b) by Brandon Chu.

<br>  




<br>

## Resources:  

- [Website](https://daancorona.tech/)
- [YouTube Video](https://www.youtube.com/watch?v=_OFUefO_Vvk)
- [Refer a business - App APK Link](https://daancorona.tech/download/DaanCorona.apk)
- [Volunteering Program](https://dare2compete.com/o/volunteering-daancorona-111139)
- [Twitter](https://twitter.com/DaanCoronaIndia)
- [LinkedIn](https://www.linkedin.com/company/daancorona/)
- [An Interview with the team](https://epcbits.wordpress.com/2020/05/23/daancorona-tech/)

## References:  

1. [2018 Global Trends in Giving Report](https://www.funraise.org/giving-report/past-reports)
2. Read through our [Terms of Service](https://daancorona.tech/terms/), [Privacy Policy](https://daancorona.tech/privacy/) and our [About](https://daancorona.tech/about/) sections.