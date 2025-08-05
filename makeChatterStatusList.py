import json

# Load your JSON data from file
with open('chatters.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Lists for each status
not_followed = []
followers = []
tier1_subs = []
tier2_subs = []
tier3_subs = []

for entry in data:
    user = entry.get('data', {}).get('user', {})
    login = user.get('login')
    relationship = user.get('relationship', {})
    followed_at = relationship.get('followedAt')
    sub_benefit = relationship.get('subscriptionBenefit', {})
    tier = sub_benefit.get('tier')

    if not login:
        continue

    if tier == "1000":
        tier1_subs.append(login)
    elif tier == "2000":
        tier2_subs.append(login)
    elif tier == "3000":
        tier3_subs.append(login)
    elif followed_at:
        followers.append(login)
    else:
        not_followed.append(login)

print("Not Followed:", not_followed)
print("Followers:", followers)
print("Tier 1 Subs:", tier1_subs)
print("Tier 2 Subs:", tier2_subs)
print("Tier 3 Subs:", tier3_subs)

print("\nCounts:")
print("Not Followed:", len(not_followed))
print("Followers:", len(followers))
print("Tier 1 Subs:", len(tier1_subs))
print("Tier 2 Subs:", len(tier2_subs))
print("Tier 3 Subs:", len(tier3_subs))

with open('chatters.md', 'w', encoding='utf-8') as f:
    f.write("# Twitch Chatters Status\n\n")
    f.write(f"**Not Followed ({len(not_followed)}):**\n")
    for name in not_followed:
        f.write(f"- {name}\n")
    f.write(f"\n**Followers ({len(followers)}):**\n")
    for name in followers:
        f.write(f"- {name}\n")
    f.write(f"\n**Tier 1 Subs ({len(tier1_subs)}):**\n")
    for name in tier1_subs:
        f.write(f"- {name}\n")
    f.write(f"\n**Tier 2 Subs ({len(tier2_subs)}):**\n")
    for name in tier2_subs:
        f.write(f"- {name}\n")
    f.write(f"\n**Tier 3 Subs ({len(tier3_subs)}):**\n")
    for name in tier3_subs:
        f.write(f"- {name}\n")