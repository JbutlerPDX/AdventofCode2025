lockState = 50
finalLandings = 0      # part 1: times dial ends exactly at 0
finalPasses = 0        # part 2: times 0 is passed or landed on

with open('lockFile', 'r') as f:
    for line in f:
        step = line.strip()
        if not step:
            continue
        direction = step[0]
        turnValue = int(step[1:])

        s = lockState

        if direction == 'R':
            # passes when crossing from 99 -> 0
            passes = (s + turnValue) // 100
            lockState = (s + turnValue) % 100
        else:  # 'L'
            if s == 0:
                passes = turnValue // 100
            elif turnValue < s:
                passes = 0
            else:
                passes = 1 + (turnValue - s) // 100
            lockState = (s - turnValue) % 100

        # count landings (part 1)
        if lockState == 0:
            finalLandings += 1

        # add passes (part 2)
        finalPasses += passes

print("Part 1 — landings on 0:", finalLandings)
print("Part 2 — passes (including landings):", finalPasses)


