import math

def eratos(angle,derror=1):
	distance = 5000* 185 *derror
	circum = (360.0/angle)* distance * 1/1000
	return circum

# a = eratos(7.2)
# b = eratos(8.6)
# c = eratos(5.8)

# d = eratos(7.2, 1.15)
# e = eratos(7.2, 0.85)
# f = eratos(8.6, 1.15)
# g = eratos(8.6, 0.85)
# h = eratos(5.8, 1.15)
# i = eratos(5.8, 0.85)

# errors = [a,b,c,d,e,f,g,h,i]
# correct = 40000

def percentage_error(val,correct):
	abs_error = abs(float(val-correct))
	perc_error = (abs_error/val) * 100
	return perc_error,val

# print map(percentage_error,errors,[correct]*len(errors))
# # print help(map)

# print math.degrees(math.asin(0.62))
# print math.degrees(math.atan(4.0/7.0))
# print math.degrees(math.atan(1/40.0))
# print 25/math.tan(math.radians(1.30))
# print 28.0*24/720
moon_circ = (0.93/(205/60.0))*40000
moon_diiam = moon_circ / math.pi
# print moon_diiam, math.tan(math.radians(0.5))
moon_dist = moon_diiam /math.tan(math.radians(0.5))
# print moon_dist
moon_dist = 400000 # more accurate
moon_sun_angle = math.radians(89.853)
sun_dist = moon_dist / math.cos(moon_sun_angle)
print sun_dist

tangent = (5000*0.185)/156000000
sun_angle = math.degrees(math.atan(tangent))