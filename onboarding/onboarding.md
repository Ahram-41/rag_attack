# Student Onboarding

### Before Joining:
1. Attend the HSE (Health, Safety, and Environment) induction briefing.
2. Complete the online Fusionopolis 1 Staff and Student Safety Induction Course.
3. Send the HSE certificate once you pass the test.
4. Wait for a notification email to receive a temporary access card for Level 13.

### VPN

The team will help create the GPU cluster account, which requires an A*STAR VPN to access the GPU cluster.

The A*STAR VPN can be accessed using your A*STAR email address and password. If you do not have an A*STAR email, please approach your supervisor for help with VPN login credentials, which can be accessed through the IHPC laptop without the need for an A*STAR email account creation.

### Issuing IHPC Laptop and Granting VPN Access without an A*STAR Email

Ensure the following steps related to the provision of student accounts have been duly followed up prior to your appointment:

1. Ensure all your accounts (Windows ID, email, VPN) are formally activated, and you are able to log into your Windows account.

   - Ask your supervisor for assistance, and then contact the service desk at 6517 7979 for student account setup after the account has been created.
   - Example:
     - Username: ARES\stuXXX
     - UPN: stuXXX@cfar.a-star.edu.sg
     - Password: Contact the service desk at 6517 7979

2. Ensure the PC clinic staff helps you connect to A*STAR WiFi.

3. Ensure your CISCO AnyConnect VPN login details are correct: stuj?????????@ihpc.a-star.edu.sg.

4. Ensure you can connect to the VPN and link your mobile phone with the DUO client.

   - First, install the DUO app.

5. Set up your work environment – provide URLs and a list of software/packages/libraries/modules for installation.
   - Example:
     - Microsoft C++ Build Tools: https://github.com/bycloudai/InstallVSBuildToolsWindows (this build tool is for running some Python packages)
     - Node.js: https://nodejs.org/en/download/package-manager (if needed)
     - Python 3.11: https://www.python.org/downloads/release/python-3119/ (can be ignored if Conda is ready)

**Reminder:** If you encounter issues connecting to the ASTAR-Staff WiFi after being granted the DUO/Cisco VPN account, please make sure the other user on the laptop is logged out.

### Accessing the Login Node of the Cluster

It is recommended to use VS Code to open your home folder remotely.  
Add `10.2.57.100 canele` to `/etc/hosts` for easy access via `ssh userID@canele`.
Please see `canele-server.pdf` and `quickstart_cluster.pdf` for details.