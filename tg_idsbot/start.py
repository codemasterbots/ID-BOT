#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from data import Data
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.command("start"))
async def start(_, message):
    # Check if the user is not subscribed
    if not message.from_user.is_subscribed:
        # Send a message asking the user to subscribe
        await message.reply_text(
            "You must subscribe to use this bot. Please click the button below to subscribe.",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "Join Our Update Channel ❤️",
                        url="https://t.me/CodeMasterTG"
                    )
                ]]
            )
        )
        return

    # Your existing code for the start command
    # ...

