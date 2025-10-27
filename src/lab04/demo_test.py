from io_txt_csv import read_text, write_csv
text=read_text('data/lab04/input.txt')
print(text)
write_csv([('word','count'),('test',1)],'data/lab04/check.csv')