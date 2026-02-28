# ====================================================
# ROAD ROUTE RISK SCREENING
# EXACT REQUIRED OUTPUT VERSION
# ====================================================

# Roads and risks
roads = ["Road A", "Road B", "Road C"]
risk = [5, 2, 1]   # A, B, C

# All 3-qubit states
states = [
    "000","001","010","011",
    "100","101","110","111"
]

# ----------------------------------------------------
# Calculate risk for each state
# ----------------------------------------------------
results = {}

for s in states:

    # reverse because q0=A, q1=B, q2=C
    bits = s[::-1]

    total_risk = (
        int(bits[0]) * risk[0] +
        int(bits[1]) * risk[1] +
        int(bits[2]) * risk[2]
    )

    results[s] = total_risk

# ----------------------------------------------------
# PRINT EXACT FORMAT
# ----------------------------------------------------
print("\nRoute Probabilities")
print("-------------------")

for s in states:
    print(f"{s} : {results[s]}")

# safest route (minimum risk except 000)
valid_routes = {k:v for k,v in results.items() if k != "000"}
best_route = min(valid_routes, key=valid_routes.get)

print("\nSafest Route Bitstring:", best_route)

print("\nSelected Roads:")

bits = best_route[::-1]

for i, b in enumerate(bits):
    if b == "1":
        print("✓", roads[i])
