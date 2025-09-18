from typing import Dict, List, Tuple

def parse_and_normalize_sensor_data(text: str) -> Dict[str, List[Tuple[str, float]]]:
    """
    Parse sensor CSV-like text and compute per-sensor z-score normalization.

    Args:
        text (str): multiline CSV-like text: sensor_id,timestamp,value

    Returns:
        Dict[str, List[Tuple[str, float]]]: sensor_id → list of (timestamp, z_value)
    """
    import math

    # Parse lines, skip blanks
    data = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) != 3:
            continue  # skip malformed lines
        sensor_id, timestamp, value = parts[0], parts[1], float(parts[2])
        data.append((sensor_id, timestamp, value))

    # Group by sensor_id
    sensors = {}
    for sensor_id, timestamp, value in data:
        sensors.setdefault(sensor_id, []).append((timestamp, value))

    # Compute z-score per sensor
    result = {}
    for sensor_id, readings in sensors.items():
        values = [v for _, v in readings]
        n = len(values)
        if n == 1:
            # All z=0 for single value
            zscores = [0.0]
        else:
            mean = sum(values) / n
            # Use population stddev (ddof=0)
            variance = sum((v - mean) ** 2 for v in values) / n
            std = math.sqrt(variance) if variance > 0 else 0.0
            if std == 0:
                zscores = [0.0] * n
            else:
                zscores = [(v - mean) / std for v in values]
        rounded = [round(z, 3) for z in zscores]
        result[sensor_id] = [(timestamp, z) for (timestamp, _), z in zip(readings, rounded)]

    return result

if __name__ == "__main__":
    print("Enter sensor data (sensor_id,timestamp,value), one per line.")
    print("End input with an empty line (press Enter on a blank line):")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    input_text = "\n".join(lines)
    output = parse_and_normalize_sensor_data(input_text)
    print("\nNormalized Sensor Data:")
    for sensor_id, readings in output.items():
        print(f"{sensor_id}:")
        for timestamp, z in readings:
            print(f"  {timestamp} -> z={z}")
