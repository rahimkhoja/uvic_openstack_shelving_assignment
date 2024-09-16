# UVic OpenStack VM Shelving System

## Overview
This repository houses the codebase and documentation for the UVic OpenStack VM Shelving System. This automated system is designed to efficiently manage the lifecycle of virtual machines (VMs) within the Arbutus cloud environment. By identifying and shelving VMs that have been inactive for more than 30 days, the system aims to optimize resource utilization, minimize disruption for researchers, and reduce operational overhead.

## Features
- **Automated Shelving:** Automatically shelves VMs that have been inactive for over 30 days.
- **Email Notifications:** Sends email alerts to VM owners, providing options to defer shelving.
- **Integration with GitHub Actions:** Utilizes GitHub Actions to schedule and execute tasks.
- **Flask Web Server:** A secure Flask-based web server, utilizing Shibboleth for user authentication, facilitates user interactions.
- **Request Tracker Integration:** Automates ticket creation and tracking through Request Tracker (RT), enhancing the auditing process.
- **Comprehensive Logging:** Implements detailed logging of all actions, ensuring a robust audit trail.

For more detailed information on system operations and setup procedures, please refer to the `DOCS.md` file in this repository.
