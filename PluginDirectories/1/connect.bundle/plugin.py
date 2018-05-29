import os, json, commands

def run(cmd):
    os.system(cmd)

def results(fields, original_query):
    settings = json.load(open('preferences.json'))
    devices = settings["devices"]
    device_name = str(fields.get("~device"))

    for device in devices:
        if device_name.lower() == device["alias"].lower():
            device_name = device["fullname"]
            break

    command = "osascript toggle.applescript \"{0}\"".format(device_name)
    if "connect" in fields:
        return {
            "title": "Connect " + device_name,
            "run_args": [command + " Connect"]
        }
    elif "disconnect" in fields:
        return {
            "title": "Disconnect " + device_name,
            "run_args": [command + " Disconnect"]
        }
    elif "toggle" in fields:
        return {
            "title": "Toggle " + device_name,
            "run_args": [command + " Toggle"]
        }