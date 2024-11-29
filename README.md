<h1>Overview</h1>
<p>This project focuses on the development of a real estate listings website utilizing the Django framework integrated with various AWS services. The website aims to provide users with a seamless property browsing and listing experience, leveraging AWS services such as AWS CodePipeline, Amazon S3, CloudWatch, and AWS Elastic Beanstalk for efficient deployment, scaling, and management.</p>

## **Features**
- **Property Management**: Add, edit, and delete property listings with attributes such as location, price, size, and type.
- **User Authentication**: Secure login and registration system for administrators and users.
- **Client Management**: Keep track of buyers, sellers, and rental inquiries.
- **Transaction Handling**: Record and manage property transactions securely.
- **Search and Filter**: Advanced search functionality to filter properties by location, budget, and type.
- **Responsive Design**: A mobile-friendly interface for seamless interaction across devices.

---

## **Technology Stack**
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for styling).
- **Backend**: Django (Python).
- **Database**: SQLite (default), with the option to use PostgreSQL or MySQL for production.
- **Deployment**: AWS Beanstalk
- **APIs**: Django REST Framework for creating RESTful APIs.

---

## **Installation**

To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tobilobade/Cpp-Real-estate-project.git
   cd Cpp-Real-estate-project
   
2.  **Set up Instructions**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
