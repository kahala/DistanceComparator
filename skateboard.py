# import dsgp4.util
from sgp4.api import days2mdhms, WGS72, Satrec, jday
from datetime import datetime, timedelta

# Example TLE for the International Space Station (ISS)
line1 = '1 25544U 98067A   24189.99876543  .00000123  00000-0  12345-3 0  9999'
line2 = '2 25544  51.6418 176.4876 0005678 123.4567 234.5678 15.49876543987654'

sample_time = "2023-08-25T14:35:45"
dt_time = datetime.fromisoformat(sample_time)


satellite = Satrec.twoline2rv(line1, line2)



months, days, hours, minutes, seconds = days2mdhms(satellite.epochyr, satellite.epochdays)
minutes += 10
print(months, days, hours, minutes, seconds)
print(satellite.epochyr)


jd, fr = jday(satellite.epochyr, months, days, hours, minutes, seconds)
jd, fr = jday(dt_time.year, dt_time.month, dt_time.day, dt_time.hour, dt_time.minute, dt_time.second)
e, r, v = satellite.sgp4(jd, fr)

if e == 0:  # Check for errors during propagation
    print(f"Position (TEME): {r} km") # True Equator Mean Equinox position (km)
    print(f"Velocity (TEME): {v} km/s") # True Equator Mean Equinox velocity (km/s)
else:
    print(f"SGP4 error: {e}")


