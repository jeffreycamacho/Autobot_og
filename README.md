Context: 

In the world of sales, speed to lead is key. Specially for warm, ready to buy leads. Our company had a double booking system to increase show rate to maximize the Closer's time. When 2 Financially qualified (FQ) prospects would show up at the same time, the 1 prospect gets marked as a "Double booking" in our CRM by the Closer. 

This triggers an automation to send to a Slack channel to notify the setters to call this person ASAP, triage and reschedule for a better time. To claim these leads, a setter must be the first to comment on the thread to claim the lead. From the beginning, it was obvious that the best set up wins. Hard wired internet, fast computer, etc. 

The Pereto Principle was obvious. 80% of the leads were being claimed by 20% of the setters. 

Now, waiting for these leads were inefficient. So I decided to program a robot written in Python to scan my screen for notifications that came from this channel, and it would automatically click that notification to comment on the thread. 

Version 1 code is this baby. The win rate for it was about 55% over a course of 30 days. My win rate manually was 65%. The robot worked, but it has limitations. It depended on internet speed, and how fast Slack can handle operations. Slack isn't a fast application so each step needed a wait time of at least .02 seconds and that adds up. The only way around this was to get API access to Slack to make direct calls to perform actions. 

However, due to the security of the organization, the our Slacks admins weren't too happy when I was asking for API keys. 

So Version 2 was built on a no-code app called Make.com, on this version, for some reason, it allowed API access by just logging into my Slack account to intergrate both softwares. I could of probably figured this out via Python but that would of taken more time, time which could of been used to claim more Golden Gooses. This version worked PERFECTLY it had a 95% win rate. It was so good, it forced the sales managers to change the rules. Instead of Free-for-all, hungriest dogs eats first rules... the rules were changed to round robin. Thus ending the month and a half reign of the Golden Goose Bot.

I still want to share the code of Version 1 because it was the first real project I ever set out to do on my own. 
