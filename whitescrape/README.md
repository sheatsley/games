## Whitescrape

This is *Whitescrape* - a repo for obtaining, parsing, and reasoning character
stats in [White
Noise 2](https://store.steampowered.com/app/503350/White_Noise_2/). White Noise
is a cooperative horror game where investigators have to solve puzzles and
collect objects while a creature hunts them. Each investigator has their own
unique stats, which are affected by choice of flashlight (likewise with
creatures). This code uses [Selenium](https://selenium.dev) to obtain character
stats off of the [White Noise 2
Wiki](https://white-noise-2.fandom.com/wiki/White_Noise_2_Wiki). Afterwards,
using a simple weighted sum, the best pairings of characters and equipment are
displayed. 

Note that the contents of this script and corresponding data are quite old
(around 2017) and largely outdated. I'm sure the wiki has changed and the DOM
properties I scan for no longer exist.

## How to use this repo
Requirements:
- Python 2
- Selenium `pip install selenium`

To scrape off the wiki (most likely broken at this point), simply uncomment
line 262 (```compass()```) and run ```python2 whitescrape.py```.

To show the best character and equipment combinations, just run ```python2
whitescrape.py```. To see how the weights influence the scores, manipulate the
values on lines 171-172:

```
# final stats are calculated as investigator/creature stat + (flashlight/idol stat) * weight
waagh_weights = {'Speed':        1.0, 'Endurance':   1.0, 'Range':   1.0, 
                 'Battery Life': 1.0, 'Exploration': 1.0, 'Stealth': 1.0}
```

If, for example, you'd prefer combinations with higher speed, increase the
`Speed` value. Conversely, if `Stealth` is not important, decrease its
value. I've found that preferring attributes with values `2.0-3.0` and
decreasing unimportant values to around `0.5` produces the
results that make the most sense.

With default values of `1.0`, you'll basically get well-rounded character and
equipment combinations. 
