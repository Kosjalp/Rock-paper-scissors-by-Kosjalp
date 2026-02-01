import os

def playsound(user_os, playsoundfilepath):
  if user_os == "UNIX":
    os.system(f"afplay {playsoundfilepath}")
  elif user_os == "Linux":
    os.system(f"aplay {playsoundfilepath}")
  elif user_os == "Windows":
    import winsound
    try:
      winsound.PlaySound(playsoundfilepath, winsound.SND_FILENAME)
    except Exception as e:
      print(f"Error playing sound: {e}")