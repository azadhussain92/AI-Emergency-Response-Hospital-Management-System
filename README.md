# AI Emergency Response & Hospital Management System

A full-stack hospital management and emergency response application built using Python, Django, Django REST Framework, SQL, and Machine Learning.

## Features

- Hospital and department management
- Patient and doctor profile management
- Emergency request management
- Appointment scheduling
- Prescription management
- Medical billing
- Machine learning-based emergency risk classification
- REST API development with Django REST Framework

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQL / MySQL
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Machine Learning:** Emergency risk classification
- 
- ## System Workflow
```text
                    LOGIN
                      |
                      v
                  DASHBOARD
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
 HOSPITAL         PATIENT         DOCTOR
 MANAGEMENT      MANAGEMENT      MANAGEMENT
       |              |              |
       v              |              v
   HOSPITAL           |          APPOINTMENTS
       |              |              |
       +-------+------+              v
               |                 PRESCRIPTION
               v
         DEPARTMENTS
               |
       +-------+--------+
       |       |        |
       v       v        v
   EMERGENCY CARDIOLOGY NEUROLOGY
               |
               v
          BED MANAGEMENT
               |
       +-------+--------+
       |       |        |
       v       v        v
    ICU-01  ICU-02  GENERAL-01


       EMERGENCY RESPONSE
               |
               v
       EMERGENCY REQUEST
               |
               v
        PATIENT DETAILS
               |
               v
       AI RISK PREDICTION
               |
               v
      DOCTOR / STAFF REVIEW
               |
               v
       EMERGENCY MANAGEMENT


       PRESCRIPTION
             |
             v
       BILLING MANAGEMENT
             |
             v
       BILL / PAYMENT STATUS
```


## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Configure database settings and environment variables.
5. Run migrations using `python manage.py migrate`.
6. Start the development server using `python manage.py runserver`.

## Note

Machine learning risk classification supports emergency prioritization and should not be treated as a substitute for professional medical judgment.
