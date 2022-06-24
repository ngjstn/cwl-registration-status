# Automated CWL Registration Web Scraper 

Selenium-based web scraper to *hypothetically* automate course registration and provide updates on seat status availability for UBC CWL. 

> *dont use it though, it's against UBC ToS >:(*



### Setup 
If you were to ~~*hypothetically*~~ run this script, you would need to install the python selenium dependency, which can be done using the command: 
```
pip install selenium
```

You also need a Chromedriver executable, which you could install [here](https://chromedriver.chromium.org/downloads) (this script only supports Google Chrome btw). Make sure to install the correct version corresponding to your browser version. Unzip the installed file and place ```chromedriver.exe``` into the directory called ```webdriver```. You'll likely need to update the driver path defined in the script to your machine's directory structure. Just ```shift + right click``` the file and copy the path, replacing the variable defined ```driver_exec_path``` with your new path in ```automation.py```. 

If you run into a unicode error, try adding an extra ```/``` character bewteen directories: 

```
# BEFORE
driver_exec_path = "C:\Users\justi\OneDrive\Documents\cwl-registration-web-scrape\webdriver\chromedriver.exe"

# AFTER
driver_exec_path = "C:\\Users\\justi\\OneDrive\\Documents\\cwl-registration-web-scrape\\webdriver\\chromedriver.exe"
```

This script also imports from packages ```email``` and ```smtplib```, which should be standard python libraries, but if for whatever reason you don't have it installed, go ahead and grab those using these commands: 
``` 
pip install email 
pip install smtplib
```

---

### Phone Carrier Logistics :phone:
I've included a function that parses phone numbers from different carriers, ```parse_phone_number()```, which should *hopefully* contain the correct appended SMS gateway domains, although I'm probably missing a few carriers (oops) or the domain has been deprecated. I referenced a few of them [here](https://www.digitaltrends.com/mobile/how-to-send-a-text-from-your-email-account/).

Additionally, some carriers such as Shaw require some extra prep work to initialize SMS-Email capabilities for your phone number. It's probably best that you look it up for yourself since it's likely different for everyone :(  

---

### Actually Running the Script :japanese_ogre: 
Make sure you're in the correct directory ```cwl-registration-web-scrape``` when running the command: 
```
python automation.py
`` 
