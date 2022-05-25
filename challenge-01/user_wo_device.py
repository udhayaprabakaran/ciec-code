import pandas as pd

xl_in = pd.ExcelFile('table_data.xlsx', engine='openpyxl')

employees = xl_in.parse('Employees')
devices = xl_in.parse('Devices')

for i, emp in employees.iterrows():
    if emp['id'] not in devices['employee_id'].values:
        print('Users whose device has not been recorded: {} {}'.format(emp['first_name'], emp['last_name']))