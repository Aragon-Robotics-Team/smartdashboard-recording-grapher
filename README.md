# SmartDashboard Grapher

Graphs data smart dashboard logs, used for tuning one series against another (for example, when tuning a PID controller)

## Install

```
pip install -r requirements.txt
```

## Use

```
python grapher.py filename.csv arg0 arg1
```

The script will look for any column that contains the substrings arg0, and arg1. For example if the full title of arg0 is `SmartDashboard/Swerve/Angle/Module_0`, using `Angle/Module_0` in the argument would be sufficient.

The script will graph both arguments on one plot, using the time data provided by smart dashboard as the x-axis.
