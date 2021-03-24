# TruSTAR-MISP Enclave Ingest

**© 2021, TruSTAR Technology. All rights reserved.**

**Requirements: Python3** | **Recommended:cURL**

## Contents of Repo

- ts-misp.py: Script to send reports and indicators from TruSTAR into MISP via the PyMISP and TruSTAR Python SDKs
- requirements.txt: Python requirements file to setup venv
- trustar.conf: TruSTAR Python SDK config file where API keys are stored
- definition.json: MISP trustar_report object definition file adding Threat Actor for certain premium intel feeds
- enclave_configs.conf: Config file where you specify which enclaves you would like to map into each use case

## How to Install and Run The Scripts

1. Log into TruSTAR Station and navigate to Settings > API. Check the agreement box and generate API Key & Secret
2. Copy API Key to user_api_key and API Secret to user_api_secret in `trustar.conf`
3. SSH into MISP server
4. Navigate to misp-objects folder to verify that trustar_report exists
   - ls -la /var/www/MISP/app/files/misp-objects/objects (you might need to use sudo)
   - if it does not exist, have your server admin add a `trustar_report` directory into that file path
   - within that trustar_report directory add the `definition.json` file included in this repo
5. In your SSH session verify that your MISP server can connect to TruSTAR's API
   - `curl -k -v -u %API_KEY%:%API_SECRET% -d "grant_type=client_credentials" https://api.trustar.co/oauth/token` (without the percentages around the api keys)
6. Exit your SSH session
7. Log into MISP web app, navigate to Global Actions > List Object Templates
   - Check to see if `trustar_report` displays on this page
   - If trustar_report exists in file system but does not show up here, click Update Objects
8. Within the script package folder provided, create a Python 'virtual environment':
   - `python3 -m venv trustar-misp`
9. Activate your virtual environment:
   - `source trustar-misp/bin/activate`
10. Use pip3 to install the dependencies required for this script to run (included in requirements.txt):
    - `pip3 install -r requirements.txt`
11. There are two required command line arguments to run the script:
    - k/-key: <MISP_KEY> - Found under the automation section on the MISP web interface
    - u/-url: <https://MISP.URL/>
12. There are also several optional command line arguments highlighted in the Command Line Arguments section.
13. Run the script:
    - EXAMPLE: `python3 ts-misp.py -k MISP_KEY -u https://<your MISP URL> [ANY ADDITIONAL OPTIONAL ARGUMENTS]`
    - If you are running this as a cron job, place the whole folder provided (including the venv you created) on your MISP server

## Command Line Arguments

- -k/-key: (OPTIONAL) MISP auth key - Found under the automation section on the MISP web interface. Can also be provided in `trustar.conf`
- -u/-url: (OPTIONAL) "https://YOUR_MISP_URL/". Can also be provided in `trustar.conf`
- -ev/-event: (OPTIONAL) Defaults to 1 - Map a bunch of IOCs to one MISP Event. Other options are: 2 - Well-formed TruSTAR reports as individual MISP Objects within the same MISP event; 3 - Well-formed TruSTAR reports map to an individual MISP event. Can also be provided in `trustar.conf`
- -ft/-from-time: (OPTIONAL) Default is 1 day ago. From time expressed as an ISO formatted date (YYYY-MM-DD ex. 2019-11-04)
- -tt/-to-time: (OPTIONAL) Default is datetime.now(). To time expressed as an ISO formatted date (YYYY-MM-DD ex. 2019-11-04)
- -e/-enclave-ids:(OPTIONAL) Default will search all private and premium intel enclaves. TruSTAR enclave id(s) to search from separated by commas. DO NOT PASS IN A LIST/ARRAY
- -ec/-enclave-configs: (OPTIONAL) Defaults to False - Specify "-ec" if you have specified you enclave configs in enclave_configs.conf. If you specify both "-ev" and "-ec" then "-ev" will be set to None. If you specify both "-e" and "-ec" the script defaults to "-e"
- -ecf/-enclave-configs-file: (OPTIONAL) Defaults to None - Path to enclave configs file if you don't use the standard file. NOTE: ENCLAVE CONFIGS FILE MUST BE SETUP EXACTLY LIKE 'enclave_configs.conf' TO WORK
- -db/-debug: OPTIONAL) Debug - Defaults to False - When "-db" is specified the script does not generate log files
- -s/-ssl-verify: (OPTIONAL) Defaults to True - Specify "-s" if you want to skip SSL validation, best practice is to enable SSL validation
- -d/-distribution: (OPTIONAL) Defaults to MISP.default_event_distribution in MISP config. Options are: 0 - Your organization only; 1 - This community only; 2 - Connected communities; 3 - All communities; 4 - Sharing Group; 5 - Inherit
- -sg/-sharing-group: (OPTIONAL) Defaults to None. Pass in Id parameter found under List Sharing Groups
- -t/-threat-level-id: (OPTIONAL) Defaults to MISP.default_event_threat_level in MISP config. Options are: 1 - High; 2 - Medium; 3 - Low; 4 - Undefined
- -a/-analysis: (OPTIONAL) Defaults to 0 (initial analysis). Other options are: 1 - Ongoing; 2 - Completed
- -p/-publish: (OPTIONAL) Defaults to False. Set to True if you want each MISP event to publish after it's been added/updated
