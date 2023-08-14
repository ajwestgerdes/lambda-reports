import pandas

def create_excel(data, file_name):
    df = pandas.DataFrame({
        "Function Name": data['function_name'],
        "Last Invocation (days)": data['last_invocation'],
        "Last Lambda Modification": data['last_modified'],
        "Code Size (bytes)": data['code_size'],
        "Runtime": data['runtime'],
        "Description": data['description']
    })
    df.to_excel(file_name, sheet_name='Lambda Report', index=False)
