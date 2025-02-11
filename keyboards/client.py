from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from config import CHANNEL_URL


class ClientKeyboard:

#     async def start_keyboard():
#         ikb = InlineKeyboardBuilder()

#         ikb.button(text="Подписаться", url=CHANNEL_URL)
#         ikb.button(text="Проверить", callback_data="check")

#         ikb.adjust(1)

#         return ikb.as_markup()

    async def menu_keyboard():
        ikb = InlineKeyboardBuilder()

        # ikb.button(text="📚Qo`llanma", callback_data="instruction")
        ikb.button(text="Adminga yozing", url="t.me/swerlw")
        ikb.button(text="🚀Signal olish🚀", callback_data="get_signal")

        ikb.adjust(1, 1)

        return ikb.as_markup()

    async def register_keyboard():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="📱🔸 Royxatdan o`tmagan bo`lsangiz adminga yozing", url='t.me/Azamat_moneys')
        ikb.button(text="🔙Bosh menyuga qaytish",
                   callback_data="back")

        ikb.adjust(1)

        return ikb.as_markup()

    async def on_register_keyboard():
        ikb = InlineKeyboardBuilder()

        # ikb.button(text="Qo`llanma", callback_data="instruction")
        ikb.button(text="🚀Signal olish🚀", web_app=types.WebAppInfo(url="https://aviaflyuzbaza.netlify.app//"))
        ikb.button(text="🔙Bosh menyuga qaytish",
                   callback_data="back")

        ikb.adjust(1, 1)

        return ikb.as_markup()

    async def back_keyboard():
        ikb = InlineKeyboardBuilder()
        ikb.button(text="🔙Bosh menyuga qaytish",
                   callback_data="back")

        return ikb.as_markup()



        return ikb.as_markup()

    async def get_signal_keyboard():
        ikb = InlineKeyboardBuilder()

        ikb.button(text="🚀Signal olish🚀", web_app=types.WebAppInfo(url="https://aviaflyuzbaza.netlify.app//"))
        ikb.button(text="🔙Bosh menyuga qaytish",
                   callback_data="back")

        ikb.adjust(1)

        return ikb.as_markup()
