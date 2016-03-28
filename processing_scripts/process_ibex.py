import csv
import itertools
from nltk import WordNetLemmatizer
from operator import itemgetter
import pyvona
import re

lemmy = WordNetLemmatizer()

ibex_data = 'U:/Experiments/sleepHSP/results/results.csv'
# output_file = 'U:/Experiments/Sleep Study/processing_scripts/output.csv'

with open(ibex_data, 'rb+') as ibex_data:
    ibex_data = csv.reader(filter(lambda data_row: data_row[0] != '#', ibex_data))
    ibex_data = list(ibex_data)
    print ibex_data
#     subj = 0
#     mystery_word = 3
#     target_word = 4
#     condition = 5
#     trial = 6
#     g1, g2, g3, g4, g5 = 7, 8, 9, 10, 11
#     c1, c2, c3, c4, c5 = 12, 13, 14, 15, 16
#     exclude = 23
#
#     subj_dict = {}
#
#     for line in ibex_data[1:]:
#         for e in [line[g1], line[g2], line[g3], line[g4], line[g5]]:
#             e = e.strip()
#
#         if (line[subj], line[condition]) not in subj_dict:
#             subj_dict[(line[subj], line[condition])] = {(line[target_word], line[mystery_word]):
#                                                             [[(line[g1], line[c1]),
#                                                               (line[g2], line[c2]),
#                                                               (line[g3], line[c3]),
#                                                               (line[g4], line[c4]),
#                                                               (line[g5], line[c5])]]}
#         else:
#             # pass
#             if (line[target_word],line[mystery_word]) in subj_dict[(line[subj],line[condition])]:
#                 subj_dict[(line[subj], line[condition])][(line[target_word], line[mystery_word])] += \
#                                                              [[(line[g1], line[c1]),
#                                                               (line[g2], line[c2]),
#                                                               (line[g3], line[c3]),
#                                                               (line[g4], line[c4]),
#                                                               (line[g5], line[c5])]]
#             else:
#                 subj_dict[(line[subj],line[condition])][(line[target_word],line[mystery_word])] = \
#                                                              [[(line[g1], line[c1]),
#                                                               (line[g2], line[c2]),
#                                                               (line[g3], line[c3]),
#                                                               (line[g4], line[c4]),
#                                                               (line[g5], line[c5])]]
#
# print subj_dict
#
# with open(output_file, 'wb+') as output_file:
#     output_file = csv.writer(output_file)
#     output_file.writerow(['Subject', 'Condition', 'Mystery Word', 'Target Word', 'Highest-rated incorrect guess', 'Lowest-rated incorrect guess', 'All non-target guesses (most recent first)'])
#
#     for_tts = set()
#
#     for k,v in subj_dict.iteritems():
#         subj_number = k[0]
#         subj_condition = k[1]
#         print "Subject {}, Condition {}:".format(subj_number, subj_condition)
#         for t_word_m_word, g_c_list in v.iteritems():
#             target = t_word_m_word[0]
#             mystery = t_word_m_word[1]
#
#             guesses = []
#
#             reverse_list = reversed(g_c_list)
#             for gc in reverse_list:
#                 gc = reversed(gc)
#                 for guess in gc:
#                     lemmatized_guess = lemmy.lemmatize(guess[0].decode('unicode_escape').encode('ascii','ignore'), pos='n')
#                     lemmatized_guess = lemmatized_guess.encode('utf-8')
#                     if lemmatized_guess == 'horsey':
#                         lemmatized_guess = 'horse'
#                     guesses.append((lemmatized_guess, guess[1]))
#             # guesses = [guess for guess in guesses if guess != ('', '')]
#             # guesses = [guess for guess in guesses if guess != ('-', '-')]
#             # guesses = [guess for guess in guesses if guess[0] != '']
#             # guesses = [guess for guess in guesses if guess[1] != '']
#             guesses = [guess for guess in guesses if guess[0].strip() != target and guess[0] != '' and guess[1].isdigit() == True]
#
#             highest_incorrect = max(guesses, key=itemgetter(1))[0]
#             lowest_incorrect = min(guesses, key=itemgetter(1))[0]
#
#             print "Mystery Word: {}, Target Word: {}\nLowest incorrect guess: {}\nHighest incorrect guess: {}".format(mystery, target, lowest_incorrect, highest_incorrect)
#
#             for_tts.add(("Does {} mean {}?".format(mystery, target), "{}_{}".format(mystery, target)))
#             for_tts.add(("Does {} mean {}?".format(mystery, highest_incorrect), "{}_{}".format(mystery, highest_incorrect)))
#             for_tts.add(("Does {} mean {}?".format(mystery, lowest_incorrect), "{}_{}".format(mystery, lowest_incorrect)))
#
#             print "Guesses (most recent first): " + str(guesses)
#             print '\n'
#
#             row = [subj_number, subj_condition, mystery, target, highest_incorrect, lowest_incorrect, str(guesses)]
#             output_file.writerow(row)