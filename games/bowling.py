#simulate a game of bowling
import random
random.seed

test = 5
testing = False
frame = 0
frames = 10
total = 0
score1 = 0
score2 = 0
score3 = 0
balls = []
frameResults = []

for i in range(frames):
    if testing:
        score1 = test
    else:
        score1 = int(input())
        #score1 = random.randint(0,10)
        
    balls.append(score1)

    if testing:
        score2 = test
    else:
        #score2 = random.randint(0, 10 - score1)
        score2 = int(input())
    
    if score1 != 10:
        balls.append(score2)
        
    if i == frames - 1:
        if score1 == 10:
            if testing:
                score2 = test
            else:
                #score2 = random.randint(0, 10)
                score2 = int(input())
            balls.append(score2)
        if score1 + score2 >= 10:
            if testing:
                score3 = test
            else:
                if score2 == 10:
                    #score3 = random.randint(0, 10)
                    score3 = int(input())
                else:
                    #score3 = random.randint(0, 10 - score2)
                    score3 = int(input())
            balls.append(score3)

print(balls)
prev = 0
skip = True
for i in range(len(balls)):
    if balls[i] == 10:
        print(i, balls[i])
        total += 10 + balls[i + 1] + balls[i + 2]
        frameResults.append(total)
        if i >= len(balls) - 3:
            total += balls[i + 1] + balls[i + 2]
            frameResults.append(total)
            print("strikeexit")
            break
        prev = balls[i]
        skip = True
        continue
    if skip == False and i != 0:
            print(i, balls[i], prev)
            if balls[i] + prev == 10:
                total += 10 + balls[i + 1]
                frameResults.append(total)
                if i >= len(balls) - 1:
                    print("spareexit")
                    break
            else:
                total += balls[i] + prev
                frameResults.append(total)
                if i >= len(balls):
                    print("exit")
                    break
        
    prev = balls[i]
    skip = not skip
        
print(frameResults)
