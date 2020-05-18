# Simplest Water Reminder

## Screenshot

![Screenshot](screenshot/Ubuntu-Notification.png?raw=true)

## Installation

* Install the package [PyInstaller](https://github.com/pyinstaller/pyinstaller):

  ```terminal
    pip3 install pyinstaller
  ```

* Install the desktop notifications program libnotify-bin
  (being executed with the command `notify-send`).

  ```terminal
    sudo apt-get install libnotify-bin
  ```

## Usage

Just run the command:

* Wait! before executing the command below:
  * check if the your PYTHONPATH is indeed /usr/bin/python3
  (like written in the first line of app.py).
  * If it's not, just check your path with the command `which python3`
  and then replace the path written in the file with your path.

```terminal
  pyinstaller --onefile app.py --name "Water Reminder" --distpath [DIR_FOR_APP]]
```

## Turning ON/OFF

* Turn on – Execute the executable file, located in the directory you chose ([DIR_FOR_APP])
* Turn off – From the "System Monitor".
  Just search for Water Reminder and end its process.

## Additional information

* And of course if you want the app to have an icon,
  just change it manually after making it executable.

* If you want to change the title/body of the notification
  and/or the time between each notification, edit app.py as you prefer.

* If you want to change the app for your own needs just:
  * Change app.py accordingly
  * Copy .gitignore, app.py and the readme.md to another new directory
  * Execute the above-mentioned pyinstaller command again in that new directory.
  * Change the picture of the executable program again.

### Thanks

This app have the capability to become executable
with the help of the awesome Python package – [PyInstaller](https://github.com/pyinstaller/pyinstaller)
