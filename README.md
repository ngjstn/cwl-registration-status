# Automated CWL Registration Web Scraper 

Selenium-based web scraper to *hypothetically* automate course registration and provide updates on seat status availability for UBC CWL. 

The script is defined in the `CWLscraper` object located in `cwlscraper.py`, with all of the necessary functions defined in the object class.  

> *dont use it though, it's against UBC ToS >:(*


### Setup 
If you were to ~~hypothetically~~ run this script, you would need to install the python selenium dependency and a few other packages, which can be done using the commands: 
```
pip install selenium
pip install smtplib
pip install email
pip install pyyaml 
```

You also need a Chromedriver executable for Selenium, which you could install [here](https://chromedriver.chromium.org/downloads) (this script only supports Google Chrome btw). Make sure to install the correct version corresponding to your browser version. Unzip the installed file and place `chromedriver.exe` into the directory called `webdriver`. 

---

### SMS-Email Logistics :phone:
Email notifications are sent via Gmail from `cwlwebscrape@gmail.com`. Sending via SMS is done using a recipient's phone number appended to an email specific gateway domain that's dependent on the phone carrier.

I've included a function that parses phone numbers from different carriers, which should *hopefully* contain the correct appended SMS gateway domains, although I'm probably missing a few carriers (oops) or the domain has been deprecated. I referenced a few of them [here](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/), and the ones defined for this script can be found in `config.yaml`

Additionally, some carriers such as Shaw require extra prep work to initialize SMS-Email capabilities for your phone number. It's probably best that you look it up for yourself since it's likely different for everyone :(  

---

### Actually Running the Script 
Make sure you're in the correct directory `cwl-registration-web-scrape` when running the command: 
```
python cwlscraper.py 
# or run
python3 cwlscraper.py
``` 


