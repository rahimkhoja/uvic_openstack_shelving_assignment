# UVic OpenStack VM Shelving System

## Overview

This repository contains the code and documentation for the UVic OpenStack VM Shelving System, an automated process designed to manage the lifecycle of virtual machines (VMs) by shelving those inactive for over 30 days. This system aims to optimize resource usage within the Arbutus cloud environment by minimizing disruption to researchers and reducing operational effort.

## Features

- Automated shelving of VMs inactive for more than 30 days.
- Email notifications to VM owners with options for deferral.
- Integration with GitHub Actions for scheduled task execution.
- Flask-based web server secured with Shibboleth authentication for user interactions.
- Integration with Request Tracket for automatic Ticket creation.
- Auditing via complex ticketing and detailed Log commiting.

For detailed system operations and setup, refer to the DOCS.md file.
