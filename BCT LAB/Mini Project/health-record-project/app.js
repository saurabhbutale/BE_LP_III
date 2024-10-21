// Ensure MetaMask is injected into the browser (Injected Provider)
if (typeof window.ethereum !== 'undefined') {
    console.log('MetaMask is installed!');
    window.web3 = new Web3(window.ethereum);

    // Request access to MetaMask accounts
    ethereum.request({ method: 'eth_requestAccounts' }).catch((error) => {
        console.error("User rejected account access", error);
    });
} else {
    alert('Please install MetaMask to interact with this application.');
}

// Contract Address from Remix deployment
const contractAddress = '0xe0282ce0ca96bbb09589c87a2ec13d07fe27b9ab'; // Replace with your deployed contract address

// Contract ABI
const contractABI = [
    {
        "inputs": [
            {
                "internalType": "int256",
                "name": "patient_id",
                "type": "int256"
            },
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "height",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "weight",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "disease",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symptom1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symptom2",
                "type": "string"
            }
        ],
        "name": "addPatient",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "int256",
                "name": "patient_id",
                "type": "int256"
            }
        ],
        "name": "getPatient",
        "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "name": "Patients",
        "outputs": [
            {
                "internalType": "int256",
                "name": "patient_id",
                "type": "int256"
            },
            {
                "internalType": "string",
                "name": "name",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "height",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "weight",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "disease",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symptom1",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "symptom2",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
];

// Initialize Contract
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Form submission handler to add a new patient
document.getElementById('patientForm').onsubmit = async (event) => {
    event.preventDefault();

    const patientId = document.getElementById('patientId').value;
    const name = document.getElementById('name').value;
    const height = document.getElementById('height').value;
    const weight = document.getElementById('weight').value;
    const disease = document.getElementById('disease').value;
    const symptom1 = document.getElementById('symptom1').value;
    const symptom2 = document.getElementById('symptom2').value;

    // Get the user's MetaMask account
    const accounts = await ethereum.request({ method: 'eth_accounts' });

    // Call the contract's `addPatient` method
    contract.methods.addPatient(patientId, name, height, weight, disease, symptom1, symptom2)
        .send({ from: accounts[0] })
        .then(receipt => {
            alert('Patient added successfully!');
            console.log(receipt);
        })
        .catch(error => {
            console.error('Error adding patient:', error);
            alert('Error adding patient');
        });
};

// Function to fetch patient details
async function getPatient() {
    const patientId = document.getElementById('getPatientId').value;

    // Call the contract's `getPatient` method
    contract.methods.getPatient(patientId).call()
        .then(result => {
            const patientDetails = `Name: ${result[0]}, Height: ${result[1]}, Weight: ${result[2]}, Disease: ${result[3]}, Symptom 1: ${result[4]}, Symptom 2: ${result[5]}`;
            document.getElementById('patientDetails').innerText = patientDetails;
        })
        .catch(error => {
            console.error('Error fetching patient:', error);
            alert('Patient not found!');
        });
}
