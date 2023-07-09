import um

def main():
    test_count()
    test_case()
    test_middle_word()

def test_count():
    assert um.count("um") == 1
    assert um.count("um?") == 1
    assert um.count("Um, thanks for the album") == 1
    assert um.count("Um, thanks, um...") == 2

def test_case():
    assert um.count("Um, thanks, UM, I dunno, UmUm...") == 2

def test_middle_word():
    assert um.count("Yummy") == 0
    assert um.count("Um, thanks, UM, I dunno, UmUm...") == 2
    assert um.count("Justin Bieber sings: Yeah, you got that yummy-yum") == 0

if __name__ == "__main__":
    main()