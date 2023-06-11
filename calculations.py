'''
This file contains all the calculations that are needed for the app.py file.

It contains:
    - the speed difference calculation
    - the penalty calculation for the 30er zone
    - the penalty calculation for innerorts
    - the penalty calculation for ausserorts
    - the penalty calculation for autobahn
'''

# calculating the speed difference
def speed_difference(gefahrene, erlaubte, radar):
    if radar == 'laser':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 3
        elif gefahrene >= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 4
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 5
    elif radar == 'mobil':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 7
        elif gefahrene >= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 8
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 9
    elif radar == 'stationaer':
        if gefahrene < 100:
            result = gefahrene - erlaubte - 5
        elif gefahrene >= 100 and gefahrene < 150:
            result = gefahrene - erlaubte - 6
        elif gefahrene >= 150:
            result = gefahrene - erlaubte - 7
    return result


# penalty calculation for 30er zone
def penalty_30er_zone(result):
    if result <= 5:
        strafe = 'keine weitere Strafe'
        busse = 40
    elif result <= 10:
        strafe = 'keine weitere Strafe'
        busse = 120
    elif result <= 15:
        strafe = 'keine weitere Strafe'
        busse = 250
    elif result <= 17:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 19:
        strafe = 'keine weitere Strafe'
        busse = 600
    elif result <= 20:
        strafe = 'keine weitere Strafe'
        busse = '30 Tagessätze'
    elif result <= 24:
        strafe = 'keine weitere Strafe'
        busse = '30 Tagessätze'
    elif result <= 25:
        strafe = 'keine weitere Strafe'
        busse = '30 Tagessätze'
    elif result <= 29:
        strafe = 'keine weitere Strafe'
        busse = '50 Tagessätze'
    elif result <= 34:
        strafe = 'keine weitere Strafe'
        busse = '90 Tagessätze'
    elif result <= 39:
        strafe = 'keine weitere Strafe'
        busse = '120 Tagessätze'
    else:
        strafe = 'mindestens 1 Jahr Freiheitsentzug'
        busse = 'Strafverfahren'
    # return the result
    return strafe, busse


# penalty calculation for innerorts
def penalty_innerorts(result):
    if result <= 5:
        strafe = 'keine weitere Strafe'
        busse = 40
    elif result <= 10:
        strafe = 'keine weitere Strafe'
        busse = 120
    elif result <= 15:
        strafe = 'keine weitere Strafe'
        busse = 250
    elif result <= 17:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 19:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 20:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 24:
        strafe = '1 Monat Ausweisentzug'
        busse = 600
    elif result <= 25:
        strafe = '3 Monate Ausweisentzug'
        busse = '20 Tagessätze'
    elif result <= 29:
        strafe = '3 Monate Ausweisentzug'
        busse = '20 Tagessätze'
    elif result <= 34:
        strafe = '3 Monate Ausweisentzug'
        busse = '50 Tagessätze'
    elif result <= 39:
        strafe = '3 Monate Ausweisentzug'
        busse = '70 Tagessätze'
    elif result <= 44:
        strafe = 'mindestens 24 Monate Ausweisentzug'
        busse = 'mindestens 120 Tagessätze'
    elif result <= 49:
        strafe = 'mindestens 24 Monate Ausweisentzug'
        busse = 'mindestens 120 Tagessätze'
    else:
        strafe = 'mindestens 1 Jahr Freiheitsentzug'
        busse = 'Strafverfahren'
    # return the result
    return strafe, busse

# penalty calculation for ausserorts
def penalty_ausserorts(result):
    if result <= 5:
        strafe = 'keine weitere Strafe'
        busse = 40
    elif result <= 10:
        strafe = 'keine weitere Strafe'
        busse = 100
    elif result <= 15:
        strafe = 'keine weitere Strafe'
        busse = 160
    elif result <= 17:
        strafe = 'keine weitere Strafe'
        busse = 240
    elif result <= 19:
        strafe = 'keine weitere Strafe'
        busse = 240
    elif result <= 20:
        strafe = 'keine weitere Strafe'
        busse = 240
    elif result <= 24:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 25:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 29:
        strafe = '1 Monat Ausweisentzug'
        busse = 600
    elif result <= 34:
        strafe = '3 Monate Ausweisentzug'
        busse = '10 Tagessätze'
    elif result <= 39:
        strafe = '3 Monate Ausweisentzug'
        busse = '12 Tagessätze'
    elif result <= 44:
        strafe = '3 Monate Ausweisentzug'
        busse = '60 Tagessätze'
    elif result <= 49:
        strafe = '3 Monate Ausweisentzug'
        busse = '90 Tagessätze'
    elif result <= 54:
        strafe = '3 Monate Ausweisentzug'
        busse = 'mindestens 120 Tagessätze'
    elif result <= 59:
        strafe = '3 Monate Ausweisentzug'
        busse = 'mindestens 120 Tagessätze'
    else:
        strafe = 'mindestens 1 Jahr Freiheitsentzug'
        busse = 'Strafverfahren'
    # return the result
    return strafe, busse

# penalty calculation for autobahn
def penalty_autobahn(result):
    if result <= 5:
        strafe = 'keine weitere Strafe'
        busse = 20
    elif result <= 10:
        strafe = 'keine weitere Strafe'
        busse = 60
    elif result <= 15:
        strafe = 'keine weitere Strafe'
        busse = 120
    elif result <= 17:
        strafe = 'keine weitere Strafe'
        busse = 180
    elif result <= 19:
        strafe = 'keine weitere Strafe'
        busse = 180
    elif result <= 20:
        strafe = 'keine weitere Strafe'
        busse = 180
    elif result <= 24:
        strafe = 'keine weitere Strafe'
        busse = 260
    elif result <= 25:
        strafe = 'keine weitere Strafe'
        busse = 260
    elif result <= 29:
        strafe = 'keine weitere Strafe'
        busse = 400
    elif result <= 34:
        strafe = '1 Monat Ausweisentzug'
        busse = 600
    elif result <= 39:
        strafe = '3 Monate Ausweisentzug'
        busse = '20 Tagessätze'
    elif result <= 44:
        strafe = '3 Monate Ausweisentzug'
        busse = '30 Tagessätze'
    elif result <= 49:
        strafe = '3 Monate Ausweisentzug'
        busse = '50 Tagessätze'
    elif result <= 54:
        strafe = '3 Monate Ausweisentzug'
        busse = '60 Tagessätze'
    elif result <= 59:
        strafe = '3 Monate Ausweisentzug'
        busse = '70 Tagessätze'
    elif result <= 64:
        strafe = '3 Monate Ausweisentzug'
        busse = '90 Tagessätze'
    elif result <= 79:
        strafe = '3 Monate Ausweisentzug'
        busse = 'mindestens 120 Tagessätze'
    else:
        strafe = 'mindestens 1 Jahr Freiheitsentzug'
        busse = 'Strafverfahren'
    # return the result
    return strafe, busse