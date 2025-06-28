def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft['distance'] = 0.01
    spacecraft.update({"orbit": "sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    Name: {spacecraft['name']}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    ==========================
    """

main()