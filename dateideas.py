def ideaslist():
    ideas = {}
    #6 categories:
    #outside/inside (whether the date activity is outside the house or indoors)
    #hungry/full (whether the date activity involves food)
    #quick/long (whether the date activity is quick or long (>= 2 hours))
    #active/still (whether the date activity involves physical activty or not)
    #under50/over50 (whether the date activity is under or over $50)
    #firstdate/dating (whether the date activity is classified as a first/early-stage date or not)
    ideas["Make a charcuterie board together"] = ["inside", "hungry", "quick", "still", "under50", "dating"]
    ideas["Go to a drive-in movie together"] = ["outside", "full", "long", "still", "under50", "firstdate"]
    ideas["Stream a TV-show, concert, or movie at home!"] = ["inside", "full", "long", "still", "under50", "dating"]
    ideas["Paint & pour"] = ["outside", "full", "long", "still", "over50", "dating"]
    ideas["Dog & people watching with a walk at a park"] = ["outside", "full", "quick", "active", "under50", "firstdate"]
    ideas["Karaoke night"] = ["inside", "full", "quick", "active", "under50", "dating"]
    ideas["Ice cream date"] = ["outside", "hungry", "quick", "still", "under50", "firstdate"]
    ideas["Date at a local museum/exhibit"] = ["outside", "full", "long", "still", "under50", "dating"]
    ideas["Craft & plan your dream vacation"] = ["inside", "full", "quick", "still", "under50", "dating"]
    ideas["Go bowling"] = ["outside", "full", "long", "active", "under50", "firstdate"]
    ideas["Play minigolf"] = ["outside","full", "long", "active", "under50", "firstdate"]
    ideas["See a movie"] = ["outside","full", "long", "active", "under50", "firstdate"]
    ideas["Craft cocktails and appetizers (or mocktails)"] = ["inside", "hungry", "quick", "still", "under50", "dating"]
    ideas["Make dinner together"] = ["inside", "hungry", "long", "still", "over50", "dating"]
    ideas["Bake a dessert together"] = ["inside", "hungry", "quick", "still", "under50", "dating"]
    ideas["Do a scavenger hunt in your area"] = ["outside", "full", "long", "active", "under50", "dating"]
    ideas["Arcade date"] = ["outside", "full", "long", "active", "under50", "firstdate"]
    ideas["Picnic date"] = ["outside", "hungry", "quick", "still", "under50", "firstdate"]
    ideas["Volunteer together"] = ["outside", "full", "long", "active", "under50", "dating"]
    ideas["Go out for a nice meal (italian or sushi are some recs!)"] = ["outside", "hungry", "quick", "still", "over50", "dating"]
    return ideas