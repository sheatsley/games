#!/usr/bin/env python

import json
import string

def compass():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    adblock = webdriver.FirefoxProfile()
    adblock.add_extension('/Users/Ryan/Library/Application Support/Firefox/Profiles/t2wo4ddp.default-1462685868246/extensions/{d10d0bf8-f5b5-c8b4-a8b2-2b9879e08c5d}.xpi')
    driver = webdriver.Firefox(firefox_profile=adblock)
    driver.implicitly_wait(10)
    try:
        complete_data = []
        flashlight_data = {}
        investigator_data = {}
        creature_data = {}
        idol_data = {}

        # investigators
        driver.get('http://white-noise-2.wikia.com/wiki/Investigators')
        web_elements = driver.find_elements_by_tag_name('ul')
        for element in web_elements:
            if element.find_elements_by_tag_name('li') is not None:
                if element.find_elements_by_tag_name('li')[0].text == 'Iker':
                    investigators = element.find_elements_by_tag_name('li')
                    break
        
        urls = []
        for investigator in investigators:
            urls.append((investigator.text, investigator.find_element_by_tag_name('a').get_attribute('href')))

        for url in urls:
            driver.get(url[1])
            print '\n--- ' + url[0] + ' ---'
            investigator_table = driver.find_elements_by_tag_name('tr')

            investigator_stats = {}
            for row in investigator_table:
                stat = row.find_element_by_tag_name('th').text
                val = row.find_element_by_tag_name('td').text
                investigator_stats[stat] = val
                print stat + ': ' + val
            investigator_data[url[0]] = investigator_stats

        # flaslights
        driver.get('http://white-noise-2.wikia.com/wiki/Flashlights')
        web_elements = driver.find_elements_by_tag_name('ul')
        for element in web_elements:
            if element.find_elements_by_tag_name('li') is not None:
                if element.find_elements_by_tag_name('li')[0].text == 'Basic Flashlight':
                    flashlights = element.find_elements_by_tag_name('li')
                    break
        
        urls = []
        for flashlight in flashlights:
            urls.append((flashlight.text, flashlight.find_element_by_tag_name('a').get_attribute('href')))

        for url in urls:
            driver.get(url[1])
            print '\n--- ' + url[0] + ' ---'
            flashlight_table = driver.find_elements_by_tag_name('tr')

            flashlight_stats = {}
            for row in flashlight_table:
                stat = row.find_element_by_tag_name('th').text
                val = row.find_element_by_tag_name('td').text
                flashlight_stats[stat] = val
                print stat + ': ' + val
            flashlight_data[url[0]] = flashlight_stats 

        # creatures
        driver.get('http://white-noise-2.wikia.com/wiki/The_Creature')
        web_elements = driver.find_elements_by_tag_name('ul')
        for element in web_elements:
            if element.find_elements_by_tag_name('li') is not None:
                if element.find_elements_by_tag_name('li')[0].text == 'Olkoth':
                    creatures = element.find_elements_by_tag_name('li')
                    break
        urls = []
        for creature in creatures:
            urls.append((creature.text, creature.find_element_by_tag_name('a').get_attribute('href')))
        
        for url in urls:
            driver.get(url[1])
            print '\n--- ' + url[0] + ' ---'
            creature_table = driver.find_elements_by_tag_name('tr')

            creature_stats = {}
            for row in creature_table:
                stat = row.find_element_by_tag_name('th').text
                val = row.find_element_by_tag_name('td').text
                creature_stats[stat] = val
                print stat + ': ' + val
            creature_data[url[0]] = creature_stats 

        # idols
        driver.get('http://white-noise-2.wikia.com/wiki/Idols')
        web_elements = driver.find_elements_by_tag_name('ul')
        for element in web_elements:
            if element.find_elements_by_tag_name('li') is not None:
                if element.find_elements_by_tag_name('li')[0].text == 'Blister':
                    idols = element.find_elements_by_tag_name('li')
                    break
        urls = []
        for idol in idols:
            urls.append((idol.text, idol.find_element_by_tag_name('a').get_attribute('href')))
        
        for url in urls:
            driver.get(url[1])
            print '\n--- ' + url[0] + ' ---'
            idol_table = driver.find_elements_by_tag_name('tr')

            idol_stats = {}
            for row in idol_table:
                stat = row.find_element_by_tag_name('th').text
                val = row.find_element_by_tag_name('td').text
                idol_stats[stat] = val
                print stat + ': ' + val
            idol_data[url[0]] = idol_stats 

        # cleanup
        complete_data.append(investigator_data)
        complete_data.append(flashlight_data)
        complete_data.append(creature_data)
        complete_data.append(idol_data)
        with open('whitenoise_data.json', 'w') as wn:
            json.dump(complete_data, wn)
        driver.quit()
        print '\n Scraping complete'

    except Exception,e:
        print str(e)
        driver.quit()

def scream():

    with open('whitenoise_data.json', 'r') as wn:
        complete_data = json.load(wn)

    investigator_data = complete_data[0]
    flashlight_data = complete_data[1]
    creature_data = complete_data[2]
    idol_data = complete_data[3]
    investigator_scores = []
    flashlight_scores = []
    creature_scores = []
    idol_scores = []
    investigator_flashlight_scores = []
    investigator_weights = {'Speed':              1.0, 'Endurance':   1.0, 
                            'Bravery':            1.0, 'Exploration': 1.0, 
                            'Battery Management': 1.0, 'Vitality':  1.0,
                            'Stealth':            1.0}
        
    flashlight_weights =   {'Speed':              1.0, 'Endurance':       1.0,
                            'Range':              1.0, 'Spread':          1.0,
                            'Battery Life':       1.0, 'Exploration':     1.0,
                            'Stealth':            1.0}

    creature_weights =     {'Speed':              7.0/7, 'Skill Usage':      6.0/7,
                            'Horror':             5.0/7, 'Light Resistance': 4.0/7,
                            'Perception':         3.0/7, 'Idol Influence':   2.0/7,
                            'Strength':           1.0/7}

    idol_weights =         {'Horror':             2.0/2, 'Range':            1.0/2}

    # final stats are calculated as investigator/creature stat + (flashlight/idol stat) * weight
    waagh_weights = {'Speed':        1.0, 'Endurance':   1.0, 'Range':   1.0, 
                     'Battery Life': 1.0, 'Exploration': 1.0, 'Stealth': 1.0}

    for investigator in investigator_data:
        score = 0.0
        for stat in investigator_data[investigator]:
            score = score + int(investigator_data[investigator][stat]) * investigator_weights[stat]
        investigator_scores.append([score, investigator]) 

    for flashlight in flashlight_data:
        score = 0.0
        for stat in flashlight_data[flashlight]:
            score = score + int(flashlight_data[flashlight][stat]) * flashlight_weights[stat]
        flashlight_scores.append([score, flashlight]) 
                
    for creature in creature_data:
        score = 0.0
        for stat in creature_data[creature]:
            score = score + int(creature_data[creature][stat]) * creature_weights[stat]
        creature_scores.append([score, creature]) 

    for idol in idol_data:
        score = 0.0
        for stat in idol_data[idol]:
            score = score + int(idol_data[idol][stat]) * idol_weights[stat]
        idol_scores.append([score, idol]) 

    for investigator in investigator_data:
        for flashlight in flashlight_data:
            contribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            score = 0.0
            num_affected = 0
            for stat in investigator_data[investigator]:
                if stat == 'Speed' or stat == 'Endurance' or stat == 'Exploration' or stat == 'Stealth':
                    score = score + int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight][stat]) - 5)*waagh_weights[stat]*flashlight_weights[stat]
                    if stat == 'Speed':
                        contribution[0] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight][stat]) - 5)*waagh_weights[stat]*flashlight_weights[stat]
                    elif stat == 'Endurance':
                        contribution[1] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight][stat]) - 5)*waagh_weights[stat]*flashlight_weights[stat]
                    elif stat == 'Exploration':
                        contribution[2] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight][stat]) - 5)*waagh_weights[stat]*flashlight_weights[stat]
                    elif stat == 'Stealth':
                        contribution[3] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight][stat]) - 5)*waagh_weights[stat]*flashlight_weights[stat]
                    else:
                        raise
                elif stat == 'Battery Management':
                    x1 = int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight]['Battery Life']) - 5)*waagh_weights['Battery Life']*flashlight_weights['Battery Life']
                    x2 = x1 + int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight]['Range']) - 5)*waagh_weights['Range']*flashlight_weights['Range']
                    score = score + (x2/2)
                    contribution[4] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight]['Battery Life']) - 5)*waagh_weights['Battery Life']*flashlight_weights['Battery Life']
                    contribution[5] += int(investigator_data[investigator][stat])*investigator_weights[stat] + (int(flashlight_data[flashlight]['Range']) - 5)*waagh_weights['Range']*flashlight_weights['Range']
                else:
                    score = score + int(investigator_data[investigator][stat])*investigator_weights[stat]
                    if stat == 'Vitality':
                        contribution[6] += int(investigator_data[investigator][stat])*investigator_weights[stat]
                    elif stat == 'Bravery':
                        contribution[7] += int(investigator_data[investigator][stat])*investigator_weights[stat]
                    else:
                        raise
            score = score + (int(flashlight_data[flashlight]['Spread']) - 5)*flashlight_weights['Spread']
            contribution[8] += (int(flashlight_data[flashlight]['Spread']) - 5)*flashlight_weights['Spread']
            investigator_flashlight_scores.append([score, [investigator, flashlight]])
            for val in contribution:
                print str(round(val,2)) + ' ',
            print investigator + ' ' + flashlight
            

    print ' '
    print contribution
    print ' --- Investigators --- '
    for investigator in sorted(investigator_scores):
        print str(investigator[0]) + ': ' + investigator[1]

    print '\n --- Flashlights --- '
    for flashlight in sorted(flashlight_scores):
        print str(flashlight[0]) + ': ' + flashlight[1]

    print '\n --- Creatures --- '
    for creature in sorted(creature_scores):
        print str(creature[0]) + ': ' + creature[1]

    print '\n --- Idols --- '
    for idol in sorted(idol_scores):
        print str(idol[0]) + ': ' + idol[1]

    print '\n --- Investigator + Flashlights --- '
    for investigator_flashlight in sorted(investigator_flashlight_scores):
        print str(investigator_flashlight[0]) + ': ' + investigator_flashlight[1][0] + ' - ' + investigator_flashlight[1][1]



#compass()
scream()
