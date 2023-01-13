import pandas as pd


def get_patients():
    patients = pd.read_csv('data/cancer_patient_data_sets.csv')
    patients = patients.replace(to_replace="Low", value=0)
    patients = patients.replace(to_replace="Medium", value=0)
    patients = patients.replace(to_replace="High", value=1)
    return patients


def drop_useless_from(patients):
    patients.drop(
        ['index', 'Patient Id', 'OccuPational Hazards', 'Genetic Risk', 'chronic Lung Disease', 'Balanced Diet',
         'Obesity',
         'Chest Pain', 'Coughing of Blood', 'Fatigue', 'Weight Loss', 'Shortness of Breath', 'Wheezing',
         'Swallowing Difficulty',
         'Clubbing of Finger Nails', 'Frequent Cold', 'Dry Cough'], axis=1, inplace=True)


def fill_empty_values(patients):
    patients.fillna(patients.mean(), inplace=True)
    print('Empty values filled!\n')
