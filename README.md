# Domain to IP Converter Tool

![Domain to IP](https://img.shields.io/badge/Developed_by-Eclibes_Security_Labs-brightgreen)

This tool converts domain names to their corresponding IP addresses in bulk using multi-threading for faster processing. It supports reading a list of domains from a file and outputs the IP addresses to a specified file. Duplicates are automatically removed from the result.

## Features
- Multi-threaded for fast domain resolution.
- Handles both valid and invalid domain inputs.
- Outputs the resolved IP addresses to a file.
- Automatically removes duplicate IP addresses.
- Color-coded output for clarity:
  - Green for successfully resolved domains.
  - Red for invalid or unresolved domains.
  
## Installation
This tool requires Python 3. Install the required libraries using `pip`:

```
pip install colorama
Usage
Clone the repository:

git clone https://github.com/eclibesec/domi.git
cd domi
Run the script:
python domain_to_ip.py
Provide the required inputs:

A file containing the list of domains.
The desired output file name.
The number of threads to use (between 1 and 100).
Example
If you have a file domains.txt with the following contents:

example.com
invalid-domain
google.com
You would run the script like this:


$ python domain_to_ip.py
$ give me your file: domains.txt
$ output filename? : output.txt
threads > 1-100: 10
The output would look like this:

[example.com -> 93.184.216.34]
[bad -> invalid-domain]
[google.com -> 142.250.72.14]
Data has been saved to 'output.txt'
Duplicate lines have been removed from 'output.txt'
The output.txt file will contain:
93.184.216.34
142.250.72.14
Error Handling
If the input file is not found, an error message will be displayed.
If any domain is invalid or cannot be resolved, it will be marked with a red bad -> domain_name.
License
This tool was developed by Eclibes Security Labs. You are free to use and modify it under the MIT License.
