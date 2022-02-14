# Youtube bot
## letting you shift the youtube algorithim to view another "side" of youtube

Youtube video recommendations rely heavly on a users watch history as well as feedback (likes, not interested, etc.).
Utilizing this I want to allow myself an automated way of shifting my Youtube recommendations or at least sprinkling 
in differnet topics I felt were missing or not represented enough in my recommended videos. 

Run `python youtubeScript.py`  (or `python3 youtubeScript.py` if python3 is not your default OS python) in the terminal.
You will be prompted to enter your youtube username, password and desired search topic. The script will take over from there
wathcing videos for 30 seconds to register as a view and then proceeding to go to the next video on the search page,
doing so until the loop is over. 

Once the loop is done feel free to check out your youtube homepage. In some instances depenidng upon the searhc topic and prior search history
the searched topic may not dominate the youtube homepage but he presence amongst the recommended videos will still remain higher 
than prior to running the script. 

If you are going to be downloading this for your own use:
- please make sure you have python3.1+ installed, as well as Selenium and undetected-chromedriver. 
- The `sleep()` calls can be altered to accomadate your average youtube loading time. 

### please share any feedback or suggestions you have ! 
