import pandas

def create_excel(data):
# create an empty dataframe
df = pandas.DataFrame()

# loop through your flat dictionary and add each key-value pair to the dataframe
for key, value in flat_dict.items():
    df[key] = value

# create a new Excel writer object
writer = pandas.ExcelWriter('output.xlsx', engine='xlsxwriter')

# write the dataframe to a new sheet in the Excel file
df.to_excel(writer, sheet_name='Sheet1', index=False)

# continue adding to the same sheet over time
for i in range(10):
    # create a new dataframe with new data
    new_df = pandas.DataFrame({'new_key': [i], 'new_value': [f'new_value_{i}']})

    # add the new data to the existing dataframe
    df = pandas.concat([df, new_df], axis=0)

    # write the updated dataframe to the same sheet in the Excel file
    df.to_excel(writer, sheet_name='Sheet1', index=False)

# save and close the Excel writer
writer.save()
writer.close()