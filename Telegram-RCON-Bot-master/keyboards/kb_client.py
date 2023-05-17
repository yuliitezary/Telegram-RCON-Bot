#
#           Контакты разработчика:
#               VK: vk.com/dimawinchester
#               Telegram: t.me/teanus
#               Github: github.com/teanus
#
#
#
# ████████╗███████╗ █████╗ ███╗   ██╗██╗   ██╗███████╗
# ╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██║   ██║██╔════╝
#    ██║   █████╗  ███████║██╔██╗ ██║██║   ██║███████╗
#    ██║   ██╔══╝  ██╔══██║██║╚██╗██║██║   ██║╚════██║
#    ██║   ███████╗██║  ██║██║ ╚████║╚██████╔╝███████║
#    ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_id = KeyboardButton('🆔айди')
button_rcon = KeyboardButton('❗ркон')
button_info = KeyboardButton('🆘инфо')
button_support = KeyboardButton('🆘поддержка')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(button_id, button_rcon, button_info, button_support)

button_cancel = KeyboardButton('◀отмена')
rcon_cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)