import os, sys
from os.path import abspath, join


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


PASSWORDS = {
    'DB_MANAGER': 'dbManager',
    'INVENTORY_PASS': "inventory2021!"
}
FILE_PATHS = {
    # 'DB_LOCATION': "C:\\Users\\Eyonai\\Documents\\GitHub\\AutoBaseline\\Code\\db\\",
    'DB_LOCATION': "L:\\Testing\\Matrix\\Eran Yonai\\Auto Baseline Validation\\dbs\\",
    'POWERSHELL': 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe',
    'SPU_DIALOG': resource_path('Forms\\spu_dialog.ui'),
    'BASELINE_LOG': os.getenv('APPDATA') + '\\auto_baseline_logs.log',
    'INVENTORY_LOG': os.getenv('APPDATA') + '\\inventory_logs.log'
}

APPLICATION_VERSION = {
    'AutoBaseline': '1.3',
    'Inventory': '1'
}

TABLE_NAMES = {
    'WORKSTATION': 'workstations',
    'SYSTEM': 'systems',
    'ULS': 'ultrasounds',
    'STOCKERT': 'stockerts',
    'NGEN': 'ngens',
    'NMARQ': 'nmarqs',
    'SMARTABLATE': 'smartablates',
    'PACER': 'pacers',
    'DONGLE': 'dongles',
    'EPU': 'epus',
    'PRINTER': 'printers',
    'SPU': 'spus',
    'DEMO': 'demos',
    'workstations': 'WS',
    'systems': 'SYSTEM',
    'ultrasounds': 'ULS',
    'stockerts': 'STOCKERT',
    'ngens': 'NGEN',
    'nmarqs': 'NMARQ',
    'smartablates': 'SMARTABLATE',
    'pacers': 'PACER',
    'dongles': 'DONGLE',
    'epus': 'EPU',
    'printers': 'PRINTER',
    'spus': 'SPU',
    'demos': 'DEMO'
}

DIALOGS_FIELD_NAMES = {
    'workstations': ['Service Tag', 'DSP Version', 'Image Version', 'Configuration', 'Model', 'Graphics Card'],
    'systems': ['System Number', 'PIU Configuration', 'Location Pad', 'Patch Unit', 'Monitor 1', 'Monitor 2',
                'ECG Phantom', 'Aquarium Number', 'Aquarium Maximo'],
    'ultrasounds': ['Serial Number', 'Ultrasound System', 'Software Version', 'Application Version', 'Video Cable',
                    'Etherent Cable'],
    'stockerts': ['System SW', 'Serial Number', 'Stockert EP IO SN', 'EP IO Interface cable', 'EP Shuttle to PIU',
                  'Global Port', 'Ablation Adaptor CBL', 'RFG to WS Cable', 'Patch Electrode Cable', 'Foot Pedal'],
    'smartablates': ['System SW', 'Serial Number', 'RFG to PIU Cable', 'RFG to WS Cable', 'Foot Pedal'],
    'ngens': ['Console SW', 'Console PN', 'Console Version', 'PSU SN', 'PSU PN', 'PSU Cable', 'RFG to PIU Cable',
              'Monitor 1 SN', 'Monitor 1 PN', 'Monitor 1 Version', 'Monitor 1 Hub SN', 'Monitor 1 Hub PN',
              'Monitor 1 PSU SN', 'Monitor 1 PSU PN', 'Monitor 2 SN', 'Monitor 2 PN', 'Monitor 2Version',
              'Monitor 2 Hub SN', 'Monitor 2 Hub PN', 'Monitor 2 PSU SN', 'Monitor 2 PSU PN', 'nGEN Pump SN',
              'nGEN Pump PN', 'nGEN Pump Version', 'Pump to Console Cable', 'Foot Pedal'],
    'nmarqs': ['System SW', 'Serial Number', 'RFG to Carto Cable', 'Ethernet Cable', 'RFG to Pump Cable',
               'RFG to Monitor', 'CoolFlow Pump SN', 'CoolFlow Pump Model', 'Foot Pedal'],
    'pacers': ['Pacer Type', 'Serial Number'],
    'dongles': ['Dongle SN', 'Dongle SW Version', 'Dongle HW Version'],
    'printers': ['Printer Model', 'Printer SN'],
    'epus': ['Unit SN', 'Unit Version'],
    'spus': ['Serial Number', 'Part Number', 'SW Version', 'Main FW Version', 'Secondary FW Version', 'Front Board PN',
             'Front Board REV', 'Led Board PN', 'Led Board REV', 'Mother Board SN', 'Mother Board REV', 'Back Board PN',
             'Back Board REV', 'Power Board PN', 'Power Board REV', 'Upper Board PN', 'Upper Board REV',
             'Pacing Board PN',
             'Pacing Board REV', 'TPI Board SN', 'TPI Board REV', 'Digital Board SN', 'Digital Board REV',
             'ECG Board SN', 'ECG Board REV', 'SPU Prototypes PN', 'SPU Prototypes REV', 'MAG Location', 'MAG Location REV'],
    'demos': ['WS Type', 'SW Version', 'DSP Version', 'Image Version', 'Service Tag', 'SurPoint']
}

TABLE_FIELDS = {
    'WS': [["service_tag", "STRING PRIMARY KEY"], ["dsp_version", "STRING"], ["image_version", "STRING"],
           ["configuration", "STRING"], ["model", "STRING"], ["graphics_card", "STRING"],
           ["approved", "BOOLEAN"], ["used", "INTEGER"]],
    'SYSTEM': [["system_number", "STRING PRIMARY KEY"], ["piu_configuration", "STRING"],
               ["lp_number", "STRING"], ["patch_unit", "STRING"], ["monitor_1", "STRING"],
               ["monitor_2", "STRING"], ["ecg_phantom", "STRING"], ["aquarium_number", "STRING"],
               ["aquarium_maximo", "STRING"], ["approved", "BOOLEAN"], ["used", "INTEGER"]],
    'ULS': [["serial_number", "STRING PRIMARY KEY"], ["machine", "STRING"], ["software_version", "STRING"],
            ["application_version", "STRING"], ["video_cable", "STRING"],
            ["ethernet_cable", "STRING"], ["approved", "BOOLEAN"], ["used", "INTEGER"]],
    'STOCKERT': [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
                 ["epio_box_sn", "STRING"], ["epio_connection_cable", "STRING"],
                 ["epio_interface_cable", "STRING"], ["epushuttle_piu", "STRING"],
                 ["global_port", "STRING"],
                 ["ablation_adaptor_cable", "STRING"], ["gen_to_ws_cable", "STRING"],
                 ["patch_elect_cable", "STRING"], ["footpedal", "STRING"], ["approved", "BOOLEAN"],
                 ["used", "INTEGER"]],
    'NGEN': [["console_sn", "STRING PRIMARY KEY"], ["console_pn", "STRING"],
             ["console_version", "STRING"], ["psu_sn", "STRING"],
             ["psu_pn", "STRING"], ["psu_cable", "STRING"],
             ["gen_to_piu", "STRING"], ["monitor1_sn", "STRING"], ["monitor1_pn", "STRING"],
             ["monitor1_ver", "STRING"], ["monitor1_hubsn", "STRING"], ["monitor1_hubpn", "STRING"],
             ["monitor1_psusn", "STRING"],
             ["monitor1_psupn", "STRING"], ["monitor2_sn", "STRING"],
             ["monitor2_pn", "STRING"], ["monitor2_version", "STRING"], ["monitor2_hubsn", "STRING"],
             ["monitor2_hubpn", "STRING"], ["monitor2_psusn", "STRING"], ["monitor2_psupn", "STRING"],
             ["pump_sn", "STRING"], ["pump_pn", "STRING"], ["pump_version", "STRING"],
             ["pump_to_console", "STRING"], ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
             ["used", "INTEGER"]],
    'NMARQ': [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
              ["gen_to_carto", "STRING"], ["ethernet", "STRING"],
              ["gen_to_pump", "STRING"], ["gen_to_monitor", "STRING"],
              ["pump_sn", "STRING"],
              ["pump_model", "STRING"], ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
              ["used", "INTEGER"]],
    'SMARTABLATE': [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
                    ["gen_to_piu", "STRING"], ["gen_to_ws", "STRING"],
                    ["foot_pedal", "STRING"], ["approved", "BOOLEAN"],
                    ["used", "INTEGER"]],
    'PACER': [["serial_number", "STRING PRIMARY KEY"], ["type", "STRING"], ["approved", "BOOLEAN"],
              ["used", "INTEGER"]],
    'DONGLE': [["serial_number", "STRING PRIMARY KEY"], ["software_version", "STRING"],
               ["hardware_version", "STRING"], ["approved", "BOOLEAN"],
               ["used", "INTEGER"]],
    'EPU': [["serial_number", "STRING PRIMARY KEY"], ["version", "STRING"], ["approved", "BOOLEAN"],
            ["used", "INTEGER"]],
    'PRINTER': [["serial_number", "STRING PRIMARY KEY"], ["model", "STRING"], ["approved", "BOOLEAN"],
                ["used", "INTEGER"]],
    'SPU': [["serial_number", "STRING PRIMARY KEY"], ["pn", "STRING"],
            ["software_version", "STRING"], ["main_fw_version", "STRING"],
            ["secondary_fw_version", "STRING"], ["front_board_location", "STRING"],
            ["front_board_location_rev", "STRING"],
            ["led_board", "STRING"], ["led_board_rev", "STRING"], ["mother_board", "STRING"],
            ["mother_board_rev", "STRING"],
            ["back_board", "STRING"], ["back_board_rev", "STRING"], ["power_board", "STRING"],
            ["power_board_rev", "STRING"],
            ["upper_board", "STRING"], ["upper_board_rev", "STRING"], ["pacing_board", "STRING"],
            ["pacing_board_rev", "STRING"],
            ["tpi_board", "STRING"], ["tpi_board_rev", "STRING"], ["digital_board", "STRING"],
            ["digital_board_rev", "STRING"],
            ["ecg_board", "STRING"], ["ecg_board_rev", "STRING"], ["spu_pro", "STRING"],
            ["spu_pro_rev", "STRING"], ["mag_loc", "STRING"], ["mag_loc_rev", "STRING"], ["approved", "BOOLEAN"],
            ["used", "INTEGER"]],
    'DEMO': [["service_tag", "STRING PRIMARY KEY"], ["ws_type", "STRING"],
             ["sw_version", "STRING"], ["dsp_version", "STRING"],
             ["image_version", "STRING"], ["approved", "BOOLEAN"],
             ["used", "INTEGER"]]
}

MIN_CORRELATION = 0.7
MAX_CORRELATION = 1
PERCENTAGE_TO_PASS_DB = 0.75

SEARCH_CATALOG_COMMAND = '$s = Invoke-WebRequest -Uri "http://itsusrawsp10939.jnj.com/partnolookup/Main.aspx" -UseDefaultCredentials `\n' \
                         '-Method "POST" `\n' \
                         '-Headers @{ \n' \
                         '"Cache-Control"="max-age=0"\n' \
                         '"Upgrade-Insecure-Requests"="1"\n' \
                         '"Origin"="http://itsusrawsp10939.jnj.com"\n' \
                         '"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.58"\n' \
                         '"Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"\n' \
                         '"Referer"="http://itsusrawsp10939.jnj.com/partnolookup/Main.aspx"\n' \
                         '"Accept-Encoding"="gzip, deflate"\n' \
                         '"Accept-Language"="en-US,en;q=0.9,he;q=0.8"\n' \
                         '"Cookie"="_ga=GA1.2.231059344.1603268627; ASP.NET_SessionId=appg4m3nazairir3shlei445"\n' \
                         '} `\n' \
                         '-ContentType "application/x-www-form-urlencoded" `\n' \
                         '-Body ("__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=Jx1bFdZUxxK%2FIyJlVuaAS8d6GW%2F2MZKhNWzn7ZDD4xp1ptT4Zl4pr7PS1o7yb2RO%2F%2FFSGz7MkXsqu%2FD2i5c2hzHdq4FgBfjUoW5QDaa14%2BIlCGqsZUAVFmiB6TenAnicIBfJvHNjYRtz62Zag0Tq01i5ZKcngUt9DMa3d0ws7N%2BPGfciV7w3McgzH8SRRKPTKHutTYZ5SL%2FdEAQ7e0D2RpWwOpm9Z8mAtMVvuDz17wCjFqCEH37Sx3NoSW9cSOKkb8RNekuuCgE9S2%2BFaHyMs%2B3dPa9QtsdG3YcAfIZ8LwzByZRSfrWF6MfhaAfNOEWfeyfxaSWZZx%2B4amLCXwPiBimvxA%2Ff5jJUovUttuH%2FU2%2Fx3rwfGajlM4o84vrIKKl1qjsZhuTCwIn8bfz9HxieyQDjeRNhTgGuAt1MK6fGmVD2BWpaGd9w2yHTE222v7zACxQu8WrWn1SnJMZbeJyyLD3sQm91Ne57QgYRMGRycq1Ou2QGOUkF%2FuAulkjOvIFAjPe07zHCyV9kX8h49NqWuOGGgZQShSRQWJdUVaraux10Nqmc1a5auzT7JlRtobnNHDUVCsjBKykwiHawyzKJNe%2BQxWcfmLbDVSMP9JTJxvt%2Fr%2FNCyUL9sN4jcA3r8aGjjilxIsxVILKlgwDA%2FM5xO010AtJ1jsOe4U%2FvLkfngznvVUxxU3KfU55IP2X7uHeCZ8Ei%2F%2FSadtvULUvJPqzib%2F4Rwn5MhmRAn6ePcUDVaxDPzeTYAp4c3MPQm4oRH85MRRXA77lA6XmIaf8W0SaksvE8DOhSK79azfOeYiVB21osOqiQJhej3m4%2F%2FLQlTdUuP8OBeueQ56H%2ByUhU6e6q4yeVTQxeG0dsAyi%2B5AyduS2zgocfLck6hkiX2octeVY4nREgV%2Bewb8%2B%2BVMAbt1Wha5K03CvxUa%2BGPBLepjdPeWw28YUij0%2BJs5%2BoFE1MyP%2BadM2dKWPQDWM4CQgGhHYEtpEt17sumnvQA868taWFwHA88MZd%2BtXiYZMWquDmekKVYMaFsoiedfY8w897rQNb0gSLXoWXOs14JtVIYx%2BNu4%2F%2FLl3YHzMniN9FtRpSvQEmDY7AYe1luXcG%2BtZb4lo%2FVdADc6QOXXbGITK%2BECq7ww3RLrYlY3KKwBI6QkRxfMLQmznuNIdm5RmST%2BmJJ0JIUVQyQ5NTuGxx9CiQEP4TcpamMZ%2FSVbTpykWrxL44kI7X44SqbPsx26fD71Qg6WXyLXkRjx%2BuwMJjyss7Dgt288RDpiwGLkQ1ccSpx3%2BCsJyI0HEKyh38rClj8XgHYZiiszxkH9rsizQkzt0mHjPrBVkSUaZOjGN7HTzMyv3zJCqohdjYVruoRCDlWB%2F8UgfTRRzF9PBgTToojqnC5wwWNtB83XMMcK83niy9ycDAL16thx0vxhx2rVdK9GnPaC5C%2FVS6dkA8seryip8XYdKXQwuCBVwhKCUgWtWu21ffFSNcKSYh4zOylC4yJd%2FHD5I8kA%2BBP54%3D&__VIEWSTATEGENERATOR=3F1D2CC7&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=3MeVR2ARcxwwgDIpmzhIz6e0P%2BHEJIzw%2BEmhH%2Fvny6FuNhtcq9LABi52ZS5av3em90%2F1VT6RDNWHykf3qrkb9HTUg%2FC472C8gauFaFoiRfHIIejdITmRrmJyNlSymlUH8jdo%2Fw%3D%3D&txtPartNo=" + $txt + "&btnLookup=Search&TextBoxWatermarkExtender1_ClientState=&txtSRP5=&TextBoxWatermarkExtender2_ClientState=")\n' \
                         '$s.Content'  # command to open catheter catalog and search 'search_data'
