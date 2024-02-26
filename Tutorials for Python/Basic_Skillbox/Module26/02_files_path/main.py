# TODO здесь писать код

import os
from typing import Optional


def gen_files_path(dir_name: str, path: str = os.path.abspath(os.sep)) -> Optional[str]:
    result_paths = ""
    for i_elem in os.listdir(path):
        if i_elem == dir_name:
            path_gen = os.walk(os.path.join(path, i_elem))
            for i_path in path_gen:
                for i_file in i_path[2]:
                    result_paths += f"{os.path.join(i_path[0], i_file)}\n"
            else:
                return result_paths
        elif os.path.isdir(os.path.join(path, i_elem)):
            result = gen_files_path(dir_name, path=os.path.join(path, i_elem))
            if not (result is None):
                return result
    else:
        return None


print(gen_files_path("Module19", path=os.path.abspath("../../../Python_Basic")))

# зачтено
