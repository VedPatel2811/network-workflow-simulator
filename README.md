# Network Workflow Simulator

## Project Description
The **Network Workflow Simulator** is a simplified network elements workflow simulator inspired by Ciena's PlannerPlus. Built using Python and Flask, it provides a web-based interface to simulate basic network workflows and configurations. This tool demonstrates proficiency in Python, web development, database management, and debugging techniques, offering a platform for testing and verification.

### Features
- Web-based interface using Flask
- Basic network workflow simulation
- Data storage with SQLite
- Logging and debugging capabilities
- Easy-to-use form for adding new workflows

## Prerequisites
- Python 3.x
- Flask
- SQLite
- Any IDE (VS Code recommended)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/VedPatel2811/network-workflow-simulator.git
   cd ciena-network-workflow-simulator
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open a browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
Network-Workflow-Simulator/
├── app.py            # Main Flask application
├── templates/        # HTML templates for the web interface
├── static/           # CSS and JavaScript files
├── database.db       # SQLite database for storing configurations
└── README.md         # Project documentation
```

## Usage
1. Open the web application in your browser.
2. Add a new workflow using the form.
3. The newly added workflow will be displayed in the list below the form.
4. Check the SQLite database to confirm that the entry has been recorded.

## Example Workflow
1. Open the application at `http://127.0.0.1:5000/`
2. Enter a **workflow name** and **status** in the form.
3. Click **Add Workflow**.
4. The workflow will appear in the list of existing workflows.

## Future Enhancements
- Integrate real network element simulation
- Implement workflow state transitions
- Add REST API endpoints for external integration

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to open issues and submit pull requests.

## Contact
For any inquiries or issues, please contact [Ved Patel](mailto:veds28112004@gmail.com).
