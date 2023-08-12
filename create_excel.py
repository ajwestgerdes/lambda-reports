import pandas

grouped_data = {}

# df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
#                    index=['row 1', 'row 2'],
#                    columns=['col 1', 'col 2'])
# df1.to_excel("output.xlsx")  

def create_excel(data):
    print(data)
    df = pandas.DataFrame({
        "Function Name": data['function_name'],
        "Last Invocation (days)": data['last_invocation'],
        "Last Lambda Modification": data['last_modified'],
        "Code Size (bytes)": data['code_size'],
        "Runtime": data['runtime'],
        "Description": data['description']
    })
    df.to_excel('test.xlsx', sheet_name='Lambda Report', index=False)
