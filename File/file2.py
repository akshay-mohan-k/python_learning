def game(score):
    with open("e:/python/file/Hi-score.txt", "r+") as f:
        currentScore = f.read()
        if(currentScore == ""):
            currentScore = score
            f.write(str(currentScore))
        elif(int(currentScore) < score):
            currentScore = score
            f.write(str(currentScore))
        finalScore = f.read()
    return finalScore

print(game(20))