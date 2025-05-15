"""
"""

latin_writers_structured = {
    "Cicero": {
        "name": "Cicero",
        "art": "rhetoric and philosophy"
    },
    "Virgil": {
        "name": "Virgil",
        "art": "epic poetry"
    },
    "Horace": {
        "name": "Horace",
        "art": "lyric poetry and satire"
    },
    "Ovid": {
        "name": "Ovid",
        "art": "mythological storytelling and elegy"
    },
    "Livy": {
        "name": "Livy",
        "art": "historical narrative"
    },
    "Tacitus": {
        "name": "Tacitus",
        "art": "historical analysis and political commentary"
    },
    "Seneca": {
        "name": "Seneca",
        "art": "Stoic philosophy and tragedy"
    },
    "Lucretius": {
        "name": "Lucretius",
        "art": "Epicurean philosophy and didactic poetry"
    },
    "Catullus": {
        "name": "Catullus",
        "art": "personal lyric poetry and invective"
    },
    "Juvenal": {
        "name": "Juvenal",
        "art": "satirical criticism of Roman society"
    },
    "Plautus": {
        "name": "Plautus",
        "art": "comic theater"
    },
    "Terence": {
        "name": "Terence",
        "art": "refined comedic drama"
    },
    "Propertius": {
        "name": "Propertius",
        "art": "elegiac love poetry"
    },
    "Martial": {
        "name": "Martial",
        "art": "epigrammatic wit and satire"
    },
    "Quintilian": {
        "name": "Quintilian",
        "art": "rhetorical theory and education"
    },
    "Suetonius": {
        "name": "Suetonius",
        "art": "imperial biography"
    },
    "Sallust": {
        "name": "Sallust",
        "art": "moralistic historiography"
    },
    "Ennius": {
        "name": "Ennius",
        "art": "early epic poetry and Roman history"
    },
    "Lucan": {
        "name": "Lucan",
        "art": "historical epic poetry with Stoic overtones"
    },
    "Apuleius": {
        "name": "Apuleius",
        "art": "novelistic prose and Platonism"
    }
}

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