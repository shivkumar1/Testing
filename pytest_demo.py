def string_counts():
    dct = {}
    with open("pytest.log", "r") as f:
        for line in f:
            lst = line.split(" ")
            if lst[2] in dct:
                dct[lst[2]] = dct[lst[2]] + 1
            else:
                dct[lst[2]] = 1
	#print dct
				
    return dct
  