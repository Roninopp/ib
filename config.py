# FILL THESE VALUES ACCORDINGLY.

from THANOSPRO.config.rishu_config import Config

class Development(Config):
  # get these values from my.telegram.org. 
  APP_ID = 76359    # 6 is a placeholder. Fill your 6 digit api id
  API_HASH = "78ba6352dd5cdc166fdef5aa84ba7c67"   # replace this with your api hash

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "postgres://qdilvugl:RSz_qLCVe07nPfWN6ahTY8Qryp_9fuhs@ruby.db.elephantsql.com/qdilvugl"
  ALIVE_NAME = "Ronin"
  # After cloning the repo and installing requirements...
  # Do `python string.py` and fill the on screen prompts.
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  THANOSPRO_SESSION = "1BVtsOJUBu3_kEu_mV76-5FIKSgdBPlFXvTma7Fxyv96szkmXAkG6WT5Yi_P3sXZ11aVSvqFAAQZ5jCa9B-Mlb5uE3dustOUNgzjHRNFcTBxkMGfNZ7iD0kWIX8sTMrOOhD5wnUllCs3bpVxLWxxSiZfvVg66gq_ytKgk7MMw428Q9LN0DksGJPX3I3GZlvsFd1CKOFP-appcToR_nAAahsOtbB7aIu4IhbY8RYTo79k_m041xnGohdVgV9MkozgqGldx6osIIcUAji5t33AWB3o-ac6xDP5eLrTDRk3vCbkWo3F2W2QuO3z7Ex5cSqibgFYt7h1E_oDjgHFRoMqoL2TzsAvNsL8="

  # Create a bot in @BotFather
  # And fill the following values with bot token and username.
  BOT_TOKEN = "5420641611:AAFRadnL6Z16KVBIW72IyPl3V9OJ98YlmwI" #token
  #FILL BOT USERNAME WITHOUT @
  BOT_USERNAME = "GAANDFAADNEWAALIBOT"
  # Custom Command Handler. 
  HANDLER = "."
 

  # Custom Command Handler for sudo users.
  SUDO_HANDLER = "!"
  # if u want to add sudo then remove #
  #SUDO_USERS = [1793699293]


# end of required config
# THANOSPRO
