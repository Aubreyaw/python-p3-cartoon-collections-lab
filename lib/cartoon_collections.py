def roll_call_dwarves(dwarf_names = []):
    for index, item in enumerate(dwarf_names, start=1):
        print(f"{index}. {item}")
    pass

def summon_captain_planet(calls):
     new_calls = [call.capitalize() + "!" for call in calls]
     return new_calls

def long_planeteer_calls(calls):
    sorted_calls = any(len(call) > 4 for call in calls)
    return sorted_calls
    

def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheeses:
            return item
    return None
    

