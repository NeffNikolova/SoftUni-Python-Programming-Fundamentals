from math import floor

biscuits_per_day_per_worker = int(input())
worker_count = int(input())
competitor_biscuits_for_thirty_days= int(input())
total_biscuits = 0

for day in range(1, 31):

    if day % 3 == 0:
        total_biscuits += floor(0.75 * (biscuits_per_day_per_worker * worker_count))
    else:
        total_biscuits += biscuits_per_day_per_worker * worker_count

print(f'You have produced {total_biscuits} biscuits for the past month.')

percentage = abs(total_biscuits - competitor_biscuits_for_thirty_days)/competitor_biscuits_for_thirty_days * 100
if total_biscuits > competitor_biscuits_for_thirty_days:
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage:.2f} percent less biscuits.")
