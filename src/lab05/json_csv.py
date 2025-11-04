from pathlib import Path
import json,csv,sys
sys.path.append('C:/Users/dasha/Desktop/python_labs/src')
from lab04.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
    j_path=Path(json_path)
    if not j_path.exists(): 
        raise FileNotFoundError
    with open(j_path,'r',encoding='utf-8') as j_file:
        try:
            j_data=json.load(j_file)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        except not j_data: 
            raise ValueError('Файл JSON пуст')
        except isinstance(j_data,list):
            raise ValueError('Файл не является СПИСКОМ словарей')
        except all(isinstance(row,dict) for row in j_data):
            raise ValueError('Файл не является списком СЛОВАРЕЙ')
    c_path=Path(csv_path)
    ensure_parent_dir(c_path)
    with open(c_path,'w',encoding='utf-8', newline='') as c_file:
        c_writer=csv.DictWriter(c_file,fieldnames=j_data[0].keys())
        c_writer.writeheader()
        c_writer.writerows(j_data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    c_path=Path(csv_path)
    if not c_path.exists():
        raise FileNotFoundError
    if c_path.suffix != '.csv':
            raise ValueError("Неверный тип файла")
    with open(c_path,'r',encoding='utf-8') as c_file:
        c_data=csv.DictReader(c_file)
        if not c_data.fieldnames:
            raise ValueError('Файл пустой или в нем нет заголовков')
        c_rows=list(c_data)
        if not c_rows:
            raise ValueError('В файле есть заголовки, но нет данных')
    j_path=Path(json_path)
    ensure_parent_dir(j_path)
    with open(j_path,'w', encoding='utf-8') as j_file:
        json.dump(c_rows,j_file,ensure_ascii=False,indent=2)
