def create_election():
    candidates = {}
    while True:
        name = input("Enter candidate name or press Enter to finish : ").strip()
        if not name:
            break
        candidates[name] = 0
    return candidates

def vote(candidates, name):
    if name in candidates:
        candidates[name] += 1
        return True
    return False

def print_winner(candidates):
    if not candidates:
        print("No candidates in the election")
        return

    max_votes = max(candidates.values())
    winners = [name for name, votes in candidates.items() if votes == max_votes]

    print("Winner is:")
    for winner in winners:
        print(winner)


print("Set up the election:")
candidates = create_election()

print("\nVoting begins:")
while True:
    vote_for = input("Vote for or press Enter to finish voting : ").strip()
    if not vote_for:
        break
    if vote(candidates, vote_for):
        print("Vote recorded successfully.")
    else:
        print("Invalid candidate name. Vote not counted.")

print("\nVoting Results:")
sorted_results = dict(sorted(candidates.items(), key=lambda x: x[1], reverse=True))
for candidate, votes in sorted_results.items():
    print(f"{candidate}: {votes}")

print("\nDetermining winner:")
print_winner(candidates)

