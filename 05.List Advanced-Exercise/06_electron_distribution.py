electrons_nr = int(input())
filled_shells = 0
shells = []
while electrons_nr >= 2*((filled_shells+1)**2):
    shells.append(2 * ((filled_shells + 1) ** 2))
    electrons_nr -= 2*((filled_shells+1)**2)
    filled_shells = len(shells)
else:
    if electrons_nr > 0:
        shells.append(electrons_nr)

print(shells)