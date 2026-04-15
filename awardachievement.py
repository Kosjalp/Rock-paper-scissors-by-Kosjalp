def award_achievement(stat1, isGreater, stat2,name, achievements):
    if name not in achievements:
        if isGreater:
            if stat1 > stat2:
                achievements.append(name)
        else:
            if stat1 < stat2:
                achievements.append(name)
        print("")
        print(f"Achievement unlocked: {name}")
        print("")