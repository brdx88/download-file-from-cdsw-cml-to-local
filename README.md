# CDSW/CML File Downloader to Local using Selenium Automatically
This project demonstrates an automated approach to downloading files from a cdsw/cml (Cloudera Machine Learning/Cloudera Data Science Workbench) interface using Python and Selenium. The script logs into a cdsw/cml environment, navigates through project folders, sorts files by modification date, and downloads the most recent file using automated interactions.

## Problems
Imagine the process of manually downloading monitoring reports from CDSW/CML on a weekly basis is time-consuming and tedious. With over 10 files to download each week, the repetitive task of navigating through the project directories, sorting the files, and manually clicking download is both inefficient and error-prone. This problem is compounded by the fact that the files are buried within the project directory structure, requiring several clicks to access and sort the correct files. Automating this process would save significant time and reduce manual errors.

## Features
- **Automated Login**: Automatically logs into the cdsw/cml platform using provided credentials.
- **Folder Navigation**: Navigates through the cdsw/cml interface to locate the project and desired folder.
- **File Sorting**: Sorts the files by "Last Modified" date to ensure the latest file is selected.
- **File Download**: Automatically clicks the "Download" button and handles Chrome's download prompt.
- **User-Defined Download Directory**: Files are saved to a custom download directory.
- **Custom Chrome Settings**: Chrome browser is configured with specific options for automation and file download handling.

## Dependencies
To run the script, you will need the following Python packages:
```bash
pip install selenium webdriver-manager pyautogui
```
- Selenium: For browser automation.
- webdriver-manager: Automatically manages and downloads the appropriate ChromeDriver version.
- autogui: Handles mouse actions for the download prompt in Chrome.

## Setup Instructions
1. Clone the Repository:
   ``` bash
   git clone https://github.com/your-username/cdsw/cml-file-downloader.git
   ```
2. Configure the Download Directory and Credentials: Update the following variables in the script:
    - `download_dir`: Path to the folder where files will be downloaded.
    - `cdsw/cml_user`: Your cdsw/cml username.
    - `cdsw/cml_pssw`: Your cdsw/cml password.
    - `cdsw/cml_url`: URL of your cdsw/cml environment.
3. Chrome Preferences: The script configures the Chrome browser to:
    - Set a default download directory.
    - Disable download prompts for a seamless experience.
4. Run the Script: Run the Python script to start the automation process:
  ```bash
  python cdsw/cml_file_downloader.py
  ```

## How It Works
1. Login: The script waits for the login page to load, enters the username and password, and submits the form.
2. Folder Navigation: The script navigates through the project directories to reach the specific file folder.
3. File Selection: It sorts the files based on the "Last Modified" date, selecting the latest file.
4. Download: The "Download" button is clicked, and pyautogui is used to click the "Keep" button if Chrome displays a download security prompt.
5. Completion: Once the file is downloaded, the browser is closed automatically.

## Key Code Sections
1. Login Automation:
   ```python
   username_input.send_keys(cdsw/cml_user)
   password_input.send_keys(cdsw/cml_pssw)
   login_button.click()
   ```
2. File Sorting:
   ```python
   last_modified_button.click()
   last_modified_button_desc.click()
   ```
3. Download Handling
   ```python
   download_link.click()
   pyautogui.click(keep_button_x, keep_button_y)
   ```
### Notes
The `pyautogui` coordinates for clicking the "Keep" button may vary depending on the screen size and Chrome's layout. You may need to adjust the values for `keep_button_x` and `keep_button_y` based on your monitor.
Ensure that the appropriate version of Chrome and ChromeDriver are installed for compatibility.

## Conclusion
This project automates the process of navigating through the cdsw/cml interface, sorting files by modification date, and downloading the latest file. It's designed to save time and improve efficiency by eliminating manual steps in the file download process.
