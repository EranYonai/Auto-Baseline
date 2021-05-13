PASSWORDS = {
    'DB_MANAGER': 'dbManager'
}
FILE_PATHS = {
    'DB_LOCATION': "C:\\Users\\eyonai\\OneDrive - JNJ\\Documents\\GitHub\\Baseliner\\Code\\db\\"
}

APPLICATION_VERSION = {
    'AutoBaseline': '1.1',
    'Inventory': '0.2'
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
    'DEMO': 'demos'
}

DIALOGS_FIELD_NAMES = { # FIXME
    'workstations': ['Service Tag', 'DSP Version', 'Image Version', 'Configuration', 'Model', 'Graphics Card'],
    'systems': ['System Number', 'PIU Configuration', 'Location Pad', 'Patch Unit', 'Monitor 1', 'Monitor 2',
                'ECG Phantom', 'Aquarium Number', 'Aquarium Maximo']
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
    'STOCKERT': [["software_version", "STRING PRIMARY KEY"], ["serial_number", "STRING"],
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
                 ["spu_pro_rev", "STRING"], ["approved", "BOOLEAN"],
                 ["used", "INTEGER"]],
    'DEMO': [["service_tag", "STRING PRIMARY KEY"], ["ws_type", "STRING"],
                  ["sw_version", "STRING"], ["dsp_version", "STRING"],
                  ["image_version", "STRING"], ["approved", "BOOLEAN"],
                  ["used", "INTEGER"]]
}

MIN_CORRELATION = 0.7
MAX_CORRELATION = 1
PERCENTAGE_TO_PASS_DB = 0.8