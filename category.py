
"""
Function that gets the category based on the subcategory
"""
def category(string):
    if string in ('SugarCreamFlavor Shot Machines','Hot Beverage Machine','Iced Beverage Machine'):
        return "Beverage Equipment"
    
    if string in ('Preventative Maintenance','Air Conditioning','Exhaust Systems','Heating'):
        return "Heating/Ventilation & AC"
    
    if string in ('WindowDoor Repairs'):
        return "Facility Maintenance"
    
    if string in ('Reach In Cooler','Reach In Freezer','Deli Bar-Specialty Refigerator',
                        'Walk In Freezers','Walk In Coolers','Under Counter Cooler - Freezer','Ice Machine'):
        return "Refrigeration"
    
    if string in ('GrillsBagel Toasters','SmallwareA','SmallwareB','SmallwareC','SmallwareD','SmallwareE','Ovens','Hot Holding Cabinets','Dishwasher'):
        return "Food Preparation Equipment"
    
    else:
        return "Invalid"

    
    
