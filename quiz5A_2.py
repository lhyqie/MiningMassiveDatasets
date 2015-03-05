data = [
{'name': 'A', 'bid': 0.1, 'CTR1': 0.015, 'CTR2':0.010, 'CTR3':0.005, 'budget': 1.0, 'clicks': 0},
{'name': 'B', 'bid': 0.09, 'CTR1': 0.016, 'CTR2':0.012, 'CTR3':0.006, 'budget': 2.0,  'clicks': 0},
{'name': 'C', 'bid': 0.08, 'CTR1': 0.017, 'CTR2':0.014, 'CTR3':0.007, 'budget': 3.0,  'clicks': 0},
{'name': 'D', 'bid': 0.07, 'CTR1': 0.018, 'CTR2':0.015, 'CTR3':0.008, 'budget': 4.0,  'clicks': 0},
{'name': 'E', 'bid': 0.06, 'CTR1': 0.019, 'CTR2':0.016, 'CTR3':0.010, 'budget': 5.0,  'clicks': 0}
]

clicks = 101

last_total_clicks = None
while True:
    total_clicks = 0
    for d in data:
        total_clicks += d['clicks']
    if total_clicks >= clicks: break
    if last_total_clicks == total_clicks : break
    #----------- star a phase -------------------------
    slot1 = None
    slot2 = None
    slot3 = None
    # find slot 1
    max_e = 0
    for d in data:
        if d['budget'] <= 0 : continue
        if d['bid'] * d['CTR1'] > max_e:
            max_e = d['bid'] * d['CTR1']
            slot1 = d
    #print max_e
    
    # find slot 2
    max_e = 0
    for d in data:
        if d['budget'] <= 0 : continue
        if d != slot1: #skip slot1's winner
            if d['bid'] * d['CTR2'] > max_e:
                max_e = d['bid'] * d['CTR2']
                slot2 = d
    #print max_e
    
    # find slot 3
    max_e = 0
    for d in data:
        if d['budget'] <= 0 : continue
        if d != slot3:
            if d['bid'] * d['CTR3'] > max_e:
                max_e = d['bid'] * d['CTR3']
                slot3 = d
    #print max_e
    
    slot_out = slot1
    CTR_out = slot1['CTR1']
    min = slot1['budget'] / slot1['bid']
    if min > slot2['budget'] / slot2['bid']:
        min = slot2['budget'] / slot2['bid']
        slot_out = slot2
        CTR_out = slot2['CTR2']
    if min > slot3['budget'] / slot3['bid']:
        min = slot3['budget'] / slot3['bid']
        slot_out = slot3
        CTR_out = slot3['CTR3']
    
    clicks_for_slot_out = (int)(slot_out['budget'] / slot_out['bid'])
    slot1['clicks'] += round(clicks_for_slot_out * 1.0 / CTR_out * slot1['CTR1'])
    slot1['budget'] -= clicks_for_slot_out * 1.0 / CTR_out * slot1['CTR1'] * slot1['bid']
    slot2['clicks'] += round(clicks_for_slot_out * 1.0 / CTR_out * slot2['CTR2'])
    slot2['budget'] -= clicks_for_slot_out * 1.0 / CTR_out * slot2['CTR2'] * slot2['bid']
    slot3['clicks'] += round(clicks_for_slot_out * 1.0 / CTR_out * slot3['CTR3'])
    slot3['budget'] -= clicks_for_slot_out * 1.0 / CTR_out * slot3['CTR3'] * slot3['bid'] 
       
    print slot1
    print slot2
    print slot3
    print 'total_clicks=',total_clicks
    last_total_clicks = total_clicks 
    print '-------------------------------------------------------------------------------------------'
    
for d in data:
    print d['name'], d['clicks']