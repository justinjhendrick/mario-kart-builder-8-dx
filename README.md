# mario-kart-builder-8-dx
Choose the driver, kart, tire, glider build that's best for your playstyle

Tell this tool how much you care about each stat, and it will output the
build(s) with the best score.
For example, to find the build with the highest sum of its stats, you would
specify the same weight to all stats, like this:

```
GroundSpeed: 1.0
WaterSpeed: 1.0
AirSpeed: 1.0
AntiGravitySpeed: 1.0
Acceleration: 1.0
Weight: 1.0
GroundHandling: 1.0
WaterHandling: 1.0
AirHandling: 1.0
AntiGravityHandling: 1.0
Traction: 1.0
MiniTurbo: 1.0
```

Given this input, this tool will multiply 1.0 times the value of each statistic
for a build and sum up the products which is the "score" of the build. Then it
will choose the build(s) with the highest score.

# Acknowledgements

We copied the source data from https://github.com/jfmario/mario-kart-8-deluxe-builds
