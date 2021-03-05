import csv
import pandas as pd
import numpy as np

def module_sum(filepath, object_list):
    data = pd.read_csv(filepath_or_buffer=filepath, encoding="UTF-8", sep=",")
    data['Dr.price'] = data['Dr.price'].astype(np.int64)
    data['Cr.price'] = data['Cr.price'].astype(np.int64)
    dr_sum = data['Dr.price'].sum()
    cr_sum = data['Cr.price'].sum()
    if dr_sum != cr_sum:
        context = {
            'object_list': object_list,
            'dr_sum': dr_sum,
            'cr_sum': cr_sum,
            'warning': '合計金額が一致しません',
        }
    else:
        context = {
            'object_list': object_list,
            'dr_sum': dr_sum,
            'cr_sum': cr_sum,
        }
    return context

def module_output(model):
    output_path = 'journalentryapp/output/'
    output_name = 'data.csv'
    object_list = model.objects.all()
    with open(output_path + output_name, 'w', encoding='UTF-8', newline='') as csv_file:
        header = ['date' ,'Dr.account' ,'Dr.price' ,'Dr.class' ,'Cr.account' ,'Cr.price' ,'Cr.class']
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        for obj in object_list:
            date = obj.date
            dr_account = obj.dr_account
            dr_price = obj.dr_price
            dr_class = obj.dr_class
            cr_account = obj.cr_account
            cr_price = obj.cr_price
            cr_class = obj.cr_class
            row = []
            row += date, dr_account, dr_price, dr_class, cr_account, cr_price, cr_class
            writer.writerow(row)
