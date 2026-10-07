import csv

try:
    with open("patients.csv", "r") as file:
        reader = csv.DictReader(file)
        patients = list(reader)

    print("All Patient Details:")
    for patient in patients:
        print(patient)

    patient_id = input("\nEnter Patient ID to search: ")

    found = False

    for patient in patients:
        if patient["Patient ID"] == patient_id:
            print("\nPatient Found:")
            for key, value in patient.items():
                print(f"{key}: {value}")
            found = True
            break

    if not found:
        print("Patient not found.")

except FileNotFoundError:
    print("Error: patients.csv file not found.")
except Exception as e:
    print("Error:", e)
