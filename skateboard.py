# import dsgp4.util
from sgp4.api import days2mdhms, WGS72, Satrec, jday

# Example TLE for the International Space Station (ISS)
line1 = '1 25544U 98067A   24189.99876543  .00000123  00000-0  12345-3 0  9999'
line2 = '2 25544  51.6418 176.4876 0005678 123.4567 234.5678 15.49876543987654'

satellite = Satrec.twoline2rv(line1, line2)

from datetime import datetime, timedelta

# Propagate 10 minutes after the TLE epoch
months, days, hours, minutes, seconds = days2mdhms(satellite.epochyr, satellite.epochdays)
seconds += 10

jd, fr = jday(satellite.epochyr, months, days, hours, minutes, seconds)

e, r, v = satellite.sgp4(jd, fr)

if e == 0:  # Check for errors during propagation
    print(f"Position (TEME): {r} km")
    print(f"Velocity (TEME): {v} km/s")
else:
    print(f"SGP4 error: {e}")


