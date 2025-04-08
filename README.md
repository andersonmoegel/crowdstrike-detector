# CrowdStrike Falcon Installation Check

This Python script checks if **CrowdStrike Falcon** is installed on a Windows system and creates a temporary file if it is. The verification is performed using three different methods: installation folder, registry key, and running service.

## Features

- ✅ Checks if the CrowdStrike Falcon folder exists
- ✅ Verifies the Windows registry for the CrowdStrike service key
- ✅ Checks if the `CSFalconService` is running
- ✅ Creates a temporary file confirming installation
- ✅ Prints result messages to the terminal

## How It Works

### 1. Library Imports

```python
import os
import winreg
import subprocess
```

### 2. Configuration

```python
cs_path = r"C:\Program Files\CrowdStrike"
temp_file = r"C:\Windows\Temp\CrowdStrike_Installed.txt"
```

### 3. Functions

#### `is_crowdstrike_installed()`

Checks for:
- Existence of installation folder
- Registry key presence
- Running status of the service

#### `create_temp_file()`

Creates a `.txt` file in `C:\Windows\Temp\` with confirmation message.

#### `main()`

Runs the installation check and, if successful, creates the file and displays a success message.

### 4. Execution

```python
if __name__ == "__main__":
    main()
```

## Usage

Just run the script on a Windows system with Python installed.  
If CrowdStrike is detected, a file named `CrowdStrike_Installed.txt` will be created in `C:\Windows\Temp\`.

## Example Output

```bash
✅ CrowdStrike found! File created at C:\Windows\Temp\CrowdStrike_Installed.txt
```

## Possible Improvements

- Add exception logging and detailed error messages
- Detect different versions or installation paths of CrowdStrike

## License

This script is provided as-is, without warranty or guarantees. Use at your own discretion.
