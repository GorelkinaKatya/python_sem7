poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
poem = list(poem.split())

def rythm(poem_letter):
    vowels = 'аеёиоуыэюя'
    count = 0
    for i in poem_letter:
        if i in vowels:
            count += 1
    return count

def same_by(rythm, poem):
    if len(set(map(rythm, poem))) < 2:
        return 'Парам пам-пам'
    else:
        return 'Пам парам'
    
print(same_by(rythm, poem))