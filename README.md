Tkinter Git GUI Tool
Project Overview
A lightweight Python GUI application built with Tkinter that provides basic Git repository cloning functionality. This tool simplifies the process of cloning Git repositories by offering a user-friendly interface.

Key Features
Simple and intuitive GUI interface
Repository cloning functionality
Support for both direct URLs and configured repository names
Threaded operations to prevent UI freezing
Error handling with user-friendly messages
Technology Stack
Python 3.x
Tkinter for GUI
GitPython for Git operations
JSON for configuration
Installation
Clone this repository:
bash
Copy Code
git clone https://github.com/wrhz/.git
Install required dependencies:
bash
Copy Code
pip install -r requirements.txt
Configuration
Create a config.json file in the src directory with your preferred repository shortcuts:

json
Copy Code
{
  "names": {
    "shortcut1": "https://github.com/user/repo1.git",
    "shortcut2": "https://github.com/user/repo2.git"
  }
}
Usage
Run the application:
bash
Copy Code
python main.py
Select "克隆仓库" (Clone Repository) from the dropdown
Enter either:
A full Git repository URL
A configured repository name from config.json
Specify the local path where you want to clone the repository
Click "克隆" (Clone) button
Contribution Guidelines
We welcome contributions! Please follow these steps:

Fork the repository
Create a new branch for your feature
Submit a pull request with a clear description of your changes
License
This project is licensed under the MIT License - see the LICENSE file for details.

Why This Project?
This tool demonstrates:

Practical application of Python GUI development
Integration with Git operations
Clean code structure
Good documentation practices
Perfect for developers looking to learn about:

Tkinter GUI development
Git operations programmatically
Threading in Python applications
Configuration management
Future Roadmap
Add more Git operations (pull, push, commit)
Implement repository management features
Add dark/light theme support
Support for multiple Git providers
