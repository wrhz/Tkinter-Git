import tkinter as tk
from tkinter import ttk
import json
import git
import subprocess
from threading import Thread

WIDTH: int = 400
HEIGHT: int = 300

options: list[str] = ["初始化仓库", "克隆仓库"]
option: str = ""

with open("src/config.json", "r") as f:
    config: dict = json.load(f)

if config.get("username"):
    subprocess.run(["git", "config", "--global", "user.name", config.get("username")])
if config.get("email"):
    subprocess.run(["git", "config", "--global", "user.email", config.get("email")])

def do_init(init_path):
    try:
        repo = git.Repo.init(init_path)
        print(repo)
    except Exception as e:
        error.config(text=str(e), fg="red")

def do_clone(url, save_path):
    try:
        repo = git.Repo.clone_from(url, save_path)
        print(repo)
    except Exception as e:
        error.config(text=str(e), fg="red")

def init_repo():
    global option, tk, win, error

    try:
        if option == "init":
            entries = [child for child in win.winfo_children() 
                if isinstance(child, tk.Entry)]
            if len(entries) >= 2:
                input_init_path_entry = entries[1]
                input_init_path = input_init_path_entry.get()
                if input_init_path:
                    Thread(
                        target=do_init,
                        args=(input_init_path,),
                        daemon=True
                    ).start()
                else:
                    error.config(text="请输入初始化仓库路径", fg="red")
        else:
            error.config(text="请选择相匹配的模式", fg="red")
    except Exception as e:
        error.config(text=str(e), fg="red")

def clone_repo():
    global option, config, tk, win, error

    try:
        if option == "clone":
            entries = [child for child in win.winfo_children() 
                if isinstance(child, tk.Entry)]
            
            if len(entries) >= 3:
                url_or_name = entries[1].get()
                save_path = entries[2].get()
                if url_or_name and save_path:
                    names = config.get("names")
                    if not names.get(url_or_name):
                        Thread(
                            target=do_clone,
                            args=(url_or_name, save_path),
                            daemon=True
                        ).start()
                    else:
                        Thread(
                            target=do_clone,
                            args=(names[url_or_name], save_path),
                            daemon=True
                        ).start()
                else:
                    error.config(text="请输入完整信息", fg="red")
        else:
            error.config(text="请选择相匹配的模式", fg="red")
    except Exception as e:
        error.config(text=str(e), fg="red")

def on_select_get_option(_):
    global option, win, git_options, error

    try:
        now_option: str = git_options.get()

        for widget in win.winfo_children():
            if widget != git_options and widget != error:
                widget.destroy()
        
        match now_option:
            case "初始化仓库":
                option = "init"
                input_init_path_label = tk.Label(win, text="请输入初始化仓库路径")
                input_init_path_label.pack()
                input_init_path_entry = tk.Entry(win)
                input_init_path_entry.pack()

                init_button = tk.Button(win, text="初始化", command=init_repo)
                init_button.pack()

            case "克隆仓库":
                option = "clone"
                input_url_or_name_label = tk.Label(win, text="请输入仓库地址或名称")
                input_url_or_name_label.pack()
                input_url_or_name_entry = tk.Entry(win)
                input_url_or_name_entry.pack()

                input_save_path_label = tk.Label(win, text="请输入保存路径")
                input_save_path_label.pack()
                input_save_path_entry = tk.Entry(win)
                input_save_path_entry.pack()

                clone_button = tk.Button(win, text="克隆", command=clone_repo)
                clone_button.pack()

            case _:
                option = ""
                empty_text = tk.Label(win, text="暂无选择情况", fg="gray")
                empty_text.pack(expand=True)
    except Exception as e:
        error.config(text=str(e), fg="red")

if __name__ == "__main__":
    win: tk.Tk = tk.Tk()

    win.title("Tkinter Git")

    win.geometry(f"{WIDTH}x{HEIGHT}+{(win.winfo_screenwidth() - WIDTH) // 2}+{(win.winfo_screenheight() - HEIGHT) // 2}")

    git_options = ttk.Combobox(win, values=options)
    git_options.pack()
    git_options.bind("<<ComboboxSelected>>", on_select_get_option)

    empty_text = tk.Label(win, text="暂无选择情况", fg="gray")
    empty_text.pack(expand=True)

    error = tk.Label(win, text="", fg="red")
    error.pack()

    win.mainloop()
