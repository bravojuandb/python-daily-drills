

latin_writers = {
    "Cicero": "rhetoric and philosophy",
    "Virgil": "epic poetry",
    "Horace": "lyric poetry and satire",
    "Ovid": "mythological storytelling and elegy",
    "Livy": "historical narrative",
    "Tacitus": "historical analysis and political commentary",
    "Seneca": "Stoic philosophy and tragedy",
    "Lucretius": "Epicurean philosophy and didactic poetry",
    "Catullus": "personal lyric poetry and invective",
    "Juvenal": "satirical criticism of Roman society",
    "Plautus": "comic theater and popular Latin comedy",
    "Terence": "refined comedic drama",
    "Propertius": "elegiac love poetry",
    "Martial": "epigrammatic wit and satire",
    "Quintilian": "rhetorical theory and education",
    "Suetonius": "imperial biography",
    "Sallust": "moralistic historiography",
    "Ennius": "early epic poetry and annalistic history",
    "Lucan": "historical epic poetry with Stoic overtones",
    "Apuleius": "novelistic prose and Platonism"
}
import pandas as pd

df = pd.DataFrame.from_dict(latin_writers, orient='index')

print(df)