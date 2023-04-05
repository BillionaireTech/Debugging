# There are a few potential errors in this code:
# 1. The script does not import openpyxl module to work with Excel files. You need to add the following line at the beginning of the script:

import openpyxl

# 2. The script is trying to save the DataFrame df to the Excel file instead of the result variable. You need to change the line:

df.to_excel(writer, sheet_name=sheet_name, index=False)
#to:
pd.DataFrame({'result': [result]}).to_excel(writer, sheet_name=sheet_name, index=False)

# 3. The script is using the variable df to save the results to the Excel file, which will overwrite the original data read from the file. To fix this, you need to create a new DataFrame to store the results for each strategy. Replace the line:

df = pd.read_excel('C:/Users/bahgat/Downloads/columns_to_be_used (6).xlsx')
#with:
df_input = pd.read_excel('C:/Users/bahgat/Downloads/columns_to_be_used (6).xlsx')
results = []

#Then, replace the line:

df.to_excel(writer, sheet_name=sheet_name, index=False)
#with:
results.append(result)
pd.DataFrame({'result': results}).to_excel(writer, sheet_name=sheet_name, index=False)

# 4. The script is not handling the case where the PandasData object cannot be created for a given input dictionary. In this case, the script should skip the current iteration of the loop and continue with the next one. To fix this, you need to add the continue statement to the except block:

except Exception as e: 
    print(f"Error creating PandasData object for Strategy {index+1}: {e}") 
    continue 

    #This will ensure that the script skips the current iteration of the loop and moves on to the next one if there is an error creating the PandasData object.

# 5. The script is not passing the params dictionary to the MyStrategy class constructor. To fix this, you need to change the line:

cerebro.addstrategy(MyStrategy, **input_dict)
#to:
cerebro.addstrategy(MyStrategy, **input_dict, **MyStrategy.params)

#This will ensure that the params dictionary is also passed to the MyStrategy class constructor.
