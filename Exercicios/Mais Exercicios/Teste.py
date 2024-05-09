from datetime import datetime

hora_atual = datetime.now().hour

if 6 <= hora_atual < 12:
    print("BOM DIA!😊")
elif 12 <= hora_atual < 18:
    print("BOA TARDE!😊")
else: # 18 < hora_atual < 6:
    print("BOA NOITE!😊")