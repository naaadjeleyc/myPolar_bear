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
        # Country.objects.all().delete()
        print("Command parse_docx started")
    base_dir = Path(__file__).resolve().parent.parent.parent.parent
    docx_path = str(
        base_dir) + '/datasources/Data_Extract_From_World_Development_Indicators.xlsx'
    df = pd.read_excel(str(docx_path), usecols=[
                       0, 1], sheet_name="Data", na_values=['NA'])
    country_name_col = df['Country Name']
    country_code_col = df['Country Code']

    for i in range(len(country_name_col)):
        country_exist = Country.objects.filter(country_name=country_name_col[i]).exists()
        if not(country_exist) and isinstance(country_code_col[i], str):
            country_row = Country.objects.create(
                country_name=country_name_col[i],
                country_code=country_code_col[i]
            )
            country_row.save()
