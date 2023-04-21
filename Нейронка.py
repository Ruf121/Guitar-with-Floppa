import librosa
import numpy as np
from Переделка import model
# Создать словарь, отображающий индекс аккорда в его название
chord_idx = {0: 'C',
             1: 'D',
             2: 'Dm',
             3: 'E',
             4: 'F',
             5: 'G',
             6: 'A',
             7: 'H',
             8: 'Hm',
             9: 'Am',
             10: 'Cm',
             11: 'C#m',
             12: 'Em',
             13: 'Fm',
             14: 'Gm',
             }


# Функция, которая будет проходить через нейросеть, чтобы определить аккорд
def classify_chord(file_path):
    # Загрузить аудио файл и извлечь его функции mfcc
    y, sr = librosa.load(file_path, mono=True, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)

    # Изменить размерность mfcc для использования в модели
    mfcc = np.expand_dims(mfcc, axis=0)
    mfcc = np.expand_dims(mfcc, axis=-1)

    # Передать mfcc через модель и получить индекс предсказанного аккорда
    pred_idx = model.predict(mfcc).argmax(axis=-1)[0]

    # Получить соответствующее имя аккорда из словаря chord_idx
    chord_name = chord_idx[pred_idx]

    return chord_name

# classify_chord(model) Удобнее вызвать функцию из другого файла(возможно)
