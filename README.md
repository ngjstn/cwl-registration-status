# Automated CWL Registration Web Scraper 

Selenium-based web scraper to *hypothetically* automate course registration and provide updates on seat status availability for UBC CWL. 

> *dont use it though, it's against UBC ToS >:(*


### Installation 
If you were to ~~*hypothetically*~~ run this script, you would need to install the python selenium dependency, which can be done using the command: ```pip install selenium```

You also need a Chromedriver executable, which you could install [here](https://chromedriver.chromium.org/downloads) (this script only supports Google Chrome btw). Make sure to install the correct version corresponding to your browser version. Unzip the installed file and place ```chromedriver.exe``` into the directory called ```webdriver```. You'll likely need to update the driver path defined in the script to your machine's directory structure. Just ```shift + right click``` the file and copy the path, replacing the variable defined ```driver_exec_path``` with your new path in ```selenium_test.py```. 

If you run into a unicode error, try adding an extra ```/``` character bewteen directories: 

```
# BEFORE
driver_exec_path = "C:\Users\justi\OneDrive\Documents\cwl-registration-web-scrape\webdriver\chromedriver.exe"

# AFTER
driver_exec_path = "C:\\Users\\justi\\OneDrive\\Documents\\cwl-registration-web-scrape\\webdriver\\chromedriver.exe"
```
