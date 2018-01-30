#Rebecca TeKolste
#Homework 2, Problem 1

##Formula utility =  1.371(b1*b2*b3*b4*b5*b6*b7*b8) - 0.371

multiplier = 1.371
constant = .371

dictCoefficients = {'Vision':               [1.00, 0.98, 0.89, 0.84, 0.75, 0.61],
                    'Hearing':              [1.00, 0.95, 0.89, 0.80, 0.74, 0.61],
                    'Speech':               [1.00, 0.94, 0.89, 0.81, 0.68],
                    'Ambulation':           [1.00, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':            [1.00, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':              [1.00, 0.95, 0.85, 0.64, 0.46],
                    'Cognintion':           [1.00, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':                 [1.00, 0.96, 0.90, 0.77, 0.55]};

def get_score(vision, hearing, speech, ambulation, dexterity, emotion, cognition, pain):
    if not(vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision can only take 1-6')
    if not(hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing can only take 1-6')
    if not(speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech can only take 1-5')
    if not(ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation can only take 1-6')
    if not(dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity can only take 1-6')
    if not(emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion can only take 1-5')
    if not(cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition can only take 1-6')
    if not(pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain can only take 1-5')

    b1 = dictCoefficients['Vision'][vision - 1]
    b2 = dictCoefficients['Hearing'][hearing - 1]
    b3 = dictCoefficients['Speech'][speech - 1]
    b4 = dictCoefficients['Ambulation'][ambulation - 1]
    b5 = dictCoefficients['Dexterity'][dexterity - 1]
    b6 = dictCoefficients['Emotion'][emotion - 1]
    b7 = dictCoefficients['Cognintion'][cognition - 1]
    b8 = dictCoefficients['Pain'][pain - 1]

    score = multiplier*(b1*b2*b3*b4*b5*b6*b7*b8)-constant

    return score

#sanity test below
print(get_score(1, 1, 2, 3, 1, 1, 1, 1))
#All looks good.


