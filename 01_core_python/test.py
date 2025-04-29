emoji = "😚"

heart = [
    "      " + emoji * 12 + "      " + emoji * 12,   # 24
    "    " + emoji * 18 + "    " + emoji * 18,       # 36
    "   " + emoji * 22 + "  " + emoji * 22,          # 44
    "  " + emoji * 50,                               # 50
    " " + emoji * 54,                                # 54
    emoji * 56,                                      # 56
    " " + emoji * 54,                                # 54
    "  " + emoji * 50,                               # 50
    "   " + emoji * 44,                              # 44
    "    " + emoji * 36,                             # 36
    "     " + emoji * 30,                            # 30
    "      " + emoji * 20,                           # 20
    "       " + emoji * 10                           # 10
]

# Total: 24+36+44+50+54+56+54+50+44+36+30+20+10 = 508 → we’ll trim 8 emojis from last row
heart[-1] = "       " + emoji * 2  # use only 2 instead of 10 → 500 total

# Print and count
count = 0
for line in heart:
    print(line)
    count += line.count(emoji)

print(f"\nTotal emojis used: {count}")
