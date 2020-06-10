# urlCroll.py

A simple python script which crawl all the anchor tab in a web page. I use this for Offline CTF chellenges (Vulnerable VMs), because the other advanced tools takes a bit longer to finish the scan. 
 
**Usage :**  

```shell  
$ python urlCroll.py <url>
``` 

**Example :**  

```shell  
$ python urlCroll.py https://google.com

https://https://www.google.co.in/imghp?hl=en&tab=wi
https://https://maps.google.co.in/maps?hl=en&tab=wl
https://https://play.google.com/?hl=en&tab=w8
https://https://www.youtube.com/?gl=IN&tab=w1
https://https://news.google.co.in/nwshp?hl=en&tab=wn
https://https://mail.google.com/mail/?tab=wm
https://https://drive.google.com/?tab=wo
https://https://www.google.co.in/intl/en/about/products?tab=wh
https://http://www.google.co.in/history/optout?hl=en
https:///preferences?hl=en
```  

To sort uniqe urls 

```shell 
$ python urlCroll.py https://google.com | sort -u
```
