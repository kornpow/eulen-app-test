import math

def distance_to_lat_long(distance_km, bearing_degrees, start_lat, start_long):
    """
    Convert distance and bearing to new coordinates
    distance_km: distance in kilometers
    bearing_degrees: direction in degrees (0° is North, 90° is East)
    """
    R = 6371  # Earth's radius in km
    # Convert to radians
    bearing_rad = math.radians(bearing_degrees)
    start_lat_rad = math.radians(start_lat)
    start_long_rad = math.radians(start_long)
    # Calculate new latitude
    end_lat_rad = math.asin(
        math.sin(start_lat_rad) * math.cos(distance_km/R) +
        math.cos(start_lat_rad) * math.sin(distance_km/R) * math.cos(bearing_rad)
    )
    # Calculate new longitude
    end_long_rad = start_long_rad + math.atan2(
        math.sin(bearing_rad) * math.sin(distance_km/R) * math.cos(start_lat_rad),
        math.cos(distance_km/R) - math.sin(start_lat_rad) * math.sin(end_lat_rad)
    )
    return round(math.degrees(end_lat_rad), 3), round(math.degrees(end_long_rad), 3)


def google_maps_url(lat,long):
    return f"https://www.google.com/maps?q={lat},{long}"