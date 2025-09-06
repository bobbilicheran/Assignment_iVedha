# Assignment

This project has three tests. Each test is in its own folder.

---

## Test1: Service Monitor and REST API

**Files**
- `monitor_services.py` → checks if httpd, rabbitmq-server, and postgresql are running.  
  Creates JSON files with service name, status (UP/DOWN), and host name.  

- `rest_service.py` → Flask REST API.  
  - `POST /add` → insert JSON data into Elasticsearch  
  - `GET /healthcheck` → return overall application status  
  - `GET /healthcheck/<service>` → return one service status  

- `requirements.txt` → needed Python packages (Flask, Elasticsearch client).  
- `.gitignore` → ignores JSON files in the `output/` folder.  

**How to run**
```bash
cd test1
python3 monitor_services.py
python3 rest_service.py

## Test2: Ansible Inventory and Playbook

### Files

- `inventory` → has three groups: httpd, rabbitmq, postgresql.  
  > Note: host1, host2, host3 are placeholders. Replace with real IPs or hostnames if running on actual servers.  

- `assignment.yml` → playbook with three tasks:  
  - `verify_install` → check or install httpd service  
  - `check-disk` → check disk usage, send mail if usage >80%  
  - `check-status` → call REST API from Test1 to get application status  

### How to run
```bash
ansible-playbook assignment.yml -i inventory -e task_action=verify_install
ansible-playbook assignment.yml -i inventory -e task_action=check-disk
ansible-playbook assignment.yml -i inventory -e task_action=check-status

# Test3: CSV Data Processing

### Files

- `Assignment python.csv` → input file with property sales data  
- `filter_sales.py` → Python script to calculate average price per sq ft and select properties below the average  
- `below_average_price_per_foot.csv` → output file created by the script  

### How to run
```bash
cd test3
python3 filter_sales.py

This will generate below_average_price_per_foot.csv.

Notes

Python 3 is required.

Install pandas with:

pip install pandas


Some files (like CSV output) are generated when you run the script.

