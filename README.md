**This script helps fetch Collection Protocol (CP) details from OpenSpecimen using its REST API and saves the output as a JSON file.**

---

## **Introduction**

This script demonstrates how to:

- Authenticate with OpenSpecimen using REST API
- Input a CP ID from the user
- Fetch details of the Collection Protocol
- Save the CP data as a `.json` file

---

### **Requirements**
- Python 3.x
- `requests` module  

### **Steps to Run**

1. Clone or download this repository.
2. Navigate to the folder where the script is saved.
3. Run the script using:   python3 cp_audit.py
4. The CP details will be saved in a file named cp_<id>.json.

### **What I Learned**
1. How to authenticate and generate a session token using OpenSpecimen REST APIs.
2. How to send GET and POST requests using the Python requests library.
3. How to handle and save JSON responses.
4. How to manage user input and simple error handling in Python.
5. A better understanding of OpenSpecimen's API structure.

