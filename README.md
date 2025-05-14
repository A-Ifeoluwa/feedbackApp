
---

# Feedback Form with Automated Email Response

## Description

This project is a simple **Feedback Form** integrated with **Azure Functions** and **SendGrid** to automatically send an email confirmation to users upon form submission. It demonstrates the use of **Azure Functions** for handling API requests, **SendGrid** for sending emails, and a **Flask web application** for the user interface.

## Features

* **User Feedback Form**: Collects user's name, email, and message.
* **Automatic Email Response**: Sends a confirmation email to the user upon submission.
* **Azure Functions**: Handles the backend email processing.
* **SendGrid Integration**: Sends emails via the SendGrid API.

## Tech Stack

* **Frontend**: HTML, CSS
* **Backend**: Python (Flask)
* **Serverless**: Azure Functions
* **Email Service**: SendGrid

## Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd feedback-form
   ```

2. **Install required packages**:
   Ensure your `package.json` includes the necessary dependencies. Run:

   ```bash
   npm install
   ```

3. **Set up SendGrid**:

   * Sign up for SendGrid and create an API key.
   * Add your SendGrid API key as an environment variable (`SENDGRID_API_KEY`).

4. **Azure Functions**:

   * Create an **Azure Function** to handle the feedback submission.
   * Set the **API URL** in the Flask backend (`AZURE_FUNCTION_URL`).

5. **Run the Web App**:
   Start the Flask application:

   ```bash
   python app.py
   ```

   Open the web app in your browser to test the feedback form and the email functionality.

## Usage

* **Submit the Feedback Form**: Enter your name, email, and feedback, then click "Send Feedback."
* **Email Confirmation**: After submission, you will receive a confirmation email.

## License

This project is licensed under the MIT License.

---

Check out the project via this link below
https://feedbackapp-hxgggzehe6ecd3ev.eastus-01.azurewebsites.net/

