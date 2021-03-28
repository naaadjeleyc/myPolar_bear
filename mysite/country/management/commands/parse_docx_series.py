import os
import pandas as pd
import numpy as np
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
from country.models import Country


class Command(BaseCommand):
    help = "load data from docx"

    def handle(self, *args, **options):
        # Series.objects.all().delete()
        print("Command parse_docx_series started")
    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    docx_path = str(
        base_dir) + '/datasources/Data_Extract_From_World_Development_Indicators.xlsx'
    df = pd.read_excel(str(docx_path), usecols=[
                       2, 3], sheet_name="Data", na_values=['NA'])
    series_name_col = df['Series Name']
    series_code_col = df['Series Code']

    for i in range(len(series_name_col)):
        series_exist = Series.objects.filter(
            series_name=series_name_col[i]).exists()
        if not(series_exist) and isinstance(series_code_col[i], str):
            series_row = Series.objects.create(
                series_name=series_name_col[i],
                series_code=series_code_col[i]
            )
            series_row.save()
