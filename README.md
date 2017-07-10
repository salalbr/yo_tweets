yo_tweets
========

Quick example showing how to use python to search tweets. Heavily based on [python-twitter-examples](https://github.com/ideoforms/python-twitter-examples).

Example
-------
```bash
$ python yo_tweets.py search --query superhero --cred credentials.py --since 2017-07-01 --until 2017-07-02
Query: superhero
Search complete: 0.098 seconds
(Sat Jul 01 23:59:59 +0000 2017) @jotalian2802 RT @EnzoZelocchi: #enzozelocchi  #hollywood #USA #california  #NYC #Hero #UK #England #films #awards #best #actor #actorslife #LA #USA #sup…
(Sat Jul 01 23:59:59 +0000 2017) @salley_jazmin RT @EnzoZelocchi: #enzozelocchi  #hollywood #USA #california  #NYC #Hero #UK #England #films #awards #best #actor #actorslife #LA #USA #sup…
(Sat Jul 01 23:59:44 +0000 2017) @HeirToTheMuscle @DeityOfWrath -sadness, while I fight outsiders who intend to conquer this world to fulfill my destiny as a superhero."
(Sat Jul 01 23:59:32 +0000 2017) @The7thMatrix Watch 'Captain Canuck' (@captaincanuck) - The Animated Series Ft. Canada's Premier Superhero! https://t.co/8NgH88GzFO #HappyCanadaDay
(Sat Jul 01 23:59:29 +0000 2017) @rvrsuperheroes The Batman #rvrsuperheroes #superhero #batman #DC #gotham https://t.co/67QeqfTCYc
(Sat Jul 01 23:59:25 +0000 2017) @the_superhero @Jeunelio Plat du pied sécurité.
(Sat Jul 01 23:59:00 +0000 2017) @wifey503 Become an IT Girl Superhero to share your love of @ITCosmetics (and win prizes!). Click here to sign up: #entry -… https://t.co/rVO53HS9gz
(Sat Jul 01 23:58:56 +0000 2017) @binkietae RT @gayhyungs: au where jeongguk is a superhero and keeps blowing off his dates with taehyung to save the world, until one day taehyung is…
(Sat Jul 01 23:58:56 +0000 2017) @the_superhero @l_unclephil Impossible, je n'ai pas fini de porter les vôtres
(Sat Jul 01 23:58:53 +0000 2017) @Surabhi31529435 RT @EricaClub: #SuperHero @Shaheer_S 🔥🔥🔥🔥🔥
````

Dependencies
-------
**Modules**:

[commandr](https://github.com/tellapart/commandr) - commandr is a simple tool
for making Python functions accessible from the command line.

[twitter](https://pypi.python.org/pypi/twitter) - an API and command-line
toolset for Twitter.
