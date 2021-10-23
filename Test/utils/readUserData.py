from utils.excelUtils import *
from data.data import *
import ast

# Gchat
maxRow = getRowCount(user_data, gchat )
email = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 1), None)
userName = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 2), None)
seenOldBound = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 4), None)
# seenOldBound = [i.strip('][').split(', ') for i in seenOldBound]
seenOldBound = [ast.literal_eval(i) for i in seenOldBound]
room = remove_items(readsinglecol(user_data, gchat, 2, maxRow, 5), None)
#
# # sheet two
maxRow = getRowCount(user_data, time_message)
time = remove_items(readsinglecol(user_data, time_message, 2, maxRow, 1), None)
message = remove_items(readsinglecol(user_data, time_message, 2, maxRow, 2), None)
# print(email)
# print(userName)
# print(room)
# print(time)
# print(message)


# whats app
maxRow = getRowCount(user_data, whats_app_sheet)
phone = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 1), None)
whatsAppGroup = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 3), None)
whatsAppGroupMessage = remove_items(readsinglecol(user_data, whats_app_sheet, 2, maxRow, 2), None)
# print(phone)
# print(len(phone))
# # print(whatsAppGroup)
# print(whatsAppGroupMessage)


# skype
maxRow = getRowCount(user_data, skype_sheet)
people = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 1), None)
skypeName = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 2), None)
skypeGroup = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 3), None)
skypeMessage = remove_items(readsinglecol(user_data, skype_sheet, 2, maxRow, 5), None)
# print(people)
# print(skypeGroup)
# print(skypeMessage)

# GoogleMessages
maxRow = getRowCount(user_data, google_messages_sheet)
phoneNumber = remove_items(readsinglecol(user_data, google_messages_sheet, 2, maxRow, 1), None)
messages = remove_items(readsinglecol(user_data, google_messages_sheet, 2, maxRow, 3), None)

# convert string formatted list to actual list
# b = "[1, 2, 3, 4, 5]"
# res = b.strip('][').split(', ')
# print("final list", res)
# res = ast.literal_eval(b)
# print("final list", res)
