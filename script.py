# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_damages(damages):
    new_damages = []
    conversion = {"M": 1000000,
                  "B": 1000000000}
    for damage in damages:
        if damage == 'Damages not recorded':
            new_damages.append(damage)
        elif damage[-1] in conversion.keys():
            new_value = float(damage[:-1]) * conversion[damage[-1]]
            new_damages.append(new_value)

    return new_damages
new_dmgs = update_damages(damages)
print(new_dmgs)
# write your construct hurricane dictionary function here:

hurricanes = {}
def hurr_dict(names, months, years, max_sustained_winds, areas_affected, deaths):
  for i in range(len(names)):
     hurricanes[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind:": max_sustained_winds[i], "Areas Affected ": areas_affected[i], "Damage": new_dmgs[i], "Deaths": deaths[i]}
  return hurricanes
hurricanes = hurr_dict(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricanes)
# write your construct hurricane by year dictionary function here:
hurridict = {}
def hurricane_by_year_dictionary(hurricanes): 
    current_year = []
    current_cane = []
    for year in hurricanes:
      yeary = hurricanes.get(year)
      yeary2 = yeary.get("Year")
      current_year.append(yeary2)      
    for value in hurricanes.values():
      current_cane.append(value)
    for i in range(len(hurricanes)):
      if current_year[i] not in hurridict.keys():
        hurridict[current_year[i]] = [current_cane[i]] 
      else:
        hurridict[current_year[i]].append(current_cane[i])
    return hurridict  
       
          
hurridict = hurricane_by_year_dictionary(hurricanes)
print(hurridict) 

# write your count affected areas function here:
areaff = {}
def area_count(hurricanes):
  areatotal = []
  for area in hurricanes:
    area1 = hurricanes.get(area)
    area2 = area1.get("Areas Affected ")
    areatotal.append(area2)
  for area in areatotal:
    for i in range(len(area)):
      if area[i] not in areaff:
        areaff.update({area[i]: 1})
      else:
        areaff[area[i]] += 1 
  return areaff  
areaff = area_count(hurricanes)
print(areaff)


# write your find most affected area function here:
def mostaff(areaff):
  max_area = " "
  max_area_count = 0
  for key,value in areaff.items():
    if value > max_area_count:
      max_area = key
      max_area_count = value
  return max_area, max_area_count
print(mostaff(areaff))  
     
# write your greatest number of deaths function here:
def most_d(hurricanes):
  most_deaths = 0
  most_deaths_area = " "
  for key, value in hurricanes.items():
    if value["Deaths"] > most_deaths:
      most_deaths = value["Deaths"]
      most_deaths_area = key
  return most_deaths_area, most_deaths
print(most_d(hurricanes))  

# write your catgeorize by mortality function here:
def mortalityhur(hurricanes):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in hurricanes.items():
    if value["Deaths"] <= 0:
      hurricanes_by_mortality[0].append(key)
    elif value["Deaths"] <= 100:
      hurricanes_by_mortality[1].append(key)
    elif value["Deaths"] <= 500:
      hurricanes_by_mortality[2].append(key)
    elif value["Deaths"] <= 1000:
      hurricanes_by_mortality[3].append(key)
    elif value["Deaths"] <= 10000:
      hurricanes_by_mortality[4].append(key)
    else:
      hurricanes_by_mortality[5].append(key)
  return hurricanes_by_mortality
print(mortalityhur(hurricanes))  
# write your greatest damage function here:
def most_c(hurricanes):
  hcost = 0
  hname = " "
  for key, value in hurricanes.items():
    if value["Damage"] == "Damages not recorded":
      print(key, value["Damage"])
    elif value["Damage"] > hcost:
      hcost = value["Damage"]
      hname = key
  print("Most costly was " + hname + " with a cost of " + str(hcost) + "$")
print(most_c(hurricanes))           
# write your categorize by damage function here:
def damageshur(hurricanes):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in hurricanes.items():
    if value["Damage"] != "Damages not recorded":
      if value["Damage"] <= 0 :
        hurricanes_by_damage[0].append(key)
      elif value["Damage"] <= 100000000:
        hurricanes_by_damage[1].append(key)
      elif value["Damage"] <= 1000000000:
        hurricanes_by_damage[2].append(key)
      elif value["Damage"] <= 10000000000:
        hurricanes_by_damage[3].append(key)
      elif value["Damage"] <= 50000000000:
        hurricanes_by_damage[4].append(key)
      else:
        hurricanes_by_damage[5].append(key)
  return hurricanes_by_damage
print(damageshur(hurricanes))  





