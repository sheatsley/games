## Darkscrape 

This is *Darkscrape* - a repo for obtaining, parsing, and reasoning character
stats in [Dark Souls
2](https://darksouls2.wiki.fextralife.com/Dark+Souls+2+Wiki). Dark Souls 2 is a
action role playing game where players explore a vast world and a cryptic
storyline to develop a sense of purpose. Within the game, players may encounter
other players who seek to aid or harm their progress. These encounters motivate
the purpose of this repo - by computing the most optimal equipment pairings,
players can be prepared for the most difficult encounters. This code uses
[Selenium](https://selenium.dev) to obtain character stats off of the [Dark
Souls 2 Wiki](https://darksouls2.wiki.fextralife.com/Dark+Souls+2+Wiki).
Afterwards using a simple weighted sum, the best pairings of equipment are
displayed, given a weight constraint. This is reducible to a [knapsack
problem](https://en.wikipedia.org/wiki/Knapsack_problem).

Note that the contents of this script and corresponding data are quite old
(around 2015) and largely outdated. I'm sure the wiki has changed and the DOM
properties I scan for no longer exist.

## How to use this repo
Requirements:
- Python 2
- Selenium `pip install selenium`

To scrape off the wiki (most likely broken at this point), simply uncomment
line 382 and 383 (`obtain()` & `scrape()`) and run ```python2 darkscrape.py```.

To show the best character and equipment combinations, just run ```python2
darkscrape.py```. To see how the weights influence the scores, manipulate the
values on lines 183-200:

```
# Rounded with elemental 
point = float(data[armor]['fire'])*1.0 + float(data[armor]['lightning'])*1.0 +
            float(data[armor]['physical']) + float(data[armor]['slash']) + 
            float(data[armor]['thrust']) + float(data[armor]['strike'])*0.0 + 
            float(data[armor]['magic'])*0.0
```

With default values of `1.0`, you'll basically get well-rounded character and
equipment combinations. 

Furthermore, you can specify the maximum allowable weight (`max_equp_load`),
only show equipment under a certain weight (`desired_roll`), and other
parameters on lines 341-345.

```
max_equip_load = 60.0
#initial_equip_load = 8.50 # darksword + caestus + yorksha's chime
#initial_equip_load = 11.5 # astora greatsword + yorksha's chime
initial_equip_load = 13.5 # zweilhander greatsword + yorksha's chime 
desired_roll = 70.00
```
