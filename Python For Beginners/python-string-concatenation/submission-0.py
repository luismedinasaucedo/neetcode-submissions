def concatenate(s1: str, s2: str) -> str:
    resultado =s1 + s2

    if len(resultado)>10:
        return "Too long!"
    else:
        return resultado




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
