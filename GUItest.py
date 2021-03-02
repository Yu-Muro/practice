import tkinter as tk
from typing import Text

base_ground = tk.Tk() # メインウィンドウの作成
base_ground.title("GUItest") # ウィンドウのタイトルを設定
base_ground.geometry("800x500")

# フレーム一覧
frame_title = tk.Frame(base_ground)
frame_name = tk.Frame(base_ground)
frame_name_ruby = tk.Frame(base_ground)
frame_job = tk.Frame(base_ground)
frame_birth = tk.Frame(base_ground)
frame_address = tk.Frame(base_ground)
frame_entry_data = tk.Frame(base_ground)
frame_grade = tk.Frame(base_ground)
frame_history = tk.Frame(base_ground)

# タイトル
title = tk.Label(frame_title, text = "従業員データ入力")
title.pack(side = tk.TOP)

# ラベル
label_name_f = tk.Label(frame_name, text = "性")
label_name_f.grid(row = 0, column = 0)
label_name_l = tk.Label(frame_name, text = "名")
label_name_l.grid(row = 0, column = 2)
label_name_ruby_f = tk.Label(frame_name_ruby, text = "セイ").grid(row = 0, column = 0)
label_name_ruby_l = tk.Label(frame_name_ruby, text="メイ").grid(row = 0, column = 2)

# テキストボックス
txt_box_name_f = tk.Entry(frame_name, width = 20)
txt_box_name_f.grid(row = 0, column = 1)
txt_box_name_l = tk.Entry(frame_name, width = 20)
txt_box_name_l.grid(row = 0, column = 3)
txt_box_name_ruby_f = tk.Entry(frame_name_ruby, width = 20).grid(row = 0, column = 1)
txt_box_name_ruby_l = tk.Entry(frame_name_ruby, width = 20).grid(row = 0, column = 3)

# 位置決め
frame_title.pack()
frame_name.pack()
frame_name_ruby.pack()

base_ground.mainloop() # 画面の維持
