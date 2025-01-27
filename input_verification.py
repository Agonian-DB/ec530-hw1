import re

def input_verification(raw_data):

    result = []
    lines = raw_data.splitlines()

    for line in lines:
        # Match common formats: "40 42.8 74 00.6", "40.7128° N 74.0060° W", etc.
        line = line.strip()
        if not line:
            continue

        # Case 1: Degrees with directional indicators (e.g., "40.7128° N 74.0060° W")
        match = re.match(r"([\d.]+)[°\s]*([NS])[\s,]*([\d.]+)[°\s]*([EW])", line, re.I)
        if match:
            lat, lat_dir, lon, lon_dir = match.groups()
            lat = float(lat) * (1 if lat_dir.upper() == "N" else -1)
            lon = float(lon) * (1 if lon_dir.upper() == "E" else -1)
            result.append((lat, lon))
            continue

        # Case 2: Simple decimals (e.g., "40.7128 -74.0060")
        match = re.match(r"^([\d.-]+)\s+([\d.-]+)$", line)  # 加了 ^ 和 $
        if match:
            lat, lon = map(float, match.groups())
            if -90 <= lat <= 90 and -180 <= lon <= 180:
                result.append((lat, lon))
                continue
        
        # Case 3: Degrees without directional indicators (e.g., "40 42.8 74 00.6")
        match = re.match(r"(\d+)\s+([\d.]+)\s+(\d+)\s+([\d.]+)", line)
        if match:
            lat_deg, lat_min, lon_deg, lon_min = map(float, match.groups())
            lat = lat_deg + lat_min / 60
            lon = lon_deg + lon_min / 60
            result.append((lat, lon))
            continue



        # If no valid format matches
        raise ValueError(f"Invalid coordinate format: {line}")

    return result
