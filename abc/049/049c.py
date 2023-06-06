S = input()
S = S.replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
print("YES" if len(S) == 0 else "NO")