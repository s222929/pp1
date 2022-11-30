array = [
    {'country': "Poland:", "Population" : 38000000},
    {'country': "Ukraine:", "Population" : 43000000},
    {'country': "Uganda:", "Population" : 47000000},
    {'country': "Germany:", "Population" : 83000000},
    {'country': "France:", "Population" :67000000}
]


items = 0
while items < len(array):
    for x,y in array[items].items():
        print(x, "", y, end = " ")
    items = items + 1
    print()