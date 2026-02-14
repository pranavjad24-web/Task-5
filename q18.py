class Patient:
    def __init__(self, pid, name, diagnosis):
        self.pid = pid
        self.name = name
        self.diagnosis = diagnosis

class GeneralPatient(Patient):
    def treatment_cost(self):
        return 1000

class ICU_Patient(Patient):
    def treatment_cost(self):
        return 5000

p = ICU_Patient(1, "Arun", "Critical")
print("Treatment Cost:", p.treatment_cost())
