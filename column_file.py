#! /usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Dict, List
from datetime import datetime
from numpy import nan

def parse_col(list_ligns: List, info: Dict, remove_zero_ending: bool) -> Dict:
    dic_scallar={}
    # Fichier une colonne
    dic_scallar["start_date"] =datetime.strptime(f"""{'-'.join([list_ligns[i]
                                                 for i in [2,0,1]])}""", "%y-%m-%d")
    dic_scallar["start_time"] = f"""{':'.join([list_ligns[i] for i in [10,11,12]])}"""
    for key, val in info.items():
        if key in "cuteval":
            pass
        elif not isinstance(val, list):
            dic_scallar[key] = list_ligns[val]
        elif len(val) == 2:
            tmp_lst = list_ligns[val[0]:val[1]] if val[1] != "end" \
                else list_ligns[val[0]:]
            if remove_zero_ending :
                print(f"I delete some Zero ending : {type(tmp_lst[-1])} | {tmp_lst[-1]}")
                while tmp_lst[-1] in "0." and len(tmp_lst) > 1:
                    tmp_lst = tmp_lst[:-1]
            dic_scallar[key] = tmp_lst
        else:
            raise SyntaxError(f"This value is not correctly defined : {val}")
    return dic_scallar


def col_selector(lst_dic: List[Dict])-> List[Dict]:
    lst_out=[]
    for dic_selected in lst_dic :
        # On cherche la taille de la liste la plus grande
        n_listmax = max([len(i) if isinstance(i, list) else 1 for i in dic_selected.values()])
        # On alligne les key sur la taille de la liste la plus grande
        for key, val in dic_selected.items():
            if not isinstance(val, list):
                dic_selected[key] = [val] * n_listmax
            elif len(val) != n_listmax:
                dic_selected[key] = val + [nan] * (n_listmax - len(val))
            else:
                pass
        lst_out.append(dic_selected.copy())
    # end of for on dic list
    return lst_out
