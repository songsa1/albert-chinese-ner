#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/13 15:51
# @Author  : SongSa
# @Desc    : 构造数据集
# @File    : create_data.py
# @Software: PyCharm
import os
import pandas as pd

type_dict = {
    "疾病":"ill",
    "检查和数字":"che",
    "科室":"fac",
    "器械":"ins",
    "患者类型":"pty",
    "基因/蛋白":"gep",
    "药物":"med",
    "评估指标":"eva",
    "物种":"spe",
    "耐药":"dru",
    "研究类型":"res",
    "人群":"cro",
    "治疗":"cur",
    "身体部位":"bod",
    "疾病程度/病理":"deg",
    "病因/机制":"eti",
    "症状":"sym",
    "疗效描述":"eff",
    "研究方向":"reo",
    "不良反应":"adv"
}

# a = []
# for i in type_dict.values():
#     a.append('B-{}'.format(i))
#     a.append('I-{}'.format(i))
# print(a)
# print(1)
#
#
#
#
#
#
#
# df = pd.read_excel(r'F:\code\NLP\NLP_job\albert-chinese-ner\全领域.xlsx')
# df = df.astype('str')
# train_f = open('train.txt', 'w', encoding='utf-8')
# dev_f = open('dev.txt', 'w', encoding='utf-8')
# test_f = open('test.txt', 'w', encoding='utf-8')
#
# print(len(set(df['text'])))
# the_num = 0
# for row in set(df['text']):
#     the_num += 1
#     if the_num <= 3400:
#         f = train_f
#     elif the_num <= 4000:
#         f = dev_f
#     else:
#         f = test_f
#     label_index_dict = {}
#     row_df = df[df['text'] == row]
#     for index, r_row in row_df.iterrows():
#         r_row = dict(r_row)
#         print(r_row)
#         index_list = r_row['range'].split(',')
#         for t_index in range(int(index_list[0]), int(index_list[1])):
#             if t_index == int(index_list[0]):
#                 label_index_dict[t_index] = 'B-{}'.format(type_dict[r_row['type']])
#             else:
#                 label_index_dict[t_index] = 'I-{}'.format(type_dict[r_row['type']])
#     for the_i, the_r in enumerate(row):
#         if the_r in [' ', '\r', '\n', '\t']:
#             continue
#         else:
#             if the_i in label_index_dict.keys():
#                 f.write('{} {}'.format(the_r, label_index_dict[the_i]))
#                 f.write('\n')
#             else:
#                 f.write('{} O'.format(the_r))
#                 f.write('\n')
#     f.write('\n')
#     print(1)


# train_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\train.txt', 'w', encoding='utf-8')
# dev_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\dev.txt', 'w', encoding='utf-8')
# test_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\test.txt', 'w', encoding='utf-8')
#
# file_lists = os.listdir(r'C:\Users\ss\Desktop\糖尿病')
# for index, file_name in enumerate(file_lists):
#     if index <400:
#         f = train_f
#     elif index < 490:
#         f = dev_f
#     else:
#         f = test_f
#     file_name = r'C:\Users\ss\Desktop\糖尿病\{}'.format(file_name)
#     print(file_name)
#     with open(file_name, 'r', encoding='utf-8') as t_f:
#         for i in t_f.readlines():
#             print(i)
#             f.write(i.replace('\t', ' '))

# train_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\train.txt', 'r', encoding='utf-8')
# dev_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\dev.txt', 'r', encoding='utf-8')
# test_f = open(r'F:\code\NLP\NLP_job\albert-chinese-ner\test.txt', 'r', encoding='utf-8')
#
# train_list = []
# for row in test_f.readlines():
#     if row:
#         train_list.append(row.split('\t')[-1].replace('\n', '').split('-')[-1])
# print(set(train_list))
# print(len(set(train_list)))

# a = {'Level', 'Drug', 'Reason', 'Frequency', 'Amount', 'Test_Value', 'Duration', 'Operation', 'Treatment', 'Anatomy', 'Disease', 'SideEff', 'O', 'Test', 'Symptom', 'Method'}
# labels_list = []
# for i in a:
#     print(i)
#     labels_list.append('B-{}'.format(i))
#     labels_list.append('I-{}'.format(i))
# print(labels_list)

# with open(r'F:\code\NLP\NLP_job\albert-chinese-ner\train.txt', 'r', encoding='utf-8') as f:
#     for i in f.readlines():
#         print(i)