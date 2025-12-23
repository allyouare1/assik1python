S1 = input().strip()
S2 = input().strip()
if len(S1) != len(S2):
    print("NO")
else:
    s_S1 = sorted(S1)
    s_S2 = sorted(S2)

    if s_S1 == s_S2:
        print("YES")
    else:
        print("NO")