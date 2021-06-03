from skyfield import api
from skyfield import almanac
import csv, pytz

ts = api.load.timescale()
eph = api.load('de421.bsp')

t0 = ts.utc(2021, 6, 1)
t1 = ts.utc(2022, 12, 31)
t, y = almanac.find_discrete(t0, t1, almanac.moon_phases(eph))

ty = zip(t, y)
with open("phases.csv", "w") as phasefile:
    phasecsv = csv.DictWriter(phasefile, ["utc", "phase", "Pacific time"])
    phasecsv.writeheader()
    [phasecsv.writerow({"utc":t1.utc_iso(),
                        "phase":almanac.MOON_PHASES[y1],
                        "Pacific time": t1.astimezone(pytz.timezone('US/Pacific'))}) for t1, y1 in ty]
