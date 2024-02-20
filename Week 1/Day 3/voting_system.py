# voter dictionary = {"name": "", "age": number, "addr": "address"}
# vote dictionary = {"id": number,"canidate: "name"}
# canidate = {"name": "", "positions": ""}
import random
voters_line = [] # queue, append(), pop()
votes = []
canidates = []
num_of_votes = 0
# cast vote
def vote(id, canidate, votes, voter_name, set_of_voters_voted):
    if voter_name not in set_of_voters_voted:
        votes.append({"id": id, "canidate": canidate})
        set_of_voters_voted.add(voter_name)
    else:
        print(f"{voter_name} has already voted before.")
    return votes, set_of_voters_voted

for i in range(20):
    name = f"citizen-{i}"
    address = f"street-{i}"
    age = random.randint(18,100)
    voters_line.append({"name": name,"age": age,"addr": address})

canidates_votes = {}
for i in range(4):
    name = f"canidate-{i}"
    for j in range(random.randint(1,3)):
        position = f"position-{j}"
        canidates.append({"name":name,"position":position})
    canidates_votes[name] = 0

set_of_voters_voted = set() # to keep track of each voter after they voted
num_of_voters = len(voters_line)

while num_of_voters > len(votes):
    voter = voters_line.pop()
    canidate_name = random.choice(canidates)['name']
    votes, set_of_voters_voted = vote(num_of_votes, canidate_name, votes, voter["name"],set_of_voters_voted)
    canidates_votes[canidate_name] +=  1
    num_of_votes += 1

for key in canidates_votes:
    print(f"{key} has acquired {canidates_votes[key]} votes")
# test if a voter can vote twice or no
# canidate = random.choices(canidates)
# votes, set_of_voters_voted = vote(num_of_votes, canidate, votes, "citizen-19",set_of_voters_voted)
# votes, set_of_voters_voted = vote(num_of_votes, canidate, votes, "citizen-9",set_of_voters_voted)



