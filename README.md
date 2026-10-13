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

## How It Works

1. **User Authentication:** Patients, doctors, and hospital administrators log in according to their assigned roles.
2. **Hospital Management:** Administrators manage hospitals, departments, doctors, and bed availability.
3. **Appointment Scheduling:** Patients request appointments with doctors and track their appointment status.
4. **Emergency Response:** Patients submit emergency requests, which authorized hospital staff can review and manage.
5. **AI Risk Prediction:** The machine learning model estimates an emergency risk category using relevant patient information.
6. **Prescription Management:** Doctors create prescriptions that can be stored and accessed by authorized users.
7. **Medical Billing:** The system manages patient bills and payment status.
8. **Admin Dashboard:** Administrators oversee hospital operations and manage system records.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** MySQL
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Machine Learning:** Emergency risk classification

- ## System Workflow
<table>
<tr>
<td width="50%" valign="top">

<h3 align="center">Hospital Management Workflow</h3>

<pre>
          LOGIN
            |
            v
        DASHBOARD
            |
   +--------+--------+
   |        |        |
   v        v        v
HOSPITAL PATIENT  DOCTOR
MANAGEMENT MANAGEMENT MANAGEMENT
   |        |        |
   v        |        v
HOSPITAL    |   APPOINTMENTS
   |        |        |
   +----+---+        v
        |       PRESCRIPTION
        v
   DEPARTMENTS
        |
   +----+--------+
   |    |        |
   v    v        v
EMERGENCY CARDIOLOGY NEUROLOGY
        |
        v
  BED MANAGEMENT
        |
   +----+--------+
   |    |        |
   v    v        v
 ICU-01 ICU-02 GENERAL-01
</pre>

</td>
<td width="50%" valign="top">

<h3 align="center">Emergency Response & Billing</h3>

<pre>
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
</pre>

</td>
</tr>
</table>


## Installation

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   ```

   Windows:

   ```bash
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure database settings and required environment variables.

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.


### 🗄️ Database Setup

This project uses MySQL as its database.

1. Install MySQL Server.
2. Create a database in MySQL.
3. Update the database credentials in `settings.py`.
4. Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
**Note:** The database itself is not included in this repository. Tables are created using Django migrations.
## Note


Machine learning-based risk classification is intended to support emergency assessment and does not replace professional medical judgment. In real emergencies, qualified medical professionals must determine patient priority and treatment.



