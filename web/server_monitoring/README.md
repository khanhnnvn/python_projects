# A simple server monitoring system using Flask web framework

### Usage: 
First time see this web app? please run the following commands to init database: <br/>
```
$ from server import init_db
$ init_db()
```
Now you are ready to go: <br/>
```
$ python server.py
```
And enjoy, access: http://127.0.0.1:5000

### Function:
- View all monitored servers
- Login / Logout (default user to login: admin/admin)
- Some functions only available when logged in:
   1. Add new server to monitor
   2. Add new user
   3. Remove existing server
   4. Remove existing user
