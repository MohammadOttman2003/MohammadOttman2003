# Were creating a basic Python Script that store some information about sports Injuries

injuries = {
    "acl tear": {
        "Description" : "A tear of the anterior cruciate ligament in the knee.",
        "Common Sports": ["Basketball, Soccer, Volleyball, Football"],
        "Treatment": "Surgery followed by Physical Therapy.",
        "Recovery Exercises": ["Nordic Curls","HamString Curls", "Back-Sled","Walking backwards on incline Treadmill"]
    },
    "concussion": {
        "Description" : "A brain injury caused by a blow to the head.",
        "Common Sports": ["Football", "Boxing", "Rugby"],
        "Treatment": "Rest and gradual return to activities. Nuero-Muscular Therapy along with rest can accelerate healing process.",
        "Recovery Exercises": ["Stationary Bike", "Walking"]
    },
    "sprained ankle": {
        "Description" : "An injury to the ligaments in the ankle.",
        "Common Sports" : ["Basketball", "Running", "Soccer"],
        "Treatment" : "Rest, ice, compression, and elevation (RICE).",
        "Recovery Exercises" : ["Calf Raises,", "Negative Calf Raises", "Balance on one foot", "Spell Alphabet with foot"]
    },
    "tibia fracture": {
        "Description" : "When a fall blow places more pressure on tibia causing a complete/partial break.",
        "Common Sports" : ["Football","Basketball","Rugby"],
        "Treatment" : "Surgery, usually one including nails or plates, followed by Physical Therapy",
        "Recovery Exercises" : ["One legged wall squats","leg curls","Step-ups","Calf raises"]
    }
}


def get_injury_info(injury_name):
    injury_name_lower = injury_name.lower()
    injury = injuries.get(injury_name_lower)
    if injury:
        return injury
    else:
        return "Injury not found."