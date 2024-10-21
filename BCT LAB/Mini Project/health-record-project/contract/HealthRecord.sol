pragma solidity ^0.6.0;

contract Health_Record {

    struct Patient {
        int patient_id;
        string name;
        string height;
        string weight;
        string disease;
        string symptom1;
        string symptom2;
    }

    Patient[] public Patients;

    // Add a new patient record
    function addPatient(int patient_id, string memory name, string memory height, string memory weight, string memory disease, string memory symptom1, string memory symptom2) public {
        Patient memory patient = Patient(patient_id, name, height, weight, disease, symptom1, symptom2);
        Patients.push(patient);
    }

    // Retrieve patient details by patient_id
    function getPatient(int patient_id) public view returns (string memory, string memory, string memory, string memory, string memory, string memory) {
        for (uint i = 0; i < Patients.length; i++) {
            if (Patients[i].patient_id == patient_id) {
                return (
                    Patients[i].name,
                    Patients[i].height,
                    Patients[i].weight,
                    Patients[i].disease,
                    Patients[i].symptom1,
                    Patients[i].symptom2
                );
            }
        }
        return ("Name not Found", "Height not Found", "Weight not Found", "Disease not Found", "Symptom1 not Found", "Symptom2 not Found");
    }
}