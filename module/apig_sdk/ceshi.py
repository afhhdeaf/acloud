import ast


# d = '{"app_id":"c3d963fbcaec400d82b0ff8a9c1b3e9a","app_name":"DefaultApp_hid_8ueio2noh3nfsqy_iot","device_id":"60c899d0b86d7b02bc71af42_raventest2","node_id":"raventest2","gateway_id":"60c899d0b86d7b02bc71af42_raventest2","device_name":"phone","node_type":"GATEWAY","description":None,"fw_version":None,"sw_version":None,"device_sdk_version":None,"auth_info":{"auth_type":"SECRET","secret":"f7091f4d1d83e0935dce69c0390a4e97","fingerprint":None,"secure_access":true,"timeout":0},"product_id":"60c899d0b86d7b02bc71af42","product_name":"cqupt_test","status":"INACTIVE","create_time":"20210617T080117Z","tags":[],"extension_info":None}'
# print(ast.literal_eval(d))

# {
#     'app_id': 'c3d963fbcaec400d82b0ff8a9c1b3e9a', 
#     'app_name': 'DefaultApp_hid_8ueio2noh3nfsqy_iot', 
#     'device_id': '60c899d0b86d7b02bc71af42_raventest3',
#     'node_id': 'raventest3', 
#     'gateway_id': 
#     '60c899d0b86d7b02bc71af42_raventest3', 
#     'device_name': 'watch', 
#     'node_type': 'GATEWAY', 
#     'description': None, 
#     'fw_version': None, 
#     'sw_version': None, 
#     'device_sdk_version': None, 
#     'auth_info': {
#         'auth_type': 'SECRET', 
#         'secret': '25ac9486524d6ed5cad1840a24f9b83b', 
#         'fingerprint': None, 
#         'secure_access': False, 
#         'timeout': 0}, 
#     'product_id': '60c899d0b86d7b02bc71af42', 
#     'product_name': 'cqupt_test', 
#     'status': 'INACTIVE', 
#     'create_time': '20210618T042318Z', 
#     'tags': [], 
#     'extension_info': None
# }
x = {'switch_success': 0}
print('switch_success' in x)