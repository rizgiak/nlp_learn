"""
Extract PDF Information
"""

# pylint: disable=C0103
# pylint: disable=C0121
# pylint: disable=C0209

import os
import sys
import time

import json
import re

import fitz
import tabula
import PySimpleGUI as sg

print(fitz.__doc__)

if tuple(map(int, fitz.version[0].split("."))) < (1, 18, 18):
    raise SystemExit("require PyMuPDF v1.18.18+")

output_dir = "output"  # found images are stored in this subfolder

metadata_dir = output_dir + "/metadata/"
text_dir = output_dir + "/text/"
img_dir = output_dir + "/img/"
table_dir = output_dir + "/table/"

if not os.path.exists(output_dir):  # make subfolder if necessary
    os.mkdir(output_dir)
if not os.path.exists(metadata_dir):
    os.mkdir(metadata_dir)
if not os.path.exists(text_dir):
    os.mkdir(text_dir)
if not os.path.exists(img_dir):
    os.mkdir(img_dir)
if not os.path.exists(table_dir):
    os.mkdir(table_dir)


def fine_replace(txt):
    """
    fine replace
    """
    txt = txt.replace("-\n", "")
    txt = txt.replace("\n", " ")
    txt = txt.replace("'", "")
    return txt


def cut_references(txt):
    """
    cut references
    """
    last_start = len(txt)
    for m in re.finditer("references", txt.lower()):
        last_start = m.start()
    return txt[:last_start]


def dump_to_txt(txt, file_path):
    """
    dump txt
    """
    txt = cut_references(txt)
    with open(file_path, "w", encoding="utf-8", errors="ignore") as file:
        file.write(str(txt))


def dump_to_json(txt, file_path):
    """
    dump json
    """
    txt = json.dumps(metadata, ensure_ascii=False)
    dump_to_txt(txt, file_path)


def pymupdf_extract_text(file_path):
    """
    Load PDF
    """
    # print(fitz.__doc__)
    doc = fitz.open(file_path)
    md_res = doc.metadata
    num_pages = doc.page_count
    txt = ""

    for page_num in range(num_pages):
        page = doc.load_page(page_num)
        txt += page.get_text()

    txt = fine_replace(txt)

    doc.close()
    return md_res, txt


def pymupdf_extract_image(file_path, output_path):
    """
    extract image
    """
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    os.system("python pipeline/pymu_img.py " + file_path + " " + output_path)


def tabula_extract_table(file_path, output_path):
    """
    tabula_extract_table
    """
    t0 = time.time()
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    # Extract tables from the PDF
    tables = tabula.read_pdf(file_path, pages="all")
    id_ext = 0

    for idx, table in enumerate(tables):
        print("Checking table ", idx)
        is_ok = True

        if is_ok:
            is_ok = check_cells_length(table, 60)
        if is_ok:
            is_ok = check_cols_length(table, 60)

        if is_ok:
            table = check_null_ratio(table, 0.7)
            id_ext += 1
            table.to_csv(output_path + "/table" + str(idx) + ".csv", encoding="utf-8")

    print(str(len(tables)) + " tables in total")
    print(str(id_ext) + " tables extracted")
    t1 = time.time()
    print("total time %g sec" % (t1 - t0))


def check_null_ratio(df, rate):
    """
    check_null_ratio
    """
    ret = True
    total = df.shape[1]
    sumation = df.isnull().sum()
    list_isnull = [i / total > rate for i in sumation]
    drop_list = []
    for idv, val in enumerate(list_isnull):
        if val:
            drop_list.append(idv)
            ret = False
    df = df.drop(df.columns[drop_list], axis=1)
    if not ret:
        print("Recreate current table, reason: null rate = ", rate)
    return df


def check_cells_length(df, length):
    """
    check_cells_length
    """
    ret = True
    df_isnull = df.isnull()
    ix, jx = df.shape
    for i in range(ix):
        for j in range(jx):
            if df_isnull.iat[i, j] == False and len(str(df.iat[i, j])) > length:
                ret = False
    if not ret:
        print("Skip current table, reason: cell's value is too long")
        print(df.head())
        print("[END]")
    return ret


def check_cols_length(df, length):
    """
    check_cols_length
    """
    ret = True
    cols = df.columns
    cols_isnull = cols.isnull()
    for i, val in enumerate(cols):
        if cols_isnull[i] == False and len(val) > length:
            ret = False
    if not ret:
        print("Skip current table, reason: col's value is too long")
        print(df.head())
        print("[END]")
    return ret


# Run the app
if __name__ == "__main__":
    fdir = sys.argv[1] if len(sys.argv) == 2 else None
    if not fdir:
        fdir = sg.popup_get_folder("Select folder:", title="PDF Extraction")
    if not fdir:
        raise SystemExit()
    print(fdir)

    max_p = len(os.listdir(fdir))
    i_doc = 0
    print("==================================================  (0/" + str(max_p) + ") 0% complete")
    for filename in os.listdir(fdir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(fdir, filename)
            (metadata, text) = pymupdf_extract_text(pdf_path)
            text_loc = text_dir + filename + ".txt"
            md_loc = metadata_dir + filename + ".txt"
            img_loc = img_dir + filename
            table_loc = table_dir + filename
            tabula_extract_table(pdf_path, table_loc)
            pymupdf_extract_image(pdf_path, img_loc)
            dump_to_txt(text, text_loc)
            dump_to_json(metadata, md_loc)
            print(f"File: {filename}")

            i_doc += 1
            perc = (i_doc / max_p) * 100
            print(
                "==================================================  ("
                + str(i_doc)
                + "/"
                + str(max_p)
                + ") "
                + str(round(perc, 2))
                + "% complete"
            )
