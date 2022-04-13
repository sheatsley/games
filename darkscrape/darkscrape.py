#!/usr/bin/env python

import math
import time
import random
import json
import urllib
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def obtain():

    driver = webdriver.Firefox()
    try:
        urls = []
        with open('armor_urls.json', 'r') as a:
            urls = json.load(a)

        driver.get('http://darksouls3.wiki.fextralife.com/Armor')
        armor_links = driver.find_element_by_class_name('col-sm-3')
        hyperlinks = armor_links.find_elements_by_class_name('wiki_link')
        for link in hyperlinks:
            print link.get_attribute('href')
            if link.get_attribute('href') not in urls:
                urls.append(link.get_attribute('href'))

        with open('armor_urls.json', 'w') as a:
            json.dump(urls, a)

    except Exception,e:
        print str(e)
        driver.quit()

def scrape():

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    try:
        data = {} 
        with open('armor_urls.json', 'r') as a, open('darksouls_complete_data.json', 'r') as d:
            armor_urls = json.load(a)
            data = json.load(d)

        caught_up = False 
        for armor in armor_urls:
            if armor == 'http://darksouls3.wiki.fextralife.com/Black+Leather+Set':
                caught_up = True
            if caught_up:
                driver.get(armor)

                pieces = driver.find_elements_by_class_name('col-sm-3')
                print len(pieces)
                looks_good = False
                for piece in pieces:
                    num_grabbed = 0
                    grab_next = False
                    skip_next = False
                    values = {'physical': '0', 'strike': '0', 'slash': '0', 'thrust': '0', 'weight': '0', \
                            'bleed': '0', 'poison': '0', 'frost': '0', 'curse': '0', 'poise': '0', \
                            'magic': '0', 'fire': '0', 'lightning': '0', 'dark': '0', 'durability': '0'}

                    if len(piece.find_elements_by_class_name('wiki_link')) == 0:
                        print 'failed'
                        break # DO NOT BREAK - YOU NEED TO SKIP, NOT BREAK SCRUB
                    armor_name = piece.find_element_by_class_name('wiki_link').text
                    print '======= ' + armor_name + ' =======' 
                    for cells in piece.find_elements_by_tag_name('td'):
                        print '--> ' + cells.get_attribute('innerHTML')[:150]
                        if '&nbsp;' in cells.get_attribute('innerHTML'):
                            skip_next = True
                        if grab_next:
                            if num_grabbed == 0:
                                values['physical'] = cells.text
                            elif num_grabbed == 1:
                                values['bleed'] = cells.text
                            elif num_grabbed == 2:
                                values['strike'] = cells.text
                            elif num_grabbed == 3:
                                values['poison'] = cells.text
                            elif num_grabbed == 4:
                                values['slash'] = cells.text
                            elif num_grabbed == 5:
                                values['frost'] = cells.text
                            elif num_grabbed == 6:
                                values['thrust'] = cells.text
                            elif num_grabbed == 7:
                                values['curse'] = cells.text
                            elif num_grabbed == 8:
                                values['magic'] = cells.text
                            elif num_grabbed == 9:
                                values['poise'] = cells.text
                            elif num_grabbed == 10:
                                values['fire'] = cells.text
                            elif num_grabbed == 11:
                                values['lightning'] = cells.text
                            elif num_grabbed == 12:
                                values['durability'] = cells.text
                            elif num_grabbed == 13:
                                values['dark'] = cells.text
                            elif num_grabbed == 14:
                                values['weight'] = cells.text
                                data[armor + '_' + armor_name] = values
                                print 'Finished ' + str(armor_name) + '\n' + \
                                        'physical: ' + str(values['physical']) + ' \tbleed: ' + str(values['bleed']) + \
                                        '\nstrike: ' + str(values['strike']) + ' \tposion: ' + str(values['poison']) + \
                                        '\nslash: ' + str(values['slash']) + ' \tfrost: ' + str(values['frost']) + \
                                        '\nthrust: ' + str(values['thrust']) + ' \tcurse: ' + str(values['curse']) + \
                                        '\nmagic: ' + str(values['magic']) + ' \tpoise: ' + str(values['poise']) + \
                                        '\nfire: ' + str(values['fire']) + '\nlightning: ' + str(values['lightning']) + \
                                        ' \tdurability: ' + str(values['durability']) + '\ndark: ' + str(values['dark']) + \
                                        ' \tweight: ' + str(values['weight'])
                                #if not looks_good:
                                    #input('Look good?')
                                    #looks_good = True
                                with open('darksouls_complete_data.json', 'w') as d:
                                    json.dump(data, d)
                                break
                            else:
                                print 'CRITICAL ERROR: GRABBED TOO MUCH'
                                driver.quit()

                            num_grabbed = num_grabbed + 1
                            grab_next = False
                        elif not skip_next:
                            DOM = cells.find_element_by_tag_name('img').get_attribute('title')
                            if 'Physical Resitance' in DOM or 'Strike Defense' in DOM or 'Slash Defense' in DOM or \
                                    'Thrust Defense' in DOM or 'weight.png' in DOM or 'physicaldef.png' in DOM or \
                                    'strikedef.png' in DOM or 'slashdef.png' in DOM or 'thrustdef.png' in DOM or \
                                    'Bleed Resistance' in DOM or 'Poison Resistance' in DOM or 'Frost Resistance' in DOM or \
                                    'Curse Resistance' in DOM or 'Magic Defense' in DOM or 'Poise' in DOM or \
                                    'Fire Defense' in DOM or 'Dark Defense' in DOM or 'Lightning Defense' in DOM or \
                                    'durability.png' in DOM or 'durabilitiy' in DOM or 'bleedres.png' in DOM or \
                                    'magicdef.png' in DOM or 'firedef.png' in DOM or 'lightningdef.png' in DOM or \
                                    'darkdef.png' in DOM:
                                        grab_next = True
                                        print '<-- Obtaining ' + DOM
                            else:
                                skip_next = True
                                print '<-- Skipping...'
                        else:
                            skip_next = False

                print 'Sleeping for 7 for ' + armor 
                time.sleep(7)
    except Exception,e:
        print str(e)
        driver.quit()

def verify():
    #with open('darksouls_complete_data.json', 'r') as d, open('armor_urls.json', 'r') as u:
    with open('darksouls_complete_data.json', 'r') as d, open('armor_urls.json', 'r') as u:
        data = json.load(d)
        urls = json.load(u)

    for url in urls:
        found = False
        for armors in data.keys():
            if url in armors:
                found = True
        if not found:
            print 'Did not find: ' + url

    for armor in data:
        if data[armor]['weight'] == '0':
            print 'ERROR: ' + armor + ' appears to be incomplete... \n\t' + data[armor]

def analyse():
    with open('darksouls_complete_data.json', 'r') as d:
        data = json.load(d)

    helms = {} 
    chests = {}
    gloves = {}
    leggings = {}
    phelms = {} 
    pchests = {} 
    pgloves = {} 
    plegs = {} 
    for armor in data:
        # Rounded with elemental 
        point = float(data[armor]['fire'])*1.0 + float(data[armor]['lightning'])*1.0 + float(data[armor]['physical']) + float(data[armor]['slash']) + \
                float(data[armor]['thrust']) + float(data[armor]['strike'])*0.0 + float(data[armor]['magic'])*0.0

        # Rounded without elemental 
        #point = float(data[armor]['physical']) + float(data[armor]['slash']) + float(data[armor]['thrust']) + float(data[armor]['strike']) 

        # Strike
        #point = float(data[armor]['strike'])

        # Thrust 
        #point = float(data[armor]['thrust'])

        # Slash 
        #point = float(data[armor]['slash'])

        # Physical 
        #point = float(data[armor]['physical'])

        worth = point/float(data[armor]['weight'])

        if 'Helm' in armor or 'Hat' in armor or 'Hood' in armor or 'Mask' in armor or 'Crown' in armor or 'Blindfold' \
                in armor:
                    helms[armor] = worth
                    phelms[armor] = point
        elif 'Chest' in armor or 'Overcoat' in armor or 'Armor' in armor or 'Robe' in armor or 'Garb' in armor or 'Coat' \
                in armor or 'Dress' in armor or 'Vest' in armor or 'Attire' in armor or 'Chain Mail' in armor or 'Gown' in armor \
                or 'Amor' in armor:
                    chests[armor] = worth
                    pchests[armor] = point
        elif 'Guantlet' in armor or 'Gloves' in armor or 'Bracelets' in armor or 'Manchettes' in armor or 'Gauntlet' in armor \
                or 'Wrap' in armor:
                    gloves[armor] = worth
                    pgloves[armor] = point
        elif 'Leggings' in armor or 'Trousers' in armor or 'Skirt' in armor or 'Boots' in armor or 'Waistcloth' in armor:
            leggings[armor] = worth
            plegs[armor] = point
        else:
            print 'MISSING: ' + armor
            raise

    bhelms = sorted(helms, key=helms.get, reverse=True)
    bchests = sorted(chests, key=chests.get, reverse=True)
    bgloves = sorted(gloves, key=gloves.get, reverse=True)
    blegs = sorted(leggings, key=leggings.get, reverse=True)
    
    bphelms = sorted(phelms, key=phelms.get, reverse=True)
    bpchests = sorted(pchests, key=pchests.get, reverse=True)
    bpgloves = sorted(pgloves, key=pgloves.get, reverse=True)
    bplegs = sorted(plegs, key=plegs.get, reverse=True)

    '''
    print '=== Helmets ==='
    for helm in bphelms:
        print '{:>30} -{:2}-> {:4.3} ({:5.2}) | {:>4} -{:5.4} ({:>5.2}) | {:6.2} '.format( \
                helm.split('_')[len(helm.split('_'))-1], \
                bphelms.index(helm), \
                helms[helm], \
                float(bhelms.index(helm))/len(bhelms), \
                phelms[helm], \
                '0.00' if bphelms.index(helm) == 0 else  \
                str(phelms[bphelms[0]] - phelms[helm])[:3], \
                float(bphelms.index(helm))/len(bphelms), \
                float(bphelms.index(helm))/len(bphelms)-float(bhelms.index(helm))/len(bhelms))
    print '\n=== Chests ==='
    for helm in bpchests:
        print '{:>30} -{:2}-> {:4.3} ({:5.2}) | {:>4} -{:5.4} ({:>5.2}) | {:6.2} '.format( \
                helm.split('_')[len(helm.split('_'))-1], \
                bpchests.index(helm), \
                chests[helm], \
                float(bchests.index(helm))/len(bchests), \
                pchests[helm], \
                '0.00' if bpchests.index(helm) == 0 else  \
                str(pchests[bpchests[0]] - pchests[helm])[:3], \
                float(bpchests.index(helm))/len(bpchests), \
                float(bpchests.index(helm))/len(bpchests)-float(bchests.index(helm))/len(bchests))
    print '\n=== Gloves ==='
    for helm in bpgloves:
        print '{:>30} -{:2}-> {:4.3} ({:5.2}) | {:>4} -{:5.4} ({:>5.2}) | {:6.2} '.format( \
                helm.split('_')[len(helm.split('_'))-1], \
                bpgloves.index(helm), \
                gloves[helm], \
                float(bgloves.index(helm))/len(bgloves), \
                pgloves[helm], \
                '0.00' if bpgloves.index(helm) == 0 else  \
                str(pgloves[bpgloves[0]] - pgloves[helm])[:3], \
                float(bpgloves.index(helm))/len(bpgloves), \
                float(bpgloves.index(helm))/len(bpgloves)-float(bgloves.index(helm))/len(bgloves))
    print '\n=== Legs ==='
    for helm in bplegs:
        print '{:>30} -{:2}-> {:4.3} ({:5.2}) | {:>4} -{:5.4} ({:>5.2}) | {:6.2} '.format( \
                helm.split('_')[len(helm.split('_'))-1], \
                bplegs.index(helm), \
                leggings[helm], \
                float(blegs.index(helm))/len(blegs), \
                plegs[helm], \
                '0.00' if bplegs.index(helm) == 0 else  \
                str(plegs[bplegs[0]] - plegs[helm])[:3], \
                float(bplegs.index(helm))/len(bplegs), \
                float(bplegs.index(helm))/len(bplegs) - float(blegs.index(helm))/len(blegs))
        '''

    print '\t\t\t\t\t\t\t\tThere are {} helmets, {} gloves, {} chests, & {} legs'.format(len(bphelms), len(bpgloves), len(bpchests), len(bplegs))
    print ' ========================================== Helmets ==========================================  @@@  ========================================== Gloves ========================================== '
    for helm, glove in zip(bphelms, bpgloves):
        print '{:>30} - {:02} -> {:05.2f} ({:04.1f}%) | {:4.1f} -{:0>5.2f} ({:04.1f}%) | {: >5.2f} \t\t|||\t '.format( \
                helm.split('_')[len(helm.split('_'))-1], \
                bphelms.index(helm)+1, \
                float(helms[helm]), \
                float(bhelms.index(helm))/len(bhelms)*100, \
                float(phelms[helm]), \
                0.00 if bphelms.index(helm) == 0 else  \
                float(phelms[bphelms[0]] - phelms[helm]), \
                float(bphelms.index(helm))/len(bphelms)*100, \
                float(bphelms.index(helm))/len(bphelms)-float(bhelms.index(helm))/len(bhelms)) + \
              '{:>30} - {:02} -> {:05.2f} ({:04.1f}%) | {:4.1f} -{:0>5.2f} ({:04.1f}%) | {: >5.2f}'.format( \
                glove.split('_')[len(glove.split('_'))-1], \
                bpgloves.index(glove)+1, \
                float(gloves[glove]), \
                float(bgloves.index(glove))/len(bgloves)*100, \
                float(pgloves[glove]), \
                0.00 if bpgloves.index(glove) == 0 else  \
                float(pgloves[bpgloves[0]] - pgloves[glove]), \
                float(bpgloves.index(glove))/len(bpgloves)*100, \
                float(bpgloves.index(glove))/len(bpgloves)-float(bgloves.index(glove))/len(bgloves))

    print '\n ========================================== Chests ==========================================   @@@   ========================================== Legs ========================================== '
    for chest, leg in zip(bpchests, bplegs):
        print '{:>30} - {:02} -> {:05.2f} ({:04.1f}%) | {:4.1f} -{:0>5.2f} ({:04.1f}%) | {: >5.2f} \t\t|||\t '.format( \
                chest.split('_')[len(chest.split('_'))-1], \
                bpchests.index(chest)+1, \
                chests[chest], \
                float(bchests.index(chest))/len(bchests)*100, \
                float(pchests[chest]), \
                0.00 if bpchests.index(chest) == 0 else  \
                float(pchests[bpchests[0]] - pchests[chest]), \
                float(bpchests.index(chest))/len(bpchests)*100, \
                float(bpchests.index(chest))/len(bpchests)-float(bchests.index(chest))/len(bchests)) + \
               '{:>30} - {:02} -> {:05.2f} ({:04.1f}%) | {:4.1f} -{:0>5.2f} ({:04.1f}%) | {: >5.2f}'.format( \
                leg.split('_')[len(leg.split('_'))-1], \
                bplegs.index(leg)+1, \
                float(leggings[leg]), \
                float(blegs.index(leg))/len(blegs)*100, \
                float(plegs[leg]), \
                0.00 if bplegs.index(leg) == 0 else  \
                float(plegs[bplegs[0]] - plegs[leg]), \
                float(bplegs.index(leg))/len(leg)*100, \
                float(bplegs.index(leg))/len(bplegs)-float(blegs.index(leg))/len(blegs))

    print '\nYour current metrics and weights for analysis: '
    with open('darkscrape.py', 'r') as d:
        for i, line in enumerate(d):
            if i >= 182 and i <= 200:
                print line,

    print 'Compiling results... This may take awhile...'
    current_iteration = 1
    final_iteration = len(pchests) * len(plegs) * len(phelms) * len(pgloves)
    max_equip_load = 60.0
    #initial_equip_load = 8.50 # darksword + caestus + yorksha's chime
    #initial_equip_load = 11.5 # astora greatsword + yorksha's chime
    initial_equip_load = 13.5 # zweilhander greatsword + yorksha's chime 
    desired_roll = 70.00
    results = {}
    for chests in pchests:
        for legs in plegs:
            for helms in phelms:
                for gloves in pgloves:
                    weight_points = float(data[chests]['weight']) + float(data[legs]['weight']) + \
                            float(data[gloves]['weight']) + float(data[helms]['weight'])
                    if float((weight_points + initial_equip_load)/max_equip_load)*100 < desired_roll:
                        results[chests.split('_')[len(chests.split('_'))-1] + ' <> ' + \
                                legs.split('_')[len(legs.split('_'))-1] + ' <> ' + \
                                helms.split('_')[len(helms.split('_'))-1] + ' <> ' + \
                                gloves.split('_')[len(gloves.split('_'))-1]] = \
                                pchests[chests] + plegs[legs] + phelms[helms] + pgloves[gloves]
                    current_iteration = current_iteration + 1
                    print str(current_iteration) + '/' + str(final_iteration) + '    ' + \
                            str(float(current_iteration)/float(final_iteration)*100.00)[:4] + '%' + '\r',

    print '\n\nComplete: ' + str((float(len(results))/final_iteration)*100)[:4] + \
        '% armor combinations meet the criteria of less than ' + str(desired_roll) + \
        '% roll with initial load of ' + str(float(initial_equip_load/max_equip_load)*100)[:2] + '%\nSorting...'
    sorted_results = sorted(results, key=results.get, reverse=True)
    print '\n ===== Top Combinations ===== '
    x = 0
    for armor_set in sorted_results:
        print '{:>2}: {:40} === {:>6}'.format( \
            x, \
            armor_set, \
            results[armor_set])
        x = x + 1
        if x == 10:
            break
# for the future, you wanted to scrape weapon atk type data to determine, assuming an equally likely distrubition of weapon choice,
# what kinds of attacks are you most likely to experience? The idea is that these % could then be used as input to the weights for defence
# However, in PvP, we do not see such a distribution: there is a 'pool' of weapons most people use, favoring straight-swords, then UGS/GS, etc.

def main():
    #obtain()
    #scrape()
    #verify()
    analyse()

main()
