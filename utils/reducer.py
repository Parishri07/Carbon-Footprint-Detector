def suggest_reduction(activities):
    tips = []

    if activities.get("car_km_per_week", 0) > 50:
        tips.append("Consider using public transport or carpooling.")
    if activities.get("meat_meals_per_week", 0) > 5:
        tips.append("Try a vegetarian meal once or twice a week.")
    if activities.get("electricity_units_per_month", 0) > 200:
        tips.append("Use energy-efficient appliances and turn off unused devices.")
    if activities.get("flights_per_year", 0) > 2:
        tips.append("Offset your flight emissions or explore virtual meetings.")

    if not tips:
        tips.append("You're doing great! Keep up the sustainable habits.")

    return tips
