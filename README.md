# Github Visitor Info Admin Panel

Welcome to the Django Admin Panel for GitHub Insights! This repository provides a front-end interface for visualizing the visitor data collected from GitHub profile links. It allows users to see detailed insights, including visitor locations and traffic patterns.

## Features

- **Location Insights**: Displays the city, state, and country of visitors to your GitHub profile.
- **Traffic Analytics**: Provides hourly and weekly visit trends.
- **User Account System**: Allows users to create accounts and generate unique tracking links.

## How It Works

1. **User Registration**: Users must create an account to generate a unique tracking link for their GitHub profile.
2. **Data Display**: The panel displays aggregated data collected via the Flask API, including location and visit patterns.

## Prerequisites

- **Python 3.8+**: Ensure you have Python installed.
- **Docker**: Recommended for containerized deployment.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/dpshah23/GitHub-Insights-Django-Admin.git](https://github.com/dpshah23/Github-Visitor-Info-Admin.git)
   cd Github-Visitor-Info-Admin
   ```

2. **Set Up Environment Variables**:
   - Create a `.env` file with the necessary configuration, including database settings and secret keys in project folder.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Application**:
   ```bash
   python manage.py runserver
   ```

## Docker Deployment

1. **Build and Run Docker Container**:
   ```bash
   docker-compose up --build
   ```

## VPS Hosting

For optimal performance and integration, it is recommended to host both the Flask API and Django Admin Panel on a Virtual Private Server (VPS). This setup ensures seamless communication and data flow between the two components.

## Contribution

Contributions are welcome! Feel free to open an issue or submit a pull request for new features or improvements.


---

*Note*: This panel **does not store IP addresses**. It only displays non-personalized data collected via the Flask API.

For any inquiries, contact us at [dpshah2307@gmail.com](mailto:dpshah2307@gmail.com).
