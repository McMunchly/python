#simulate a game of bowling
import random
random.seed


testing = False
frames = 10
total = 0
score1 = 0
score2 = 0
score3 = 0
balls = []
frameResults = []

for i in range(frames):
    print("Frame: " + str(i + 1))
    
    if testing:
        score1 = int(input())
    else:
        score1 = random.randint(0,10)

    balls.append(score1)

    if testing:
        score2 = int(input())
    else:
        score2 = random.randint(0, 10 - score1)

    if score1 == 10:
        print("STRIKE!!!")
    else:
        print(score1)
        balls.append(score2)
        
        if score1 + score2 == 10:
            print("Spare!")
        else:
            print(score2)
        
    if i == frames - 1:
        if score1 == 10:
            if testing:
                score2 = int(input())

                if score1 + score2 == 10:
                    print("Spare!")
            else:
                score2 = random.randint(0, 10)

            if score2 == 10:
                print("STRIKE!!!")
            balls.append(score2)
        if score1 + score2 >= 10:
            if testing:
                score3 = int(input())
            else:
                if score2 == 10:
                    score3 = random.randint(0, 10)
                else:
                    score3 = random.randint(0, 10 - score2)

            if score1 == 10:
                print("STRIKE!!!")
            balls.append(score3)

print(balls)
prev = 0
skip = True
frame = 1
for i in range(len(balls)):
    if balls[i] == 10:
        total += 10 + balls[i + 1] + balls[i + 2]
        frameResults.append(total)
        if i >= len(balls) - 3:
            if frame == 9:
                print("swoop")
                total += balls[i + 1] + balls[i + 2]
                frameResults.append(total)
            break
        prev = balls[i]
        skip = True
        frame += 1
        continue
    if skip == False and i != 0:
            if balls[i] + prev == 10:
                total += 10 + balls[i + 1]
                frameResults.append(total)
                if i >= len(balls) - 1:
                    break
            else:
                total += balls[i] + prev
                frameResults.append(total)
                if i >= len(balls):
                    break
        
    prev = balls[i]
    skip = not skip
    if i % 2 == 0:
        frame += 1
        
print(frameResults)
print("Your final score is: " + str(total))
